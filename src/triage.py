import os
import re
import json
import time
import google.generativeai as genai
from PIL import Image

# Initialize the Vision Model (Gemini 1.5 Flash is highly recommended for fast, cheap image sorting)
# Make sure your GEMINI_API_KEY is set in your environment variables
api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
vision_model = genai.GenerativeModel('gemini-1.5-flash')

TRIAGE_PROMPT = """You are the Art Director for a professional Engineering Textbook.
Analyze the provided image extracted from a raw PDF. Classify it strictly as KEEP, DISCARD, or TRANSCRIBE.

Rules for KEEP:
- It is a technical diagram, schematic, circuit (e.g., pumps, valves), graph, or free-body diagram.

Rules for DISCARD:
- It is a university logo, company logo, decorative border, or tiny illegible artifact.

Rules for TRANSCRIBE:
- The image is purely a mathematical equation, formula, or data table trapped as a picture.

Output ONLY a raw JSON object with no markdown wrappers: 
{"decision": "KEEP|DISCARD|TRANSCRIBE", "reason": "brief explanation"}
"""

OCR_PROMPT = """Extract the mathematical equations or table from this image. 
Output ONLY valid LaTeX code. For math, wrap in \\[ and \\]. Do not include ```latex wrappers or any conversational text."""

def process_images(cache_dir="data/output/assets/"):
    """Scans extracted images, filters garbage, and OCRs trapped math."""
    if not os.path.exists(cache_dir):
        print("No image cache found. Skipping triage.")
        return []

    transcribed_assets = {}
    discarded_images = []

    print("🔍 Starting Visual Triage Agent...")

    for filename in os.listdir(cache_dir):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
            
        # NEW: Throttle to prevent "429 Too Many Requests"
        time.sleep(2.0)
        
        filepath = os.path.join(cache_dir, filename)
        
        try:
            img = Image.open(filepath)
            
            # 1. Hardware Filter: Delete tiny artifacts without wasting API tokens
            if img.width < 80 or img.height < 80:
                print(f"🗑️ DISCARD: {filename} (Artifact too small)")
                img.close()
                os.remove(filepath)
                discarded_images.append(filename)
                continue

            # 2. Vision API Triage
            response = vision_model.generate_content([TRIAGE_PROMPT, img])
            result_text = response.text.strip().replace('```json', '').replace('```', '')
            try:
                result = json.loads(result_text)
            except json.JSONDecodeError:
                result = {"decision": "KEEP", "reason": "JSON Error"}

            decision = result.get("decision", "KEEP") # Default to keep if confused

            if decision == "DISCARD":
                print(f"🗑️ DISCARD: {filename} - {result.get('reason')}")
                img.close()
                os.remove(filepath)
                discarded_images.append(filename)

            elif decision == "TRANSCRIBE":
                print(f"🧮 TRANSCRIBE: Rescuing math from {filename}...")
                ocr_response = vision_model.generate_content([OCR_PROMPT, img])
                extracted_latex = ocr_response.text.strip()
                
                # Save the LaTeX and delete the useless image file
                transcribed_assets[filename] = extracted_latex
                img.close()
                os.remove(filepath)
                discarded_images.append(filename) # Treat as discarded for the markdown cleaner

            else:
                print(f"✅ KEEP: {filename} - {result.get('reason')}")
                img.close()

        except Exception as e:
            print(f"⚠️ Error analyzing {filename}: {e}. Defaulting to KEEP.")

    # 3. Save Transcribed Math to a JSON file so the Drafter can inject it later
    if transcribed_assets:
        with open("data/output/transcribed_math.json", "w", encoding="utf-8") as f:
            json.dump(transcribed_assets, f, indent=4)
        print(f"💾 Saved {len(transcribed_assets)} rescued math equations.")

    return discarded_images

def clean_manuscript(manuscript_path, discarded_images):
    """Removes [ORIGINAL_ASSET] tags for images that were deleted or transcribed."""
    try:
        with open(manuscript_path, 'r', encoding='utf-8') as f:
            content = f.read()

        for filename in discarded_images:
            # Matches tags like [ORIGINAL_ASSET: page1_img1.png]
            pattern = r'\[ORIGINAL_ASSET:\s*.*?' + re.escape(filename) + r'\]'
            content = re.sub(pattern, '', content)

        with open(manuscript_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"🧹 Cleaned manuscript. Removed {len(discarded_images)} dead tags.")
    except FileNotFoundError:
        print(f"⚠️ Manuscript file not found: {manuscript_path}")

if __name__ == "__main__":
    # Test execution
    discarded = process_images()
    clean_manuscript("data/output/tagged_manuscript.txt", discarded)
