"""
BookEducate 5.0 — Agent Node Functions (Expansion Swarm)
=======================================================
Three LangGraph nodes forming the per-chunk expansion loop:
    analyst_node → drafter_node → critic_node (→ loop or END)

Persona and subject are configured via environment variables:
    BOOK_SUBJECT  (default: "Engineering")
    BOOK_PERSONA  (default: "Elite Professor specializing in the subject matter")
"""

from __future__ import annotations

import os
from pathlib import Path

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
    model = os.getenv("DEFAULT_MODEL", "groq/llama3-8b-8192")
    if not model:
        print("[Config] ⚠️ WARNING: DEFAULT_MODEL not set, using fallback")
    return model


def _test_llm_connection() -> bool:
    """Test if LLM API is accessible. Returns True if working."""
    model = _get_model()
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    # Check if API key is set for Gemini models
    if model.startswith("gemini/") and not api_key:
        print(f"[Config] ⚠️ WARNING: Gemini model ({model}) requires GOOGLE_API_KEY or GEMINI_API_KEY")
        print(f"[Config]    Current keys: GOOGLE_API_KEY={'SET' if os.getenv('GOOGLE_API_KEY') else 'NOT SET'}, "
              f"GEMINI_API_KEY={'SET' if os.getenv('GEMINI_API_KEY') else 'NOT SET'}")
        return False
    
    try:
        # For Gemini, LiteLLM needs the API key passed explicitly or via env
        # Test with a minimal request
        test_response = litellm.completion(
            model=model,
            timeout=15,  # Short timeout for test
            messages=[{"role": "user", "content": "Say OK"}],
            api_key=api_key if api_key else None,  # Pass API key explicitly
        )
        if test_response and hasattr(test_response, "choices") and test_response.choices:
            content = test_response.choices[0].message.content
            print(f"[Config] ✅ LLM connection test passed (model: {model})")
            return True
        else:
            print(f"[Config] ⚠️ LLM test returned empty response")
            return False
    except Exception as e:
        error_msg = str(e)
        print(f"[Config] ⚠️ LLM connection test failed: {error_msg}")
        
        # Provide helpful diagnostics
        if "401" in error_msg or "authentication" in error_msg.lower():
            print(f"[Config] 💡 Authentication error - check your GOOGLE_API_KEY")
        elif "404" in error_msg or "not found" in error_msg.lower():
            print(f"[Config] 💡 Model not found - verify model name: {model}")
            print(f"[Config]    For Gemini, try: gemini/gemini-2.0-flash or gemini/gemini-1.5-flash")
        elif "429" in error_msg or "rate limit" in error_msg.lower():
            print(f"[Config] 💡 Rate limit hit - wait a moment and retry")
        
        return False


# ──────────────────────────────────────────────
# 1. ANALYST NODE
# ──────────────────────────────────────────────
ANALYST_SYSTEM_PROMPT = """\
You are a {BOOK_PERSONA} focusing on \
{BOOK_SUBJECT}. You are planning the expansion of a chapter \
for a 600-page, publication-ready engineering textbook.

Read the provided chapter text carefully. Your task is to create a \
DETAILED EXPANSION PLAN that will guide the Drafter agent.

For each section you identify, your plan MUST specify:

1. **Theoretical Introduction** — What is the "Why" behind the concept? \
What fundamental principles (Shannon Limit, Signal-to-Noise Ratio, OFDM, MIMO) \
should be derived?

2. **Mathematical Derivations Needed** — List the key equations that \
must be DERIVED from scratch using original notation. Example: if the \
source says "Capacity", you must plan to derive the Shannon-Hartley theorem.

3. **Mirror Problems** — Plan 3-5 original numerical problems per \
section with RANDOMIZED input values. Specify the problem type and \
value ranges (e.g., "Link Budget Calculation: Distance = 2-10km, \
Frequency = 28 GHz").

4. **Diagram Needs** — For every network architecture, frame structure, or \
signal flow, specify a [NEW_DIAGRAM: ...] tag with a technical \
description suitable for technical illustration.

5. **Variable Consistency Dictionary** — To prevent "Drift", you MUST define the specific LaTeX symbols the Drafter should use for this chapter.
   Example:
   - Bandwidth: $B$
   - Signal Power: $S$
   - Noise Power: $N_0$
   - Capacity: $C$

IMPORTANT: You are aware that the Drafter will use LaTeX environments for complex blocks. Your plan should explicitly request "Structure: Example Problem X (LaTeX Format)" for numerical sections.

Return ONLY the bulleted expansion plan in Markdown. No preambles."""


