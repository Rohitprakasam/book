"""
BookForge AI — Streamlit Entry Point
"""

import uuid

import streamlit as st
from langgraph.types import Command

from src.graph import build_graph

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(page_title="BookForge AI", page_icon="📖", layout="wide")

# ──────────────────────────────────────────────
# INITIALISE SESSION STATE
# ──────────────────────────────────────────────
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "graph" not in st.session_state:
    graph, _memory = build_graph()
    st.session_state.graph = graph

if "draft_text" not in st.session_state:
    st.session_state.draft_text = None

if "started" not in st.session_state:
    st.session_state.started = False

graph = st.session_state.graph
config = {"configurable": {"thread_id": st.session_state.thread_id}}

# ──────────────────────────────────────────────
# SIDEBAR — FILE UPLOAD
# ──────────────────────────────────────────────
with st.sidebar:
    st.header("📖 BookForge AI")
    st.caption("Turn a short draft into a comprehensive book.")
    st.divider()

    uploaded = st.file_uploader(
        "Upload 100-page Draft (.txt)", type=["txt"]
    )
    if uploaded is not None:
        st.session_state.draft_text = uploaded.read().decode("utf-8")
        st.success(f"Loaded **{uploaded.name}** ({len(st.session_state.draft_text):,} chars)")

    st.divider()
    st.markdown(
        "**Pipeline:**  \n"
        "`Analyst → Architect → You → Drafter`"
    )

# ──────────────────────────────────────────────
# MAIN AREA
# ──────────────────────────────────────────────
st.title("📖 BookForge AI")
st.markdown("*Your Bionic Editor — AI writes, you steer.*")
st.divider()

# --- Start Button ---
if st.session_state.draft_text and not st.session_state.started:
    if st.button("🚀 Start BookForge", type="primary"):
        with st.spinner("Running Analyst & Architect agents…"):
            graph.invoke(
                {"original_draft": st.session_state.draft_text},
                config,
            )
        st.session_state.started = True
        st.rerun()

elif not st.session_state.draft_text:
    st.info("👈 Upload a `.txt` draft in the sidebar to begin.")

# ──────────────────────────────────────────────
# CHECK GRAPH STATE (handles reruns)
# ──────────────────────────────────────────────
if st.session_state.started:
    current_state = graph.get_state(config)

    # --- CASE 1: Graph is paused at human_interview ---
    if current_state.next and "human_interview" in current_state.next:
        question = current_state.values.get("missing_context_question", "")

        st.warning("🤔 **The AI Architect needs your input before continuing.**")
        st.markdown(f"> **{question}**")

        user_answer = st.text_area(
            "Your Answer:",
            placeholder="Provide as much detail as you can…",
            height=150,
        )

        if st.button("✅ Submit Answer to AI", type="primary"):
            if not user_answer.strip():
                st.error("Please type an answer before submitting.")
            else:
                with st.spinner("Resuming pipeline — Drafter is writing…"):
                    graph.invoke(Command(resume=user_answer), config)
                st.rerun()

    # --- CASE 2: Graph finished — show final draft ---
    elif not current_state.next and "final_draft" in current_state.values:
        final = current_state.values["final_draft"]

        st.success("✅ **Draft generation complete!**")
        st.divider()
        st.markdown(final)
        st.divider()

        st.download_button(
            label="⬇️ Download as Markdown",
            data=final,
            file_name="bookforge_output.md",
            mime="text/markdown",
        )

    # --- CASE 3: Still running (shouldn't happen with invoke) ---
    else:
        st.info("⏳ Pipeline is processing…")
