"""
BookForge 5.0 — The Polished Publisher (7-Pass Math-Aware Sanitization Engine)
===============================================================================
Editor-in-Chief: applies 7 cleaning passes to produce a publication-ready
engineering textbook PDF with proper LaTeX math rendering.

Pipeline
--------
1. ``normalize_headings()``     — Fix H1/H2/H3 hierarchy
2. ``protect_math()``           — Shield $...$ and \[...\] from other passes
3. ``fix_code_and_content()``   — Code fences, bold, mermaid, leftover tags
4. ``sanitize_backslashes()``   — Escape \\n/\\r/\\t in code blocks only
5. ``strip_ai_chatter()``      — Remove AI preambles and meta-talk
6. ``fix_unicode()``           — Clean problematic Unicode characters
7. ``add_structure()``         — Page breaks, spacing, restore math
"""

import os
import re
import subprocess
from pathlib import Path


# ──────────────────────────────────────────────
# PATHS
# ──────────────────────────────────────────────
OUTPUT_DIR = Path("data/output")
RESOLVED_PATH = OUTPUT_DIR / "resolved_manuscript.md"
PRESS_READY_PATH = OUTPUT_DIR / "ready_for_press.md"
FINAL_PDF_PATH = OUTPUT_DIR / "BookForge_Final.pdf"

# ──────────────────────────────────────────────
# MATH PROTECTION STORAGE
# ──────────────────────────────────────────────
_math_placeholders: dict[str, str] = {}
_math_counter = 0


# ══════════════════════════════════════════════
# PASS 0: Strip Wrappers
# ══════════════════════════════════════════════
def strip_wrappers(text: str) -> str:
    """Pass 0: Remove wrapping markdown code fences (```markdown ... ```) if present."""
    text = text.strip()
    # Check if the entire text is wrapped in code fences
    if text.startswith("```"):
        # Remove first line (```markdown or just ```)
        text = re.sub(r'^```\w*\s*\n', '', text, count=1)
        # Remove last line (```)
        text = re.sub(r'\n```\s*$', '', text, count=1)
        print("[Sanitizer] Pass 0: Stripped outer markdown wrappers.")
    return text.strip()


# ══════════════════════════════════════════════
# PASS 1: Normalize Headings
# ══════════════════════════════════════════════
def normalize_headings(text: str) -> str:
    """Pass 1: Ensure strict H1/H2 structure. Demote garbage titles."""
    lines = text.split('\n')
    result = []
    prev_heading = ""
    
    # Patterns that indicate a FAKE H1 (not a real chapter title)
    fake_h1_patterns = [
        r'^# (Less|More) ',           # "# Less readable", "# More readable"
        r'^# Example',                 # "# Example usage:"
        r'^# (Using|Control|The) ',    # Code-like headings
        r'^# \d+\.\s',                 # Numbered items that shouldn't be H1
        r'^# [a-z]',                   # Starts with lowercase
        r'^# .{0,3}$',                 # Too short to be a chapter title
    ]
    
    h1_count = 0
    fixed_count = 0
    removed_dupes = 0
    
    for line in lines:
        # Check if this is an H1 heading
        if re.match(r'^# ', line):
            # Is it a fake H1?
            is_fake = any(re.match(pat, line) for pat in fake_h1_patterns)
            
            if is_fake:
                # Demote to H4
                line = '###' + line[1:]
                fixed_count += 1
            else:
                h1_count += 1
        
        # Remove duplicate consecutive headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)', line)
        if heading_match:
            current_heading = heading_match.group(2).strip()
            if current_heading == prev_heading:
                removed_dupes += 1
                continue
            prev_heading = current_heading
        else:
            prev_heading = ""
        
        result.append(line)
    
    text = '\n'.join(result)
    print(f"[Sanitizer] Pass 1: Normalized headings — {h1_count} H1s kept, "
          f"{fixed_count} fake H1s demoted, {removed_dupes} duplicates removed")
    return text