def analyst_node(state: BookState) -> dict:
    """
    Reads the current chunk, analyses core engineering concepts,
    and produces a bulleted expansion plan for the Drafter.
    """
    # Safely extract chunk with validation
    chunk = state.get("current_chunk", "")
    
    if not chunk or len(chunk.strip()) == 0:
        print("[Analyst] ⚠️ Empty chunk received")
        return {"analysis": "Error: Analyst received empty chunk."}

    model = _get_model()
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    try:
        # For Gemini models, ensure API key is available
        if model.startswith("gemini/") and not api_key:
            print(f"[Analyst] ❌ No API key found for Gemini model. Set GOOGLE_API_KEY or GEMINI_API_KEY")
            return {"analysis": "Error: Analyst failed - missing API key."}
        
        response = litellm.completion(
            model=model,
            timeout=LLM_TIMEOUT,
            messages=[
                {"role": "system", "content": ANALYST_SYSTEM_PROMPT.format(
                    BOOK_PERSONA=os.getenv("BOOK_PERSONA", "Elite Professor specializing in the subject matter"),
                    BOOK_SUBJECT=os.getenv("BOOK_SUBJECT", "Engineering"),
                )},
                {
                    "role": "user",
                    "content": f"Here is the chapter text to analyse:\n\n{chunk}",
                },
            ],
            api_key=api_key if model.startswith("gemini/") else None,  # Pass API key for Gemini
        )
    except Exception as e:
        error_msg = str(e)
        print(f"[Analyst] ❌ LLM call failed: {error_msg}")
        
        # Provide specific error guidance
        if "401" in error_msg or "authentication" in error_msg.lower():
            print(f"[Analyst] 💡 Authentication error - check your GOOGLE_API_KEY")
        elif "429" in error_msg or "rate limit" in error_msg.lower():
            print(f"[Analyst] 💡 Rate limit - Gemini API has usage limits")
        elif "404" in error_msg or "not found" in error_msg.lower():
            print(f"[Analyst] 💡 Model not found - verify model name: {model}")
        
        return {"analysis": "Error: Analyst failed to generate plan due to API error."}

    if not response or not hasattr(response, "choices") or not response.choices:
        print("[Analyst] ⚠️ Empty or invalid response from LLM")
        return {"analysis": "Error: Analyst failed to generate plan."}

    try:
        analysis = response.choices[0].message.content
        if not analysis:
            print("[Analyst] ⚠️ Empty content in response")
            return {"analysis": "Error: Analyst returned empty content."}
    except (AttributeError, IndexError, KeyError) as e:
        print(f"[Analyst] ⚠️ Failed to extract content from response: {e}")
        return {"analysis": "Error: Analyst response format invalid."}

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
   - If the source text contains `[ORIGINAL_ASSET: filepath]` tags, YOU MUST PRESERVE THEM EXACTLY AS THEY ARE in your expanded output. Do not alter or remove them.
   - Whenever an entirely NEW visual aid is necessary to explain a complex mechanism, insert an Image Request block in exact JSON format. DO NOT use standard Markdown image links.
   - "caption": A short, title-case name for the figure (e.g., "Figure 1.2: Hydraulic Gear Pump").
   - "subject": A detailed visual description for the artist.
   - "type": "technical illustration", "schematic", or "graph".

Example:
[NEW_DIAGRAM: {"caption": "Figure 2.1: Double-Acting Cylinder Cross-Section", "subject": "Cross-section of a double-acting hydraulic cylinder showing fluid flow paths and piston seals", "type": "technical illustration"}]

5. Formatting Rules (CRITICAL):
   - For standard text, use Markdown.
   - For "Example Problems", "Definitions", or "Key Takeaways", YOU MUST USE LATEX ENVIRONMENTS.
   - Format Example Problems exactly like this:
     
     \\begin{exampleproblem}{Example Problem X: [Title]}
       \\textbf{Problem Statement:} [Text]
       \\begin{solution}
         1. Step one...
         $$ math equation $$
       \\end{solution}
     \\end{exampleproblem}

   - Do NOT use Markdown bullet points or bold text for these headers. Use the LaTeX structure above.
   
