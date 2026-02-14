"""
BookForge 5.0 — Agent Node Functions (Expansion Swarm)
=======================================================
Three LangGraph nodes forming the per-chunk expansion loop:
    analyst_node → drafter_node → critic_node (→ loop or END)

Persona: Elite Professor of Mechanical Engineering
Subject: Hydraulics and Pneumatics
Style: Synthetic authoring, first-principles derivation, LaTeX math
"""

from __future__ import annotations

import os

import litellm
from dotenv import load_dotenv

from src.state import BookState

load_dotenv()

# ──────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────
LLM_TIMEOUT = 1800  # 30 minutes — gives CPU-based Ollama time to finish


def _get_model() -> str:
    """Return the model identifier from the environment."""
    return os.getenv("DEFAULT_MODEL", "groq/llama3-8b-8192")


# ──────────────────────────────────────────────
# 1. ANALYST NODE
# ──────────────────────────────────────────────
ANALYST_SYSTEM_PROMPT = """\
You are an Elite Professor of Mechanical Engineering specializing in \
Hydraulics and Pneumatics. You are planning the expansion of a chapter \
for a 600-page, publication-ready engineering textbook.

Read the provided chapter text carefully. Your task is to create a \
DETAILED EXPANSION PLAN that will guide the Drafter agent.

For each section you identify, your plan MUST specify:

1. **Theoretical Introduction** — What is the "Why" behind the concept? \
What first-principles physics (Force, Pressure, Energy, Continuity) \
should be derived?

2. **Mathematical Derivations Needed** — List the key equations that \
must be DERIVED from scratch using original notation. Example: if the \
source says "Bernoulli's equation", you must plan to derive it from \
the Work-Energy theorem or Navier-Stokes limits.

3. **Mirror Problems** — Plan 3-5 original numerical problems per \
section with RANDOMIZED input values. Specify the problem type and \
value ranges (e.g., "Cylinder force problem: bore = 45-120mm, \
pressure = 5-25 MPa").

4. **Diagram Needs** — For every hydraulic circuit, component, or \
flow path, specify a [NEW_DIAGRAM: ...] tag with a technical \
description suitable for TikZ rendering.

6. **Variable Consistency Dictionary** — To prevent "Drift", you MUST define the specific LaTeX symbols the Drafter should use for this chapter.
   Example:
   - Pressure: $p$ (lower case)
   - Power: $\\mathcal{P}$ (calligraphic)
   - Efficiency: $\\eta_{hyd}$
   - Flow Rate: $Q_{in}$

Return ONLY the bulleted expansion plan in Markdown. No preambles."""


def analyst_node(state: BookState) -> dict:
    """
    Reads the current chunk, analyses core engineering concepts,
    and produces a bulleted expansion plan for the Drafter.
    """
    chunk = state["current_chunk"]

    response = litellm.completion(
        model=_get_model(),
        timeout=LLM_TIMEOUT,
        messages=[
            {"role": "system", "content": ANALYST_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Here is the chapter text to analyse:\n\n{chunk}",
            },
        ],
    )

    if not response.choices:
        print("[Analyst] ⚠️ Empty response from LLM")
        return {"analysis": "Error: Analyst failed to generate plan."}

    analysis = response.choices[0].message.content
    print(f"[Analyst] Produced expansion plan ({len(analysis):,} chars)")
    return {"analysis": analysis}


# ──────────────────────────────────────────────
# 2. DRAFTER NODE
# ──────────────────────────────────────────────
DRAFTER_SYSTEM_PROMPT = """You are an Expert Engineering Textbook Author. You will receive a discrete text chunk extracted from a Source_Manuscript.

Your task is to EXPAND this text chunk by 5x while maintaining zero hallucinations and absolute mathematical precision.

Expansion Rules:

1. Explanations: Turn single bullet points into detailed, multi-paragraph explanations.

2. Context: Add relevant historical context or real-world industrial applications for every concept.

3. Step-by-Step: If a mathematical formula is present, scramble the variables to ensure copyright compliance, derive it from first principles, and provide 2 step-by-step example problems. DO NOT invent fake formulas.

4. Art Direction Rules:
Whenever a visual aid is necessary to explain a complex mechanism, insert an Image Request block in exact JSON format. DO NOT use Markdown image links.
Example:
[NEW_DIAGRAM: {"subject": "Cross-section of a double-acting hydraulic cylinder showing fluid flow", "type": "technical illustration"}]

Output the final expanded text in clean Markdown."""