# ══════════════════════════════════════════════
# PASS 2: Protect Math Blocks
# ══════════════════════════════════════════════
def protect_math(text: str) -> str:
    """
    Replace LaTeX math with placeholders to prevent other passes
    from mangling backslashes in equations like $\\rho g h$.
    
    Protects:
    - Display math: \\[ ... \\]
    - Inline math: $...$  (not $$)
    - Display math: $$ ... $$
    """
    global _math_placeholders, _math_counter
    _math_placeholders = {}
    _math_counter = 0
    
    def _replace_math(match):
        global _math_counter
        _math_counter += 1
        key = f"%%MATH_{_math_counter}%%"
        
        # Clean inline math: $ V_D $ -> $V_D$
        content = match.group(0)
        if content.startswith('$') and not content.startswith('$$'):
            # Strip internal whitespace to please Pandoc/LaTeX
            inner = content[1:-1].strip()
            content = f"${inner}$"
            
        _math_placeholders[key] = content
        return key
    
    # Protect display math: \[ ... \]  (can span multiple lines)
    text = re.sub(
        r'\\\[.*?\\\]',
        _replace_math,
        text,
        flags=re.DOTALL
    )
    
    # Protect display math: $$ ... $$  (can span multiple lines)
    text = re.sub(
        r'\$\$.*?\$\$',
        _replace_math,
        text,
        flags=re.DOTALL
    )
    
    # Protect inline math: $...$ (single line, not empty)
    text = re.sub(
        r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)',
        _replace_math,
        text,
        flags=re.DOTALL
    )
    
    print(f"[Sanitizer] Pass 2: Protected {_math_counter} math blocks")
    return text


def restore_math(text: str) -> str:
    """Restore all math placeholders back to original LaTeX."""
    for key, value in _math_placeholders.items():
        text = text.replace(key, value)
    return text


# ══════════════════════════════════════════════
# PASS 3: Fix Code and Content
# ══════════════════════════════════════════════
def fix_code_and_content(text: str) -> str:
    """
    Merged pass: code fences, bold/italic, mermaid URLs, leftover tags.
    """
    fixes = 0
    
    # --- Fix Mermaid URLs ---
    mermaid_pattern = r'!\[([^\]]*)\]\(https://mermaid\.ink/img/[^\)]+\)'
    mermaid_count = len(re.findall(mermaid_pattern, text))
    text = re.sub(
        mermaid_pattern,
        lambda m: f"\n\n> 📊 *{m.group(1).strip() or 'Technical Diagram'}*\n\n",
        text
    )
    fixes += mermaid_count
    
    # --- Fix bullet markers: * → - ---
    text = re.sub(r'^(\s*)\*\s+', r'\1- ', text, flags=re.MULTILINE)
    
    # --- Fix broken bold markers ---
    text = re.sub(r'\*\*\s+([^*]+?)\s+\*\*', r'**\1**', text)
    text = re.sub(r'\*\*([^*]+?)\s+\*\*', r'**\1**', text)
    text = re.sub(r'\*\*\s+([^*]+?)\*\*', r'**\1**', text)
    text = re.sub(r'\*\*\s*\*\*', '', text)
    text = re.sub(r'^\*\*\s*$', '', text, flags=re.MULTILINE)
    
    # --- Remove empty code blocks ---
    text = re.sub(r'```\w*\s*\n\s*```', '', text)
    
    # --- Fix unclosed code fences ---
    fence_count = len(re.findall(r'^```', text, flags=re.MULTILINE))
    if fence_count % 2 != 0:
        text += "\n```\n"
    
    # --- Resolve leftover [ORIGINAL_ASSET] tags ---
    orig_count = len(re.findall(r'\[ORIGINAL_ASSET:', text))
    text = re.sub(r'\[ORIGINAL_ASSET:\s*[^\]]+\]', '', text)
    
    # --- Resolve leftover [NEW_DIAGRAM] tags → styled boxes ---
    diag_count = len(re.findall(r'\[NEW_DIAGRAM:', text))
    text = re.sub(
        r'\[NEW_DIAGRAM:\s*([^\]]+)\]',
        r'\n\n> 📊 *Diagram: \1*\n\n',
        text
    )
    
    # --- Remove broken local image refs ---
    img_count = len(re.findall(r'!\[Original Figure\]\(/assets/', text))
    text = re.sub(r'!\[Original Figure\]\([^)]*\)', '', text)
    
    fixes += orig_count + diag_count + img_count
    print(f"[Sanitizer] Pass 3: Fixed content — {mermaid_count} mermaid, "
          f"{orig_count} assets, {diag_count} diagrams, {img_count} images")
    return text