6. Output the final expanded text in clean Markdown (with embedded HTML where specified)."""


def drafter_node(state: BookState) -> dict:
    """
    Expands the chapter using synthetic authoring with first-principles
    derivation, mirror problems, and diagram tags.
    """
    import json
    from pathlib import Path
    
    # Safely extract state with defaults
    chunk = state.get("current_chunk", "")
    analysis = state.get("analysis", "")
    feedback = state.get("feedback", "")
    
    # Validate inputs
    if not chunk or len(chunk.strip()) == 0:
        print("[Drafter] ⚠️ Empty chunk received, returning as-is")
        return {"expanded_chunk": chunk, "revision_count": state.get("revision_count", 0)}
    
    # If analysis indicates an error, skip expansion
    if analysis and analysis.startswith("Error:"):
        print("[Drafter] ⚠️ Analyst failed, skipping expansion")
        return {"expanded_chunk": chunk, "revision_count": state.get("revision_count", 0)}

    # --- Load Transcribed Math (OCR Data) ---
    math_context = ""
    _base = Path(__file__).resolve().parent.parent
    math_path = _base / "data" / "output" / "transcribed_math.json"
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

    # --- Retry Loop for LLM Stability ---
    max_retries = 3
    expanded = None
    
    model = _get_model()
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    for attempt in range(max_retries):
        try:
            # For Gemini models, ensure API key is available
            if model.startswith("gemini/") and not api_key:
                print(f"[Drafter] ❌ No API key found for Gemini model. Set GOOGLE_API_KEY or GEMINI_API_KEY")
                break  # Exit retry loop
            
            response = litellm.completion(
                model=model,
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
                api_key=api_key if model.startswith("gemini/") else None,  # Pass API key for Gemini
            )

            if response and hasattr(response, "choices") and response.choices:
                content = response.choices[0].message.content
                if content:
                    expanded = content
                    break  # Success!
            
            print(f"[Drafter] ⚠️ Empty response from LLM (Attempt {attempt+1}/{max_retries})")
        except Exception as e:
            error_msg = str(e)
            print(f"[Drafter] ⚠️ LLM Error (Attempt {attempt+1}/{max_retries}): {error_msg}")
            
            # Provide specific error guidance
            if "401" in error_msg or "authentication" in error_msg.lower():
                print(f"[Drafter] 💡 Authentication error - check your GOOGLE_API_KEY")
            elif "429" in error_msg or "rate limit" in error_msg.lower():
                print(f"[Drafter] 💡 Rate limit - waiting before retry...")
                import time
                time.sleep(5 * (attempt + 1))  # Exponential backoff
            elif "404" in error_msg or "not found" in error_msg.lower():
                print(f"[Drafter] 💡 Model not found - verify model name: {model}")
                break  # Don't retry if model doesn't exist
            
    # If all retries failed, use original chunk
    if expanded is None:
        print("[Drafter] ❌ CRITICAL FAILURE: LLM failed 3 times. Returning original chunk.")
        return {"expanded_chunk": chunk, "revision_count": state.get("revision_count", 0) + 1}

    # If we get here, 'expanded' is defined
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

NOTE: The Drafter has been instructed to use LaTeX environments (e.g., \\begin{exampleproblem}) for "Example Problems". This is EXPECTED and should NOT be flagged as an artifact.

If the draft passes all checks, output 'APPROVED' followed by the final markdown."""


def critic_node(state: BookState) -> dict:
    """
    Reviews the expanded chunk for mathematical correctness,
    problem quality, copyright independence, and formatting.
    """
    # Safely extract state with defaults
    expanded = state.get("expanded_chunk", "")
    original = state.get("current_chunk", "")
    
    # Validate inputs
    if not expanded or len(expanded.strip()) == 0:
        print("[Critic] ⚠️ Empty expanded chunk, approving by default")
        return {"feedback": "APPROVED"}
    
    if not original or len(original.strip()) == 0:
        print("[Critic] ⚠️ Empty original chunk, approving by default")
        return {"feedback": "APPROVED"}

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

    model = _get_model()
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    try:
        # For Gemini models, ensure API key is available
        if model.startswith("gemini/") and not api_key:
            print(f"[Critic] ❌ No API key found for Gemini model. Approving by default.")
            return {"feedback": "APPROVED"}
        
        response = litellm.completion(
            model=model,
            timeout=LLM_TIMEOUT,
            messages=[
                {"role": "system", "content": CRITIC_SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": (
                        f"=== ORIGINAL SOURCE ({len(original):,} chars) ===\n{original}\n\n"
                        f"=== EXPANDED DRAFT ({len(expanded):,} chars) ===\n{expanded}"
                    ),
                },
            ],
            api_key=api_key if model.startswith("gemini/") else None,  # Pass API key for Gemini
        )
    except Exception as e:
        error_msg = str(e)
        print(f"[Critic] ❌ LLM call failed: {error_msg}. Approving by default.")
        
        # Provide specific error guidance
        if "401" in error_msg or "authentication" in error_msg.lower():
            print(f"[Critic] 💡 Authentication error - check your GOOGLE_API_KEY")
        elif "429" in error_msg or "rate limit" in error_msg.lower():
            print(f"[Critic] 💡 Rate limit - Gemini API has usage limits")
        
        return {"feedback": "APPROVED"}  # Fallback to approve if critic API fails

    if not response or not hasattr(response, "choices") or not response.choices:
        print("[Critic] ⚠️ Empty or invalid response from LLM. Approving by default.")
        return {"feedback": "APPROVED"}  # Fallback to approve if critic fails

    try:
        content = response.choices[0].message.content
        if not content:
            print("[Critic] ⚠️ Empty content in response. Approving by default.")
            return {"feedback": "APPROVED"}
        feedback = content.strip()
    except (AttributeError, IndexError, KeyError) as e:
        print(f"[Critic] ⚠️ Failed to extract content: {e}. Approving by default.")
        return {"feedback": "APPROVED"}

    is_approved = feedback.upper().startswith("APPROVED")

    if is_approved:
        print(f"[Critic] ✅ APPROVED ({ratio:.1f}x expansion)")
    else:
        print(f"[Critic] ❌ Revision needed — {feedback[:100]}…")

    return {"feedback": feedback}
