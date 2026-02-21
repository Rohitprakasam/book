"""
BookForge 5.0 — The Art Department (Phase 3)
==============================================
Post-processes the expanded manuscript by resolving placeholder tags:

    [ORIGINAL_ASSET: /assets/file.png]  →  ![Enhanced Figure](/assets/file.png)
    [NEW_DIAGRAM: {...json...}]         →  ![AI Generated](/assets/ai_generated/file.png)

Usage
-----
    from src.resolver import process_art_department
    final_md = process_art_department(expanded_text, style_config={...})
"""

from __future__ import annotations

import os
import re
import json
from io import BytesIO
from pathlib import Path

# Try importing google-genai
try:
    from google import genai
    from google.genai import types
    from PIL import Image
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

try:
    from PIL import Image, ImageEnhance, ImageFilter
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False

try:
    import litellm
except (ImportError, ModuleNotFoundError) as _e:
    litellm = None
    try:
        print("Warning: litellm not found. Some agent features may be disabled.")
    except UnicodeEncodeError:
        pass
from dotenv import load_dotenv

load_dotenv()

# Project-root-relative paths (work regardless of CWD)
_BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = _BASE_DIR / "data" / "output"
RESOLVED_PATH = OUTPUT_DIR / "resolved_manuscript.md"
AI_ASSETS_DIR = OUTPUT_DIR / "assets" / "ai_generated"


def _get_model() -> str:
    """Return the model identifier from the environment."""
    return os.getenv("DEFAULT_MODEL", "groq/llama3-8b-8192")


# ──────────────────────────────────────────────
# TASK A: Resolve Original Asset Tags (With AI Enhancement)
# ──────────────────────────────────────────────
def enhance_image_with_gemini(image_path: Path) -> Path:
    """
    Sends an image to Gemini Vision to describe it, then uses Imagen
    to regenerate a cleaner, enhanced version of the diagram.
    Falls back to Pillow enhancement if Gemini is unavailable.
    Returns the path to the enhanced image.
    """
    if not HAS_GENAI:
        print("[Art Dept] ⚠️ google-genai not installed. Falling back to Pillow.")
        return _enhance_image_with_pillow(image_path)

    # Define output path
    enhanced_dir = AI_ASSETS_DIR.parent / "enhanced_images"
    enhanced_dir.mkdir(parents=True, exist_ok=True)

    enhanced_path = enhanced_dir / image_path.name
    if enhanced_path.exists():
        print(f"  ♻️  Using cached enhanced image: {enhanced_path.name}")
        return enhanced_path

    print(f"  🤖 AI Enhancing: {image_path.name}...")

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    try:
        # Step 1: Describe the original image using Gemini Vision (bytes for google.genai)
        prompt = (
            "Describe this technical diagram in precise detail. "
            "Include all labels, arrows, flow directions, component names, "
            "mathematical symbols, dimensions, and spatial relationships. "
            "Be exhaustive — this description will be used to recreate the image."
        )
        image_bytes = image_path.read_bytes()
        mime = "image/png" if image_path.suffix.lower() == ".png" else "image/jpeg"
        describe_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Content(
                    parts=[
                        types.Part.from_bytes(data=image_bytes, mime_type=mime),
                        types.Part.from_text(text=prompt),
                    ]
                )
            ],
        )
        description = describe_response.text
        print(f"  📝 Description: {description[:100]}...")

        # Step 2: Regenerate a cleaner version using the description
        import time
        target_model = os.getenv("IMAGE_MODEL", "gemini-2.5-flash-image")
        enhance_prompt = (
            f"Create a clean, high-quality, professional textbook diagram based on "
            f"this description: {description}. "
            f"Use crisp lines, clear labels, white background, publication-quality rendering. "
            f"Make it suitable for a printed engineering textbook."
        )

        max_retries = 2
        for attempt in range(max_retries + 1):
            try:
                gen_response = client.models.generate_images(
                    model=target_model,
                    prompt=enhance_prompt,
                    config=types.GenerateImagesConfig(
                        number_of_images=1,
                        aspect_ratio="16:9",
                        person_generation="DONT_ALLOW",
                    ),
                )

                for generated_image in gen_response.generated_images:
                    image_bytes = generated_image.image.image_bytes
                    result_img = Image.open(BytesIO(image_bytes))
                    result_img.save(enhanced_path, quality=95)
                    print(f"  ✅ AI Enhanced: {enhanced_path}")
                    return enhanced_path

            except Exception as retry_e:
                error_str = str(retry_e)
                if ("429" in error_str or "RESOURCE_EXHAUSTED" in error_str) and attempt < max_retries:
                    delay = 30 * (attempt + 1)
                    print(f"  ⏳ Rate limit. Retrying in {delay}s...")
                    time.sleep(delay)
                    continue
                raise  # Re-raise for outer except

    except Exception as e:
        print(f"  ⚠️ Gemini enhancement failed: {e}")
        print(f"  ↩️ Falling back to Pillow enhancement...")
        return _enhance_image_with_pillow(image_path)

    return image_path  # Should not reach here