# ══════════════════════════════════════════════
# PASS 4: Sanitize Backslashes (code blocks only)
# ══════════════════════════════════════════════
def sanitize_backslashes(text: str) -> str:
    """
    Escape \\n/\\r/\\t sequences ONLY inside code blocks.
    Math blocks are already protected by Pass 2 placeholders.
    """
    fixed_count = 0
    
    # Split by code fences and process only code blocks
    parts = re.split(r'(```[^\n]*\n.*?```)', text, flags=re.DOTALL)
    
    escape_map = {
        '\\n': '\\\\n',
        '\\r': '\\\\r',
        '\\t': '\\\\t',
        '\\0': '\\\\0',
        '\\a': '\\\\a',
        '\\b': '\\\\b',
        '\\f': '\\\\f',
    }
    
    result = []
    for i, part in enumerate(parts):
        if part.startswith('```'):
            # This is a code block — escape backslash sequences
            for old, new in escape_map.items():
                count = part.count(old)
                if count > 0:
                    part = part.replace(old, new)
                    fixed_count += count
        result.append(part)
    
    text = ''.join(result)
    print(f"[Sanitizer] Pass 4: Escaped {fixed_count} backslash sequences in code blocks")
    return text


# ══════════════════════════════════════════════
# PASS 5: Strip AI Chatter
# ══════════════════════════════════════════════
def strip_ai_chatter(text: str) -> str:
    """
    Remove AI meta-talk and clean up excessive whitespace.
    """
    patterns = [
        r'(?i)^(here is|here\'s) (the|an|your) (expanded|revised|updated|rewritten).*?\n',
        r'(?i)^(based on|following|as per) (the|your) (provided|original|expansion).*?\n',
        r'(?i)^(i have|i\'ve|let me) (expanded|revised|rewritten|provided).*?\n',
        r'(?i)^(below is|the following is).*?(expanded|revised|chapter).*?\n',
        r'(?i)^(sure|of course|certainly|absolutely)[,!.].*?\n',
    ]
    removed = 0
    print(f"[Sanitizer] Pass 5: Stripping AI chatter from {len(text):,} chars...")
    for i, pat in enumerate(patterns):
        matches = re.findall(pat, text, flags=re.MULTILINE)
        count = len(matches)
        if count > 0:
            print(f"  [Chatter] Pattern {i+1} found {count} matches")
            removed += count
            text = re.sub(pat, '', text, flags=re.MULTILINE)

    # Collapse 3+ blank lines → 2
    print("  [Chatter] Collapsing blank lines...")
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    # Remove chunk markers
    print("  [Chatter] Removing chunk markers...")
    text = text.replace("--- CHUNK END ---", "")
    text = text.replace("---\n\n---", "---")

    print(f"[Sanitizer] Pass 5: Stripped {removed} AI chatter lines")
    return text


# ══════════════════════════════════════════════
# PASS 6: Unicode / Encoding Fixes
# ══════════════════════════════════════════════
def fix_unicode(text: str) -> str:
    """
    Remove or replace characters that XeLaTeX cannot render.
    """
    replacements = {
        '\u2018': "'",   # left single quote
        '\u2019': "'",   # right single quote
        '\u201c': '"',   # left double quote
        '\u201d': '"',   # right double quote
        '\u2013': '--',  # en-dash
        '\u2014': '---', # em-dash
        '\u2026': '...', # ellipsis
        '\u00a0': ' ',   # non-breaking space
        '\u200b': '',    # zero-width space
        '\u200c': '',    # zero-width non-joiner
        '\u200d': '',    # zero-width joiner
        '\ufeff': '',    # BOM
        '\u00ad': '',    # soft hyphen
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove control characters (except newline, tab)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)

    # Encode/decode to clean unmappable chars
    cleaned = text.encode('utf-8', errors='replace').decode('utf-8', errors='replace')

    removed = len(text) - len(cleaned)
    print(f"[Sanitizer] Pass 6: Cleaned Unicode ({removed} chars removed)")
    return cleaned


