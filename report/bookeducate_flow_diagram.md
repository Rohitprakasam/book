# 🌊 PROCESS FLOW DIAGRAM: BookEducate 5.0

This document visualizes the complete end-to-end execution lifecycle of the autonomous BookEducate pipeline. From initial user execution to PDF delivery, it maps out how the Orchestrator delegates tasks to the four critical agent phases.

```mermaid
sequenceDiagram
    autonumber
    actor User as User (Terminal)
    participant Orchestrator as Master Orchestrator (main.py)
    participant P1 as Phase 1:<br/>The Deconstructor
    participant P2 as Phase 2:<br/>The Expansion Swarm
    participant P3 as Phase 3:<br/>The Art Department
    participant P4 as Phase 4:<br/>The Typesetting Engine

    %% Initialization
    User->>Orchestrator: CLI Command: `python main.py <PDF_PATH>`
    activate Orchestrator

    %% Automatic Data Sterilization
    note over Orchestrator: Data Sterilization
    Orchestrator->>Orchestrator: Purge previous `data/output`
    Orchestrator->>Orchestrator: Obliterate `data/chroma_db` (Vector Database)

    %% Phase 1
    Orchestrator->>P1: Initiate Phase 1 (Ingest Raw PDF)
    activate P1
    P1->>P1: Extract Text Layers via PyMuPDF
    P1->>P1: Extract Native PDF Images & Apply Bounding Bounds

    %% Visual Triage Agent
    note over P1: Gemini Vision Triage
    P1->>P1: Audit extracted images (<80px discarded)
    P1->>P1: Classify remaining as KEEP or TRANSCRIBE (Math/Tables)
    P1-->>Orchestrator: Return `tagged_manuscript.txt` (Contains `[ORIGINAL_ASSET]`)
    deactivate P1

    %% Phase 2
    Orchestrator->>P2: Initiate Phase 2 (Content Synthesis)
    activate P2
    P2->>P2: Chunk text into collegiate boundaries (`Chapter`, `Unit`, `Module`)

    loop Per Academic Chunk
        note over P2: Multi-Agent LLM Sub-Loop
        P2->>P2: The Analyst: Parses structure & plans expansion
        P2->>P2: The Drafter: Synthesizes text, formulas & practice problems
        P2->>P2: The Drafter: Injects Image Generation Prompts (`[NEW_DIAGRAM]`)
        P2->>P2: The Critic: Validates output against hallucination guards
    end

    P2-->>Orchestrator: Return `expanded_draft.md`
    deactivate P2

    %% Phase 3
    Orchestrator->>P3: Initiate Phase 3 (Visual Asset Generation)
    activate P3
    note over P3: Gemini Vision Synthesis (gemini-2.5-flash)
    P3->>P3: Parse entire document recursively

    loop Detected Graphics Tags
        P3->>P3: Encounter `[NEW_DIAGRAM]`
        P3->>P3: Execute API Call (Dynamic Fallback handling on 429)
        P3->>P3: Download rendered illustration to `/assets/ai_generated/`
    end

    P3-->>Orchestrator: Return `resolved_manuscript.md` (Raw Markdown with Valid Hooks)
    deactivate P3

    %% Phase 4
    Orchestrator->>P4: Initiate Phase 4 (Structure & Typesetting)
    activate P4
    P4->>P4: Convert Markdown into strictly enforced JSON Object Model

    note over P4: AI Heading Demotion Safety
    P4->>P4: Evaluate JSON `level: 1` headers
    P4->>P4: Mutate false chapters into `level: 2` sub-sections

    note over P4: Native Image Linking
    P4->>P4: Wire `[ORIGINAL_ASSET]` IDs mapping back to Phase 1 Assets

    P4->>P4: Compile sanitized JSON object into `.tex` (LaTeX Source Code)
    P4->>P4: Execute Shell command: `pdflatex -interaction=batchmode`
    P4-->>Orchestrator: Return `BookEducate.pdf`
    deactivate P4

    %% Delivery
    Orchestrator-->>User: Deployment Complete. Pipeline Terminated.
    deactivate Orchestrator
```