def _enhance_image_with_pillow(image_path: Path) -> Path:
    """
    Fallback: Enhance using Pillow (sharpen, contrast, denoise).
    Used when Gemini is unavailable or fails.
    """
    if not HAS_PILLOW:
        return image_path

    enhanced_dir = AI_ASSETS_DIR.parent / "enhanced_images"
    enhanced_dir.mkdir(parents=True, exist_ok=True)
    enhanced_path = enhanced_dir / f"pil_{image_path.name}"

    if enhanced_path.exists():
        return enhanced_path

    try:
        img = Image.open(image_path)
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")

        img = img.filter(ImageFilter.SHARPEN)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.3)
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.05)
        img = img.filter(ImageFilter.MedianFilter(size=3))
        img = img.filter(ImageFilter.SHARPEN)

        img.save(enhanced_path, quality=95)
        return enhanced_path
    except Exception:
        return image_path


def resolve_original_assets(text: str) -> str:
    """
    Replace ``[ORIGINAL_ASSET: <filepath>]`` tags with
    standard Markdown image syntax, enhancing them with Gemini AI.
    Falls back to Pillow if Gemini is unavailable.
    """
    pattern = r"\[ORIGINAL_ASSET:\s*(.+?)\]"

    def _replacer(match: re.Match) -> str:
        rel_path = match.group(1).strip()
        full_extracted_path = OUTPUT_DIR / "assets" / rel_path

        if full_extracted_path.exists():
            # Primary: Gemini AI enhancement (describe → regenerate)
            # Fallback: Pillow enhancement (sharpen/contrast)
            final_path = enhance_image_with_gemini(full_extracted_path)
            web_path = str(final_path).replace("\\", "/")
            return f"![Enhanced Figure]({web_path})"
        else:
            print(f"[Art Dept] ⚠️ Asset not found: {full_extracted_path}")
            return f"![Missing Asset]({rel_path})"

    resolved = re.sub(pattern, _replacer, text)
    original_count = len(re.findall(pattern, text))
    print(f"[Art Dept] Resolved & AI-Enhanced {original_count} tags")
    return resolved


# ──────────────────────────────────────────────
# TASK B: AI Image Generation (Imagen 3)
# ──────────────────────────────────────────────
def generate_textbook_diagram(subject: str, theme_config: dict, save_path: Path) -> bool:
    """
    Calls Google's image model to generate a stylized textbook illustration.
    """
    if not HAS_GENAI:
        print("[Art Dept] ⚠️ google-genai not installed. Skipping image generation.")
        return False

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    # Extract the illustration style generated by Phase 1
    style_prompt = theme_config.get(
        "illustration_style",
        "Flat vector illustration, clean lines, white background, educational textbook graphic"
    )

    # Combine the Drafter's subject with the Style Extractor's visual rules
    full_prompt = f"{subject}. {style_prompt}. High quality, technical diagram."
    print(f"  🎨 Generating: \"{subject[:50]}…\"")

    import time
    max_retries = 3
    base_delay = 30

    for attempt in range(max_retries + 1):
        try:
            target_model = os.getenv("IMAGE_MODEL", "gemini-2.5-flash-image")

            response = client.models.generate_images(
                model=target_model,
                prompt=full_prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio="16:9",
                    person_generation="DONT_ALLOW"
                )
            )

            for generated_image in response.generated_images:
                image_bytes = generated_image.image.image_bytes
                image = Image.open(BytesIO(image_bytes))

                save_path.parent.mkdir(parents=True, exist_ok=True)
                image.save(save_path)
                return True

        except Exception as e:
            error_str = str(e)

            # Check for Rate Limits (429)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                if attempt < max_retries:
                    delay = base_delay * (attempt + 1)
                    print(f"  ⏳ Rate limit hit. Retrying in {delay}s (Attempt {attempt+1}/{max_retries})...")
                    time.sleep(delay)
                    continue
                else:
                    print(f"  ❌ Image Gen Failed after {max_retries} retries (Rate Limit): {error_str[:100]}...")
                    return False

            print(f"  ❌ Image Generation Failed: {error_str[:200]}...")

            # Check for 404 Model Not Found to fail fast
            if "404" in error_str or "NOT_FOUND" in error_str:
                print("  ⚠️  Critical Model Error: Skipping further image generation for this run.")
                return False

            return False

    return False