# ══════════════════════════════════════════════
# PASS 7: Add Structure (page breaks, spacing)
# ══════════════════════════════════════════════
def add_structure(text: str) -> str:
    """
    Insert raw LaTeX page breaks before chapters and restore math.
    """
    # Add page break before H1 chapters using raw LaTeX command
    # Pandoc usually passes raw LaTeX commands through if they're on their own line
    text = re.sub(
        r'\n(# [^\n]+)',
        r'\n\n\\clearpage\n\n\1',
        text
    )
    
    # Fix heading jumps: #### without ### → demote to ###
    text = re.sub(r'^####\s', '### ', text, flags=re.MULTILINE)
    
    # Restore math blocks from Pass 2 placeholders
    text = restore_math(text)
    
    print("[Sanitizer] Pass 7: Added page breaks and restored math")
    return text


# ══════════════════════════════════════════════
# MASTER SANITIZER
# ══════════════════════════════════════════════
def sanitize(text: str) -> str:
    """Run all 7 sanitization passes in order."""
    print("\n══════════════════════════════════════════")
    print("  SANITIZATION ENGINE — 7-Pass Math-Aware Clean")
    print("══════════════════════════════════════════\n")

    text = strip_wrappers(text)          # Pass 0 — remove artifacts
    text = normalize_headings(text)      # Pass 1
    text = protect_math(text)            # Pass 2 — shields math
    text = fix_code_and_content(text)    # Pass 3
    text = sanitize_backslashes(text)    # Pass 4
    text = strip_ai_chatter(text)        # Pass 5
    text = fix_unicode(text)             # Pass 6
    text = add_structure(text)           # Pass 7 — restores math

    print(f"\n[Sanitizer] ✅ All 7 passes complete ({len(text):,} chars)")
    return text


# ══════════════════════════════════════════════
# PREPARE & PUBLISH
# ══════════════════════════════════════════════
FRONTMATTER = """\
---
title: "Hydraulics and Pneumatics: A First-Principles Approach"
author: "BookForge Synthetic Engine"
date: "2026"
---

"""


def prepare_manuscript() -> str:
    """
    Sanitize the resolved manuscript, add frontmatter,
    and save ``ready_for_press.md``.
    """
    if not RESOLVED_PATH.exists():
        raise FileNotFoundError(
            f"Resolved manuscript not found: {RESOLVED_PATH}\n"
            "Run the Art Department (Phase 3) first."
        )

    print("\n══════════════════════════════════════════")
    print("  PUBLISHER — Preparing manuscript…")
    print("══════════════════════════════════════════\n")

    text = RESOLVED_PATH.read_text(encoding="utf-8")

    # Run the 7-pass sanitizer
    text = sanitize(text)

    # Add professional frontmatter
    text = FRONTMATTER + text

    # Save
    PRESS_READY_PATH.write_text(text, encoding="utf-8")
    print(f"\n[Publisher] Saved press-ready manuscript ({len(text):,} chars) → {PRESS_READY_PATH}")

    return text