def drafter_node(state: BookState) -> dict:
    import json
    from pathlib import Path

    """
    Expands the chapter using synthetic authoring with first-principles
    derivation, mirror problems, and diagram tags.
    """
    chunk = state["current_chunk"]
    analysis = state.get("analysis", "")
    feedback = state.get("feedback", "")

    # --- Load Transcribed Math (OCR Data) ---
    math_context = ""
    math_path = Path("data/output/transcribed_math.json")
    if math_path.exists():
        try:
            math_data = json.loads(math_path.read_text(encoding="utf-8"))
            # Simple heuristic: Include ALL transcribed math for now, 
            # or filter by page if we had page info in chunk. 
            # Since we iterate sequentially, passing the whole dict is okay for 128k context, 
            # but better to just pass it all as reference.
            if math_data:
                math_formatted = json.dumps(math_data, indent=2)
                math_context = f"\n\n=== TRANSCRIBED MATH (RESCUED FROM IMAGES) ===\n{math_formatted}\n"
        except Exception as e:
            print(f"⚠️ Failed to load math JSON: {e}")

    # Build context: if in revision loop, include critic feedback
    revision_context = ""
    if feedback and feedback != "APPROVED":
        revision_context = (
            f"\n\n=== CRITIC FEEDBACK (address these issues) ===\n{feedback}"
        )

    response = litellm.completion(
        model=_get_model(),
        timeout=LLM_TIMEOUT,
        messages=[
            {"role": "system", "content": DRAFTER_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"=== ORIGINAL CHAPTER ({len(chunk):,} chars — expand to "
                    f"at least {len(chunk) * 5:,} chars) ===\n{chunk}\n\n"
                    f"=== EXPANSION PLAN ===\n{analysis}"
                    f"{math_context}"
                    f"{revision_context}"
                ),
            },
        ],
    )

    if not response.choices:
        print("[Drafter] ⚠️ Empty response from LLM")
        return {"expanded_chunk": chunk, "revision_count": state.get("revision_count", 0)}

    expanded = response.choices[0].message.content
    revision = state.get("revision_count", 0) + 1
    
    # --- Strip Markdown Wrappers (Safety Net) ---
    expanded = expanded.replace("```markdown", "").replace("```", "")
    
    ratio = len(expanded) / max(len(chunk), 1)
    print(f"[Drafter] Expanded chunk ({len(expanded):,} chars, {ratio:.1f}x) — revision {revision}")

    return {"expanded_chunk": expanded, "revision_count": revision}


# ──────────────────────────────────────────────
# 3. CRITIC NODE
# ──────────────────────────────────────────────
MIN_EXPANSION_RATIO = 4.0  # Must be at least 4x-5x the original

CRITIC_SYSTEM_PROMPT = """You are a strict Textbook Editor. Review the Drafter's expanded text against the original chunk from the Source_Manuscript.

Rejection Criteria (Return to Drafter if any are met):

Low Effort: If the generated text is not at least 4x to 5x the length of the original source chunk, REJECT it with feedback to add more case studies or step-by-step examples.

Hallucination: If the Drafter introduced mathematical formulas NOT derived from the Source_Manuscript, REJECT it.

Malformed Tags: If the [NEW_DIAGRAM] tags are not valid JSON, REJECT it.

If the draft passes all checks, output 'APPROVED' followed by the final markdown."""


def critic_node(state: BookState) -> dict:
    """
    Reviews the expanded chunk for mathematical correctness,
    problem quality, copyright independence, and formatting.
    """
    expanded = state["expanded_chunk"]
    original = state["current_chunk"]

    # ── Low-Effort Check ──
    ratio = len(expanded) / max(len(original), 1)
    if ratio < MIN_EXPANSION_RATIO:
        rejection = (
            f"LOW EFFORT: The expanded text is only {ratio:.1f}x the original "
            f"({len(expanded):,} vs {len(original):,} chars). "
            f"You MUST produce at least {MIN_EXPANSION_RATIO}x expansion. "
            "Go deeper: add more derivations, more mirror problems with "
            "randomized values, more [NEW_DIAGRAM: ...] tags. "
            "Do not summarize — DERIVE and EXPAND."
        )
        print(f"[Critic] ❌ Low effort ({ratio:.1f}x) — forcing re-draft")
        return {"feedback": rejection}

    # ── Artifact Check ──
    if "```markdown" in expanded or expanded.strip().startswith("```"):
         rejection = "ARTIFACT DETECTED: Remove ```markdown code fences from the output."
         print(f"[Critic] ❌ Artifact detected")
         return {"feedback": rejection}

    response = litellm.completion(
        model=_get_model(),
        timeout=LLM_TIMEOUT,
        messages=[
            {"role": "system", "content": CRITIC_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Review this expanded chapter:\n\n{expanded}",
            },
        ],
    )

    if not response.choices:
         print("[Critic] ⚠️ Empty response from LLM")
         return {"feedback": "APPROVED"} # Fallback to approve if critic fails

    feedback = response.choices[0].message.content.strip()
    is_approved = feedback.upper().startswith("APPROVED")

    if is_approved:
        print(f"[Critic] ✅ APPROVED ({ratio:.1f}x expansion)")
    else:
        print(f"[Critic] ❌ Revision needed — {feedback[:100]}…")

    return {"feedback": feedback}
