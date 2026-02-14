"""
BookForge 4.0 — Master Orchestrator
=====================================
Chains all four phases into a single end-to-end pipeline:

    Phase 1  Deconstruct   PDF → tagged_manuscript.txt
    Phase 1b Style Extract PDF → style_config.json
    Phase 2  Expand Swarm  chunks → analyst → drafter → critic loop
    Phase 3  Art Dept      [ORIGINAL_ASSET] & [NEW_DIAGRAM] → resolved Markdown
    Phase 4  Typesetting   Pandoc + Typst → paginated PDF

Usage
-----
    python main.py "path/to/input.pdf" --style "path/to/style.pdf"
"""

from __future__ import annotations

import os
import sys
import uuid
import time
import argparse
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# ──────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────
OUTPUT_DIR = Path("data/output")
EXPANDED_PATH = OUTPUT_DIR / "expanded_draft.md"
CHUNK_SEPARATOR = "\n\n--- CHUNK END ---\n\n"
THROTTLE_SECONDS = 5  # Reduced to 5s as per user request


def main(pdf_path: str, style_path: str = None) -> None:
    """Run the full BookForge 4.0 pipeline."""
    start_time = time.time()

    print()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║          📖  BOOKFORGE 4.0 — MASTER PIPELINE  📖        ║")
    print("║       Document Deconstruction & Reassembly Engine       ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()

    # ──────────────────────────────────────────
    # PHASE 1: THE DECONSTRUCTOR
    # ──────────────────────────────────────────
    print("━" * 58)
    print("🔬  PHASE 1 — THE DECONSTRUCTOR")
    print("━" * 58)
    print(f"   Input PDF: {pdf_path}")
    
    # ── Phase 1b: Style Extraction ──
    style_config = {}
    if style_path:
        print(f"   Style Ref: {style_path}")
        from src.style_manager import extract_style
        style_config = extract_style(style_path)
    else:
        print("   Style Ref: None (using defaults)")
    print()

    from src.deconstructor import deconstruct, MANUSCRIPT_PATH

    deconstruct(pdf_path)

    print(f"\n   ✅ Phase 1 complete → {MANUSCRIPT_PATH}\n")

    # ──────────────────────────────────────────
    # PHASE 2: THE EXPANSION SWARM (with Throttle & Resume)
    # ──────────────────────────────────────────
    print("━" * 58)
    print("🐝  PHASE 2 — THE EXPANSION SWARM")
    print("━" * 58)

    from src.chunker import chunk_manuscript
    from src.graph import build_graph

    chunks = chunk_manuscript(str(MANUSCRIPT_PATH))
    graph = build_graph()
    total = len(chunks)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Resume Detection ──
    # If we crashed mid-run, pick up where we left off
    expanded_draft = ""
    start_chunk = 0

    if EXPANDED_PATH.exists():
        expanded_draft = EXPANDED_PATH.read_text(encoding="utf-8")
        start_chunk = expanded_draft.count("--- CHUNK END ---")
        if start_chunk > 0:
            print(f"   🔄 Found existing progress! Resuming from chunk {start_chunk + 1}…")

    # ── Thread Pool for Parallel PDF Generation ──
    from concurrent.futures import ThreadPoolExecutor
    from src.publisher import publish_chapter_pdf
    
    # We use a ThreadPoolExecutor to run PDF generation in the background
    # allowing the main loop to proceed to the next chunk immediately.
    pdf_executor = ThreadPoolExecutor(max_workers=3)

    if start_chunk < total:
        # ── Main Expansion Loop ──
        for i, chunk in enumerate(chunks[start_chunk:], start=start_chunk):
            print(f"\n   ── Chunk {i + 1}/{total} ({len(chunk):,} chars) ──")

            config = {"configurable": {"thread_id": str(uuid.uuid4())}}

            try:
                result = graph.invoke(
                    {"current_chunk": chunk, "revision_count": 0},
                    config,
                )
                expanded = result.get("expanded_chunk", chunk)
                print(f"   ✅ Chunk {i + 1} expanded → {len(expanded):,} chars")
                
                # ── Per-Chapter PDF Publishing (ASYNC) ──
                # Submit to thread pool instead of blocking
                print(f"   🚀 Submitting Chapter {i + 1} to PDF generator (background)...")
                pdf_executor.submit(publish_chapter_pdf, expanded, i + 1)

            except Exception as e:
                print(f"   ⚠️  Chunk {i + 1} failed: {e}")
                print("   ↳ Using original chunk as fallback")
                # Log error to file
                check_log = OUTPUT_DIR / "error_log.txt"
                check_log.parent.mkdir(parents=True, exist_ok=True)
                with open(check_log, "a", encoding="utf-8") as f:
                     f.write(f"\n[Chunk {i+1}] {str(e)}\n")
                expanded = chunk

            # ── Checkpoint: save to disk after every chunk ──
            expanded_draft += expanded + CHUNK_SEPARATOR
            EXPANDED_PATH.write_text(expanded_draft, encoding="utf-8")
            print(f"   💾 Checkpoint saved to disk.")

            # ── Throttle: wait between chunks to respect Groq rate limits ──
            if i < total - 1:
                print(f"   🛑 Throttling for {THROTTLE_SECONDS}s (Groq rate-limit cooldown)…")
                for remaining in range(THROTTLE_SECONDS, 0, -1):
                    print(f"\r      ⏳ Resuming in {remaining}s…  ", end="", flush=True)
                    time.sleep(1)
                print("\r      ▶️  Resuming!                  ")

        # ── Cleanup: shutdown thread pool (wait for remaining PDFs) ──
        print("\n   ⏳ Waiting for pending PDF jobs to complete...")
        pdf_executor.shutdown(wait=True)
    
    else:
        print(f"\n   ✅ All {total} chunks already processed.")
        print("   ⏭️  Skipping Expansion & Chapter PDF generation. Moving to Final Assembly.")

    # ── Final expanded text (strip chunk markers for downstream use) ──
    full_expanded = expanded_draft.replace("--- CHUNK END ---", "---").strip()

    print(f"\n   ✅ Phase 2 complete → {EXPANDED_PATH}")
    print(f"   📊 {total} chunks expanded ({len(full_expanded):,} total chars)\n")

    # ──────────────────────────────────────────
    # PHASE 3: THE ART DEPARTMENT
    # ──────────────────────────────────────────
    print("━" * 58)
    print("🎨  PHASE 3 — THE ART DEPARTMENT")
    print("━" * 58)

    from src.resolver import process_art_department

    # Pass the style_config to the resolver
    process_art_department(full_expanded, style_config)

    print(f"\n   ✅ Phase 3 complete → data/output/resolved_manuscript.md\n")

    # ──────────────────────────────────────────
    # PHASE 4: THE TYPESETTING ENGINE
    # ──────────────────────────────────────────
    print("━" * 58)
    print("🖨️  PHASE 4 — THE TYPESETTING ENGINE")
    print("━" * 58)

    from src.publisher import prepare_manuscript, publish_pdf

    prepare_manuscript()
    publish_pdf()

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
    print(f"║  📖  Final PDF: data/output/BookForge_Final.pdf")
    print("╚══════════════════════════════════════════════════════════╝")
    print()


# ──────────────────────────────────────────────
# CLI ENTRY POINT
# ──────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BookForge 4.0 Pipeline")
    parser.add_argument("pdf_input", help="Path to input PDF")
    parser.add_argument("--style", help="Path to Style Reference PDF", default=None)
    
    args = parser.parse_args()

    if not Path(args.pdf_input).exists():
        print(f"❌ File not found: {args.pdf_input}")
        sys.exit(1)
        
    if args.style and not Path(args.style).exists():
        print(f"⚠️ Style file not found: {args.style}. Proceeding without style.")
        args.style = None

    main(args.pdf_input, args.style)
