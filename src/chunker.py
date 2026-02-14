"""
BookForge 4.0 — Multi-Strategy Manuscript Chunker
===================================================
Splits ``tagged_manuscript.txt`` into logical, LLM-friendly chunks
using a cascading strategy:

    A.  Split by "Chapter" headings (case-insensitive)
    B.  Split by major numerical sections (``\\n1. ``, ``\\n2. ``, …)
    C.  Hard-split any remaining chunk > MAX_CHUNK_CHARS by length
"""

from __future__ import annotations

import re
from pathlib import Path

MAX_CHUNK_CHARS = 4000  # Target ceiling per chunk


def _split_by_chapter(text: str) -> list[str]:
    """Strategy A: Split on 'Chapter' headings."""
    parts = re.split(r"(?=^(?:Chapter |CHAPTER ))", text, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]


def _split_by_numbered_sections(text: str) -> list[str]:
    """Strategy B: Split on major numbered sections (e.g., \\n1. Introduction)."""
    parts = re.split(r"(?=^\d+\.\s+)", text, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]


def _split_by_length(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """
    Strategy C: Hard-split long text by paragraph boundaries,
    keeping each piece under ``max_chars``.
    """
    paragraphs = text.split("\n\n")
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0

    for para in paragraphs:
        para_len = len(para)
        if current_len + para_len > max_chars and current:
            chunks.append("\n\n".join(current))
            current = []
            current_len = 0
        current.append(para)
        current_len += para_len + 2  # +2 for the "\n\n" join

    if current:
        chunks.append("\n\n".join(current))

    return chunks


def chunk_manuscript(filepath: str | Path) -> list[str]:
    """
    Read a tagged manuscript and split it into chunks using
    a multi-strategy approach:

      1. Try splitting by "Chapter" headings
      2. If that produces ≤ 1 chunk, try numbered sections
      3. Hard-split any chunk still over MAX_CHUNK_CHARS

    Parameters
    ----------
    filepath : str | Path
        Path to ``tagged_manuscript.txt``.

    Returns
    -------
    list[str]
        A list of strings, each representing one chunk.
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Manuscript not found: {filepath}")

    text = filepath.read_text(encoding="utf-8")

    # Strategy A: Chapter-based split
    chunks = _split_by_chapter(text)

    # Strategy B: If only 1 chunk, try numbered sections
    if len(chunks) <= 1:
        print("[Chunker] No 'Chapter' headings found — trying numbered sections…")
        chunks = _split_by_numbered_sections(text)

    # Strategy B fallback: still 1 chunk? Just use the whole text
    if len(chunks) <= 1:
        print("[Chunker] No numbered sections found — using length-based split…")
        chunks = [text]

    # Strategy C: Hard-split any oversized chunk
    final_chunks: list[str] = []
    for chunk in chunks:
        if len(chunk) > MAX_CHUNK_CHARS:
            sub_chunks = _split_by_length(chunk, MAX_CHUNK_CHARS)
            final_chunks.extend(sub_chunks)
        else:
            final_chunks.append(chunk)

    print(f"[Chunker] Split manuscript into {len(final_chunks)} chunk(s)")
    for i, ch in enumerate(final_chunks):
        preview = ch[:80].replace("\n", " ")
        print(f"  Chunk {i + 1}: {len(ch):,} chars — \"{preview}…\"")

    return final_chunks


# ──────────────────────────────────────────────
# CLI ENTRY POINT
# ──────────────────────────────────────────────
if __name__ == "__main__":
    chunks = chunk_manuscript("data/output/tagged_manuscript.txt")
    print(f"\nTotal chunks: {len(chunks)}")