def resolve_art_tags(text: str, theme_config: dict = None) -> str:
    """
    Finds [NEW_DIAGRAM] JSON tags, generates images, and replaces tags with markdown links.
    """
    if theme_config is None:
        theme_config = {}

    matches = []
    pattern_json = None

    # Pattern 1: Tagged [NEW_DIAGRAM: {...}]
    pattern_tag = r'\[NEW_DIAGRAM:\s*(\{.*?\})\s*\]'
    matches.extend(list(re.finditer(pattern_tag, text, re.DOTALL)))

    # Pattern 2: Raw JSON blocks (Fallback)
    if not matches:
        pattern_json = r'(\{\s*"subject":\s*".*?",\s*"type":\s*".*?"\s*\})'
        matches.extend(list(re.finditer(pattern_json, text, re.DOTALL)))

    if not matches:
        print("[Art Dept] No [NEW_DIAGRAM] tags or JSON blocks found.")
        return text

    print(f"[Art Dept] Found {len(matches)} diagram requests — generating assets…")
    AI_ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    def replacement_func(match):
        try:
            art_request = json.loads(match.group(1))
            subject = art_request.get("subject", "Engineering diagram")
            caption = art_request.get("caption", None)

            if not caption:
                caption = " ".join(subject.split()[:5]) + "..."

            safe_subject = re.sub(r'[^a-zA-Z0-9]', '_', subject)[:30]
            filename = f"ai_{safe_subject}.png"
            save_path = AI_ASSETS_DIR / filename

            # Check if exists to avoid re-gen (caching)
            if save_path.exists():
                print(f"  ♻️  Using cached: {filename}")
                return f"![{caption}](/data/output/assets/ai_generated/{filename})"

            success = generate_textbook_diagram(subject, theme_config, save_path)

            if success:
                return f"![{caption}](/data/output/assets/ai_generated/{filename})"
            else:
                return f"*[Image generation failed for: {subject}]*"

        except json.JSONDecodeError:
            print("  ⚠️ Malformed JSON in NEW_DIAGRAM tag")
            return "*[Malformed Art Request]*"

    # Apply replacements for both patterns
    text = re.sub(pattern_tag, replacement_func, text, flags=re.DOTALL)
    if pattern_json:
        text = re.sub(pattern_json, replacement_func, text, flags=re.DOTALL)
    return text


# ──────────────────────────────────────────────
# TASK C: Master Function
# ──────────────────────────────────────────────
def process_art_department(expanded_text: str, style_config: dict = None) -> str:
    """
    Run the full Art Department pipeline:
      1. Resolve [ORIGINAL_ASSET] → Enhanced Markdown images
      2. Resolve [NEW_DIAGRAM]    → AI Generated Images
      3. Save to ``resolved_manuscript.md``
    """
    print("\n══════════════════════════════════════════")
    print("  ART DEPARTMENT — Processing tags…")
    print("══════════════════════════════════════════\n")

    # Step 1: Original assets (with Pillow enhancement)
    text = resolve_original_assets(expanded_text)

    # Step 2: New diagrams (AI Generation)
    text = resolve_art_tags(text, style_config)

    # Step 3: Save
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RESOLVED_PATH.write_text(text, encoding="utf-8")

    print(f"\n[Art Dept] ✅ Resolved manuscript saved ({len(text):,} chars) → {RESOLVED_PATH}")

    return text


# ──────────────────────────────────────────────
# CLI ENTRY POINT
# ──────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    input_path = sys.argv[1] if len(sys.argv) > 1 else "data/output/tagged_manuscript.txt"
    text = Path(input_path).read_text(encoding="utf-8")
    process_art_department(text)
