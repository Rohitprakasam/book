"""
BookForge 5.0 — Master Orchestrator
=====================================
Chains all four phases into a single end-to-end pipeline:

    Phase 1   Deconstruct   PDF → tagged_manuscript.txt
    Phase 1b  Style Extract PDF → style_config.json
    Phase 1c  Visual Triage Classify images (keep/discard/transcribe)
    Phase 2   Expand Swarm  chunks → analyst → drafter → critic loop
    Phase 3   Art Dept      [ORIGINAL_ASSET] & [NEW_DIAGRAM] → resolved Markdown
    Phase 4   Typesetting   Structured JSON → LaTeX → PDF

Usage
-----
    python main.py "path/to/input.pdf"                  # Full pipeline
    python main.py "path/to/input.pdf" --style "s.pdf"  # With style reference
    python main.py --resume                             # Resume from last checkpoint
    python main.py --phase 4                            # Re-run Phase 4 only
"""

from __future__ import annotations

import os
import sys
import uuid
import time
import argparse
import re
import json
import subprocess
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Fix Windows console encoding (cp1252 can't handle Unicode box chars)
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr.encoding != "utf-8":
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ──────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "data" / "output"
EXPANDED_PATH = OUTPUT_DIR / "expanded_draft.md"
RESOLVED_PATH = OUTPUT_DIR / "resolved_manuscript.md"
STATE_FILE = OUTPUT_DIR / "pipeline_state.json"
CHUNK_SEPARATOR = "\n\n--- CHUNK END ---\n\n"
THROTTLE_SECONDS = 5


# ──────────────────────────────────────────────
# CHECKPOINT SYSTEM (Fault Tolerance)
# ──────────────────────────────────────────────
def save_state(phase: int, data: dict = None) -> None:
    """Save checkpoint after each phase completes."""
    state = {
        "completed_phase": phase,
        "timestamp": time.time(),
        "timestamp_human": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    if data:
        state.update(data)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")
    print(f"   💾 Checkpoint saved: Phase {phase} complete.")


def load_state() -> dict:
    """Load last checkpoint."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {"completed_phase": 0}
    return {"completed_phase": 0}


# ──────────────────────────────────────────────
# PIPELINE
# ──────────────────────────────────────────────
def main(
    pdf_path: str = None,
    style_path: str = None,
    start_phase: int = 1,
) -> None:
    """Run the full BookForge 5.0 pipeline."""
    start_time = time.time()
    total = 0
    style_config = {}

    print()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║          📖  BOOKFORGE 5.0 — UNIFIED ENGINE           ║")
    print("║       Document Deconstruction & Reassembly Engine       ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()

    print()

    if start_phase == 1:
        print("   🧹 Starting fresh run. Purging previous book data to prevent cross-contamination...")
        from clear_data import clear_directory
        clear_directory(OUTPUT_DIR)
        clear_directory(BASE_DIR / "data" / "chroma_db")
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        print()
    elif start_phase > 1:
        print(f"   ⏩  Skipping to Phase {start_phase} (checkpoint/flag)")
        print()

    manuscript_file = OUTPUT_DIR / "tagged_manuscript.txt"

    # ──────────────────────────────────────────
    # PHASE 1: THE DECONSTRUCTOR
    # ──────────────────────────────────────────
    if start_phase <= 1:
        print("━" * 58)
        print("🔬  PHASE 1 — THE DECONSTRUCTOR")
        print("━" * 58)

        if not pdf_path:
            print("❌ No PDF path provided. Cannot run Phase 1.")
            return

        print(f"   Input PDF: {pdf_path}")

        # ── Phase 1b: Style Extraction ──
        if style_path:
            print(f"   Style Ref: {style_path}")
            from src.style_manager import extract_style
            style_config = extract_style(style_path)
        else:
            print("   Style Ref: None (using defaults)")
        print()

        from src.deconstructor import deconstruct

        deconstruct(pdf_path)

        # ── Phase 1c: Visual Triage ──
        print("\n   🔍 Running Visual Triage...")
        try:
            from src.triage import process_images, clean_manuscript

            extracted_dir = str(OUTPUT_DIR / "assets" / "extracted_images")
            discarded = process_images(cache_dir=extracted_dir)
            clean_manuscript(str(manuscript_file), discarded)
        except Exception as e:
            print(f"   ⚠️  Triage skipped: {e}")

        save_state(1, {"style_config": style_config})
        print(f"\n   ✅ Phase 1 complete → {manuscript_file}\n")

    # ──────────────────────────────────────────
    # PHASE 2: THE EXPANSION SWARM
    # ──────────────────────────────────────────
    if start_phase <= 2:
        print("━" * 58)
        print("🐝  PHASE 2 — THE EXPANSION SWARM")
        print("━" * 58)

        # Recover style_config from checkpoint if resuming
        if start_phase > 1 and not style_config:
            saved = load_state()
            style_config = saved.get("style_config", {})

        from src.chunker import chunk_manuscript
        from src.graph import build_graph
        from src.agents import _get_model, _test_llm_connection

        if not manuscript_file.exists():
            print("❌ Manuscript not found. Cannot proceed to Phase 2.")
            return

        # Test LLM connectivity before processing chunks
        model = _get_model()
        api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        
        print(f"   🔍 Testing LLM connection...")
        print(f"      Model: {model}")
        print(f"      API Key: {'SET' if api_key else 'NOT SET'}")
        
        if model.startswith("gemini/") and not api_key:
            print("   ❌ ERROR: Gemini model requires GOOGLE_API_KEY or GEMINI_API_KEY")
            print("   💡 Set GOOGLE_API_KEY in your .env file")
            print("   ⚠️  Aborting Phase 2 - cannot proceed without API key")
            return
        
        if not _test_llm_connection():
            print("   ⚠️  LLM connection test failed. Chunks may fail.")
            print("   💡 Check your DEFAULT_MODEL env var and API keys.")
            print("   ⚠️  Continuing anyway, but expect failures...")

        chunks = chunk_manuscript(str(manuscript_file))
        graph = build_graph()
        total = len(chunks)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # ── Resume Detection ──
        expanded_draft = ""
        start_chunk = 0

        if EXPANDED_PATH.exists():
            expanded_draft = EXPANDED_PATH.read_text(encoding="utf-8")
            separator_count = expanded_draft.count("--- CHUNK END ---")
            # Validate: only resume if separator count is within bounds
            if 0 < separator_count <= total:
                start_chunk = separator_count
                print(f"   🔄 Found existing progress! Resuming from chunk {start_chunk + 1}…")
            elif separator_count > total:
                print(f"   ⚠️  Checkpoint mismatch ({separator_count} separators vs {total} chunks). Starting fresh.")
                expanded_draft = ""
                start_chunk = 0

        if start_chunk < total:
            for i, chunk in enumerate(chunks[start_chunk:], start=start_chunk):
                print(f"\n   ── Chunk {i + 1}/{total} ({len(chunk):,} chars) ──")

                # Validate chunk before processing
                if not chunk or len(chunk.strip()) == 0:
                    print(f"   ⚠️  Chunk {i + 1} is empty, skipping...")
                    expanded = chunk
                else:
                    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
                    
                    # Ensure initial state has all required keys
                    initial_state = {
                        "current_chunk": chunk,
                        "revision_count": 0,
                        "analysis": "",
                        "expanded_chunk": "",
                        "feedback": "",
                    }

                    try:
                        result = graph.invoke(initial_state, config)
                        
                        # Safely extract expanded chunk
                        expanded = result.get("expanded_chunk") or result.get("current_chunk") or chunk
                        
                        # Validate result
                        if not expanded or len(expanded.strip()) == 0:
                            print(f"   ⚠️  Chunk {i + 1} produced empty expansion, using original")
                            expanded = chunk
                        elif expanded == chunk:
                            print(f"   ⚠️  Chunk {i + 1} returned unchanged (may indicate failure)")
                        else:
                            print(f"   ✅ Chunk {i + 1} expanded → {len(expanded):,} chars")

                    except KeyboardInterrupt:
                        print(f"\n   ⚠️  Interrupted by user at chunk {i + 1}")
                        raise
                    except Exception as e:
                        import traceback
                        error_type = type(e).__name__
                        error_msg = str(e)
                        print(f"   ⚠️  Chunk {i + 1} failed ({error_type}): {error_msg}")
                        # Print full traceback for debugging
                        tb_lines = traceback.format_exc().splitlines()
                        for line in tb_lines[:10]:  # Show more lines
                            if line.strip() and not line.startswith("File"):
                                print(f"      {line}")
                        expanded = chunk

                expanded_draft += expanded + CHUNK_SEPARATOR
                EXPANDED_PATH.write_text(expanded_draft, encoding="utf-8")
                print(f"   💾 Checkpoint saved to disk.")

                if i < total - 1:
                    print(f"   🛑 Throttling for {THROTTLE_SECONDS}s…")
                    time.sleep(THROTTLE_SECONDS)

        else:
            print(f"\n   ✅ All {total} chunks already processed.")
            print("   ⏭️  Skipping Expansion.")

        full_expanded = expanded_draft.replace("--- CHUNK END ---", "---").strip()

        save_state(2, {"total_chunks": total, "style_config": style_config})
        print(f"\n   ✅ Phase 2 complete → {EXPANDED_PATH}")
        print(f"   📊 {total} chunks expanded ({len(full_expanded):,} total chars)\n")

    # ──────────────────────────────────────────
    # PHASE 3: THE ART DEPARTMENT
    # ──────────────────────────────────────────
    if start_phase <= 3:
        print("━" * 58)
        print("🎨  PHASE 3 — THE ART DEPARTMENT")
        print("━" * 58)

        # Recover data if resuming
        if start_phase > 2:
            saved = load_state()
            style_config = saved.get("style_config", {})
            total = saved.get("total_chunks", 0)

        # Read expanded draft
        if EXPANDED_PATH.exists():
            full_expanded = EXPANDED_PATH.read_text(encoding="utf-8")
            full_expanded = full_expanded.replace("--- CHUNK END ---", "---").strip()
        else:
            print("❌ Expanded draft not found. Cannot proceed to Phase 3.")
            return

        from src.resolver import process_art_department

        # Pass the REAL style_config (Fix #1)
        process_art_department(full_expanded, style_config)

        save_state(3, {"total_chunks": total, "style_config": style_config})
        print(f"\n   ✅ Phase 3 complete → {RESOLVED_PATH}\n")

    # ──────────────────────────────────────────
    # PHASE 4: THE TYPESETTING ENGINE
    # ──────────────────────────────────────────
    if start_phase <= 4:
      print("━" * 58)
      print("🖨️  PHASE 4 — THE TYPESETTING ENGINE")
      print("━" * 58)

    # Recover metadata if jumping to Phase 4
    if start_phase > 3:
        saved = load_state()
        total = saved.get("total_chunks", 0)

    from src.structurer import structurer_node
    from src.renderer_latex import render_page_latex

    # 1. Read the resolved manuscript (or expanded if resolved missing)
    manuscript_path = RESOLVED_PATH if RESOLVED_PATH.exists() else EXPANDED_PATH
    if not manuscript_path.exists():
        print("❌ No manuscript found to render.")
        return

    print(f"📖 Reading manuscript from {manuscript_path}...")
    text = manuscript_path.read_text(encoding="utf-8")

    # 2. Split using the same chunker as Phase 2 for consistency (Fix #13)
    from src.chunker import chunk_manuscript as _chunker
    # Write temp file for chunker since it reads files
    temp_chunk_file = OUTPUT_DIR / "_phase4_temp.txt"
    temp_chunk_file.write_text(text, encoding="utf-8")
    try:
        chunks = _chunker(str(temp_chunk_file))
    finally:
        temp_chunk_file.unlink(missing_ok=True)

    full_structure = {"title": "Generated Book", "sections": []}

    # 3. Structure — with fault tolerance (skip bad sections)
    print(f"🤖 AI Structuring ({len(chunks)} sections)...")
    print(f"   Using model: {os.getenv('DEFAULT_MODEL', 'groq/llama3-8b-8192')}")
    
    # Checkpoint support: resume from partial JSON if it exists
    json_path = OUTPUT_DIR / "book_structure.json"
    start_section = 0
    if json_path.exists():
        try:
            existing = json.loads(json_path.read_text(encoding="utf-8"))
            existing_sections = existing.get("sections", [])
            if existing_sections:
                start_section = len(existing_sections)
                full_structure["sections"] = existing_sections
                print(f"   🔄 Found existing structure with {start_section} sections, resuming from section {start_section + 1}...")
        except Exception as e:
            print(f"   ⚠️ Could not load existing structure: {e}, starting fresh")
    
    failed_sections = 0
    rate_limit_delays = 0
    
    for i, chunk in enumerate(chunks[start_section:], start=start_section):
        # Show progress every 10 sections
        if (i + 1) % 10 == 0 or i == 0:
            print(f"   Processing section {i + 1}/{len(chunks)}...")
        
        try:
            data = structurer_node(chunk)
            
            # Check for explicit error from structurer
            if isinstance(data, dict) and "error" in data:
                error_msg = data["error"]
                
                # Handle rate limits specially - add delay before next request
                if "rate limit" in error_msg.lower() or "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                    rate_limit_delays += 1
                    if rate_limit_delays <= 3:  # Only delay first few rate limit errors
                        delay = 30 * rate_limit_delays
                        print(f"   ⏳ Rate limit detected, waiting {delay}s before continuing...")
                        time.sleep(delay)
                    else:
                        print(f"   ⚠️ Too many rate limits, skipping delay for remaining sections")
                
                # For rate limits, still try to continue after delay
                if "rate limit" not in error_msg.lower() and "429" not in error_msg:
                    raise Exception(f"Structurer Error: {error_msg}")

            # Validate data structure
            if isinstance(data, list):
                full_structure["sections"].append({"type": "chapter", "sections": data})
            elif isinstance(data, dict):
                if "error" not in data:  # Only add if not an error dict
                    full_structure["sections"].append(data)
                else:
                    raise Exception(f"Structurer returned error: {data['error']}")
            else:
                raise Exception(f"Unexpected structurer return type: {type(data)}")
            
            # Throttle between requests to avoid rate limits
            # Use shorter delay for Gemini (more lenient) vs other providers
            throttle_delay = 0.5 if os.getenv("DEFAULT_MODEL", "").startswith("gemini/") else 1.0
            time.sleep(throttle_delay)
            
        except Exception as e:
            failed_sections += 1
            error_msg = str(e)
            
            # Show error details for first few failures to help diagnose
            if failed_sections <= 5:
                print(f"   ⚠️ Section {i + 1} failed: {error_msg[:100]}")
            elif failed_sections == 6:
                print(f"   ⚠️ (Suppressing further error details, {failed_sections} failures so far...)")
            
            # Fallback: wrap raw text as a simple paragraph
            fallback_text = chunk[:2000] if len(chunk) > 2000 else chunk
            full_structure["sections"].append({
                "type": "chapter",
                "sections": [{"type": "paragraph", "text": fallback_text}]
            })
            
            # Add delay after failures to avoid hammering the API
            if failed_sections % 10 == 0:
                print(f"   ⏸️  Pausing after {failed_sections} failures...")
                time.sleep(5)
        
        # Save checkpoint every 10 sections to allow resuming
        if (i + 1) % 10 == 0:
            json_path.write_text(json.dumps(full_structure, indent=2), encoding="utf-8")
            print(f"   💾 Checkpoint saved ({i + 1}/{len(chunks)} sections processed)")

    if failed_sections:
        print(f"\n   ⚠️  {failed_sections}/{len(chunks)} sections failed and used fallback text")
        if failed_sections > len(chunks) * 0.5:
            print(f"   ⚠️  WARNING: >50% failure rate! Check API key, rate limits, or model availability")
    else:
        print(f"\n   ✅ All {len(chunks)} sections structured successfully")

    # 3.5 Robust Chapter Demotion
    # Since Phase 1 chunks randomly, Phase 2 treats every chunk as a new 'Chapter 1'
    # Demote fake chapters to sections so they nest properly under the real ones
    for chapter in full_structure.get("sections", []):
        if chapter.get("type") == "chapter":
            for sec in chapter.get("sections", []):
                if sec.get("type") == "heading" and sec.get("level") == 1:
                    heading_text = sec.get("text", "").lower()
                    if not any(k in heading_text for k in ["chapter ", "unit ", "module ", "part "]):
                        sec["level"] = 2

    # 3.6 Resolve Image Tags & Generate Diagrams (PHASE 3 Integration)
    from src.resolver import resolve_art_tags, resolve_original_assets
    print("🎨 Resolving and Generating AI Diagrams from JSON Structure...")
    def process_node(node):
        if isinstance(node, dict):
            if "text" in node and isinstance(node["text"], str):
                original = node["text"]
                # 1. Resolve ORIGINAL PDF Extractions
                if "ORIGINAL_ASSET" in original:
                    new_text = resolve_original_assets(original)
                    if new_text != original:
                        original = new_text
                        node["text"] = new_text
                # 2. Resolve AI Generated Diagrams
                if "NEW_DIAGRAM" in original:
                    new_text = resolve_art_tags(original)
                    if new_text != original:
                        node["text"] = new_text
            for v in node.values():
                process_node(v)
        elif isinstance(node, list):
            for item in node:
                process_node(item)

    process_node(full_structure)

    # 4. Save JSON structure (json_path already declared above at checkpoint section)
    json_path.write_text(json.dumps(full_structure, indent=2), encoding="utf-8")
    print(f"📄 JSON saved: {json_path}")

    # 5. Render LaTeX
    latex_parts = []
    for chapter in full_structure["sections"]:
        try:
            latex_parts.append(render_page_latex(chapter))
        except Exception as e:
            print(f"   ⚠️ LaTeX render error: {e} — skipping chapter")

    # 6. Build LaTeX document
    tex_out = OUTPUT_DIR / "BookForge.tex"
    template_path = BASE_DIR / "templates" / "bookforge.latex"
    if not template_path.exists():
        print(f"❌ LaTeX Template not found at {template_path}")
        return

    template_content = template_path.read_text(encoding="utf-8")

    # Clean Pandoc conditionals from template (Fix #14)
    # Remove $if(...)$...$endif$ blocks
    template_content = re.sub(
        r'\$if\(.*?\)\$.*?\$endif\$',
        '',
        template_content,
        flags=re.DOTALL
    )
    # Remove $for(...)$...$endfor$ blocks
    template_content = re.sub(
        r'\$for\(.*?\)\$.*?\$endfor\$',
        '',
        template_content,
        flags=re.DOTALL
    )

    latex_body = "\n".join(latex_parts)

    # Auto-balance braces to prevent Emergency Stops
    open_braces = latex_body.count('{') - latex_body.count(r'\{')
    close_braces = latex_body.count('}') - latex_body.count(r'\}')
    net_braces = open_braces - close_braces
    if net_braces > 0:
        print(f"   ⚠️ Auto-balancing: inserting {net_braces} missing closing braces.")
        latex_body += "}\n" * net_braces

    # Clean stray \n or \t incorrectly output by the LLM as text
    def fix_n_command(match):
        cmd = match.group(1)
        valid = ['nu', 'nabla', 'nearrow', 'neg', 'newline', 'newpage', 'ni', 'nocite', 'noindent', 'nolimits', 'nonumber', 'nopagebreak', 'normalfont', 'normalsize', 'not', 'notin']
        return '\\' + cmd if cmd in valid else '\n' + cmd[1:]
    
    def fix_t_command(match):
        cmd = match.group(1)
        valid = ['tau', 'text', 'textbf', 'textit', 'texttt', 'theta', 'times', 'tilde', 'tan', 'top', 'triangle', 'to', 'today', 'tag', 'textwidth', 'textheight', 'tfrac', 'thickapprox', 'thicksim', 'textasciicircum', 'textasciitilde']
        return '\\' + cmd if cmd in valid else ' ' + cmd[1:]

    latex_body = re.sub(r'\\(n[a-zA-Z]*)', fix_n_command, latex_body)
    latex_body = re.sub(r'\\(t[a-zA-Z]*)', fix_t_command, latex_body)

    full_latex = template_content.replace("$body$", latex_body)
    full_latex = full_latex.replace("$title$", "BookForge Book")
    full_latex = full_latex.replace("$author$", "BookForge Engine")
    full_latex = full_latex.replace("$date$", "\\today")
    # Clean any remaining $variable$ Pandoc tokens
    full_latex = re.sub(r'\$[a-zA-Z_-]+\$', '', full_latex)

    tex_out.write_text(full_latex, encoding="utf-8")
    print(f"✅ LaTeX Generated: {tex_out}")

    # 7. Compile PDF (Fix #20: use separate variable name)
    print("🚀 Compiling PDF with pdflatex...")
    output_pdf = OUTPUT_DIR / "BookForge.pdf"
    try:
        # Run twice for TOC/refs
        for pass_num in (1, 2):
            print(f"   Pass {pass_num}/2...")
            result = subprocess.run(
                ["pdflatex", "-interaction=nonstopmode",
                 "-output-directory", str(OUTPUT_DIR), str(tex_out)],
                capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120
            )
            if result.returncode != 0:
                # Log errors but DON'T crash — nonstopmode continues past errors
                print(f"   ⚠️ pdflatex pass {pass_num} had warnings/errors (see .log)")

        if output_pdf.exists() and output_pdf.stat().st_size > 0:
            size_mb = output_pdf.stat().st_size / (1024 * 1024)
            print(f"\n✅ PDF Compiled: {output_pdf} ({size_mb:.2f} MB)")
        else:
            print("\n❌ PDF file was not created. Check BookForge.log for details.")
            log_file = tex_out.with_suffix('.log')
            if log_file.exists():
                # Show last 20 lines of log
                log_lines = log_file.read_text(encoding="utf-8", errors="ignore").splitlines()
                print("   Last 20 lines of log:")
                for line in log_lines[-20:]:
                    print(f"   | {line}")

    except subprocess.TimeoutExpired:
        print("❌ pdflatex timed out after 120 seconds.")
    except FileNotFoundError:
        print("❌ pdflatex not found. Please install MiKTeX or TeX Live.")

    save_state(4, {"total_chunks": total})

    # ──────────────────────────────────────────
    # SUMMARY
    # ──────────────────────────────────────────
    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)

    print()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║              🎉  BOOKFORGE COMPLETE  🎉                 ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"║  ⏱️  Total time: {minutes}m {seconds}s")
    print(f"║  📄  Chunks processed: {total}")
    print(f"║  📝  Expanded draft: {EXPANDED_PATH}")
    print(f"║  📖  Final PDF: {output_pdf}")
    print("╚══════════════════════════════════════════════════════════╝")
    print()


# ──────────────────────────────────────────────
# CLI ENTRY POINT
# ──────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BookForge 5.0 Pipeline")
    parser.add_argument("pdf_input", help="Path to input PDF", nargs='?')
    parser.add_argument("--style", help="Path to Style Reference PDF", default=None)
    parser.add_argument(
        "--resume", action="store_true",
        help="Resume from the last completed phase checkpoint"
    )
    parser.add_argument(
        "--phase", type=int, choices=[1, 2, 3, 4], default=None,
        help="Jump directly to a specific phase (e.g., --phase 4)"
    )

    args = parser.parse_args()

    # Determine start phase
    start_phase = 1
    if args.resume:
        state = load_state()
        start_phase = state.get("completed_phase", 0) + 1
        if start_phase > 4:
            print("✅ Pipeline already complete. Nothing to resume.")
            sys.exit(0)
        print(f"🔄 Resuming from Phase {start_phase}...")
    elif args.phase:
        start_phase = args.phase

    # Validate: need PDF for Phase 1
    if start_phase <= 1:
        if not args.pdf_input or not Path(args.pdf_input).exists():
            print(f"❌ File not found: {args.pdf_input}")
            sys.exit(1)

    main(args.pdf_input, args.style, start_phase=start_phase)