def publish_pdf() -> None:
    """
    Compile the press-ready Markdown into a paginated PDF
    using Pandoc with XeLaTeX engine and suhbook template.
    """
    if not PRESS_READY_PATH.exists():
        raise FileNotFoundError(
            f"Press-ready manuscript not found: {PRESS_READY_PATH}\n"
            "Run prepare_manuscript() first."
        )

    template_path = Path("templates/bookforge.latex")

    # Ensure suhbook.cls is accessible — copy to output dir where XeLaTeX runs
    cls_source = Path("templates/suhbook.cls")
    if cls_source.exists():
        # Copy cls to current dir so XeLaTeX can find it
        cls_dest = Path("suhbook.cls")
        if not cls_dest.exists():
            cls_dest.write_text(cls_source.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"[Publisher] Copied suhbook.cls → project root")

    cmd = [
        "pandoc",
        str(PRESS_READY_PATH),
        "-o", str(FINAL_PDF_PATH),
        "--no-highlight",
        "--pdf-engine=xelatex",
        "--template", str(template_path),
        "--top-level-division=chapter",
        "--toc",
        "--toc-depth=2",
    ]

    print(f"\n[Publisher] Running: {' '.join(cmd)}")

    input_env = os.environ.copy()
    current_dir = Path.cwd().as_posix()
    # Add current directory to TEXINPUTS (recursive search //)
    if "TEXINPUTS" in input_env:
        input_env["TEXINPUTS"] = f"{current_dir}//;{input_env['TEXINPUTS']}"
    else:
        input_env["TEXINPUTS"] = f"{current_dir}//;"

    try:
        result = subprocess.run(
            cmd, capture_output=True, check=True,
            env=input_env,
            encoding='utf-8', errors='replace'
        )
        size_kb = FINAL_PDF_PATH.stat().st_size / 1024
        print(f"\n[Publisher] 🎉 SUCCESS! → {FINAL_PDF_PATH} ({size_kb:.1f} KB)")

    except FileNotFoundError:
        print(
            "\n❌ Pandoc or XeLaTeX not found!\n"
            "Install them with:\n"
            "  winget install --id JohnMacFarlane.Pandoc\n"
            "  winget install --id MiKTeX.MiKTeX\n"
            "Then restart your terminal and run again."
        )
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Pandoc/XeLaTeX compilation failed:\n{e.stderr}")



# ══════════════════════════════════════════════
# INDIVIDUAL CHAPTER PUBLISHING
# ══════════════════════════════════════════════
def publish_chapter_pdf(chapter_text: str, chapter_num: int) -> None:
    """
    Sanitize and publish a single chapter as a PDF.
    """
    chapter_dir = OUTPUT_DIR / "chapters"
    chapter_dir.mkdir(parents=True, exist_ok=True)
    
    chapter_md_path = chapter_dir / f"chapter_{chapter_num}.md"
    chapter_pdf_path = chapter_dir / f"chapter_{chapter_num}.pdf"
    
    print(f"\n[Publisher] Preparing Chapter {chapter_num} PDF...")
    
    # 1. Sanitize
    # We use a slightly lighter touch or the full suite? Let's use full suite for consistency.
    clean_text = sanitize(chapter_text)
    
    # 2. Add minimal frontmatter for this chapter
    frontmatter = (
        "---\n"
        f"title: \"Chapter {chapter_num}\"\n"
        "author: \"BookForge Draft\"\n"
        "---\n\n"
    )
    full_content = frontmatter + clean_text
    
    chapter_md_path.write_text(full_content, encoding="utf-8")
    
    # 3. Publish via Pandoc
    template_path = Path("templates/bookforge.latex")
    # Ensure template exists or fallback
    if not template_path.exists():
         # Fallback to default styling if template is missing in this context
         cmd = [
            "pandoc",
            str(chapter_md_path),
            "-o", str(chapter_pdf_path),
            "--pdf-engine=xelatex",
            "--toc"
        ]
    else:
        cmd = [
            "pandoc",
            str(chapter_md_path),
            "-o", str(chapter_pdf_path),
            "--pdf-engine=xelatex",
            "--template", str(template_path),
            "--top-level-division=chapter"
        ]

    input_env = os.environ.copy()
    current_dir = Path.cwd().as_posix()
    # Add current directory to TEXINPUTS (recursive search //)
    if "TEXINPUTS" in input_env:
        input_env["TEXINPUTS"] = f"{current_dir}//;{input_env['TEXINPUTS']}"
    else:
        input_env["TEXINPUTS"] = f"{current_dir}//;"

    try:
        subprocess.run(
            cmd, capture_output=True, check=True,
            env=input_env,
            encoding='utf-8', errors='replace'
        )
        print(f"   ✅ Chapter {chapter_num} PDF generated → {chapter_pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"   ⚠️ Failed to generate Chapter {chapter_num} PDF: {e.stderr[:200]}...")
    except Exception as e:
        print(f"   ⚠️ Failed to generate Chapter {chapter_num} PDF: {e}")


# ──────────────────────────────────────────────
# CLI ENTRY POINT
# ──────────────────────────────────────────────
if __name__ == "__main__":
    prepare_manuscript()
    publish_pdf()
