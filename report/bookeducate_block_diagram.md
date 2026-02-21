# 🗂️ SYSTEM ARCHITECTURE BLOCK DIAGRAM: BookEducate 5.0

This architectural block diagram maps the high-level software dependencies, module integration, and data persistence layers of the BookEducate 5.0 engine.

```mermaid
graph TD
    classDef memory fill:#e8f4f8,stroke:#0369a1,stroke-width:2px;
    classDef core fill:#eff6ff,stroke:#2563eb,stroke-width:2px;
    classDef external fill:#f0fdf4,stroke:#16a34a,stroke-width:2px;
    classDef output fill:#fef3c7,stroke:#d97706,stroke-width:2px;

    %% Data Inputs
    Input[Raw User PDF Document] --> Orchestrator
    Config[.env Global Configs] -.-> Orchestrator

    %% Core Application Layer
    subgraph Core Engine Orchestration
        Orchestrator{main.py<br/>Master Controller}:::core
    end

    %% Phase 1 - Deconstruction Subsystem
    subgraph Subsystem 1: Deconstruction
        Orchestrator --> P1[src/deconstructor.py]
        P1 --> Triage[src/triage.py]
    end

    %% Phase 2 - Expansion Subsystem
    subgraph Subsystem 2: Multi-Agent Expansion
        Orchestrator --> P2[src/agents.py]
        P2 --> Chunker[src/chunker.py]

        %% Agent Node Logic
        P2 --> Analyst((Analyst Node))
        P2 --> Drafter((Drafter Node))
        P2 --> Critic((Critic Node))
    end

    %% Phase 3 - Art Subsystem
    subgraph Subsystem 3: Visual Generation
        Orchestrator --> P3[src/resolver.py]
    end

    %% Phase 4 - Compilation Subsystem
    subgraph Subsystem 4: Typesetting Engine
        Orchestrator --> P4[src/renderer_latex.py]
        P4 --> Structurer[src/structurer.py]
    end

    %% External APIs & Web Services
    subgraph API Over-The-Wire Services
        Triage -.-> GeminiVision[Gemini API: Vision Models]:::external
        P2 -.-> LiteLLM[LLM Gateway: Groq / Llama / Gemini]:::external
        P3 -.-> GeminiImage[Gemini API: Image Gen]:::external
    end

    %% File IO & Data Persistence
    subgraph Stateful Memory (Local File System)
        P1 --> AssCache[(Assets Cache<br/>/extracted_images/)]:::memory
        P2 --> ExpDraft[(Expanded Draft<br/>expanded_draft.md)]:::memory
        P2 <--> Chroma[(ChromaDB Vector Store)]:::memory
        P3 --> GenAssets[(AI Diagram Library<br/>/ai_generated/)]:::memory
        P4 --> StructJSON[(book_structure.json)]:::memory
    end

    %% Compiled Final Output
    P4 --> PDFOut([BookEducate.pdf<br/>Compiled Textbook]):::output
```
