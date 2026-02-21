# BookEducate 5.0 — The Unified Engine 📚🚀

**Turn raw PDFs into comprehensive, expanded engineering textbooks using AI.**

BookEducate 5.0 is a fault-tolerant, high-fidelity pipeline that deconstructs technical source material, expands it via an AI research swarm, and reassembles it into a professional, typeset PDF using LaTeX.

## ✨ Key Features (v5.0)

- **Fault-Tolerant Pipeline:** Built-in checkpointing (`pipeline_state.json`) ensures that if an error occurs, you can resume exactly where you left off.
- **AI Expansion Swarm:** Uses a multi-agent graph (Analyst, Drafter, Critic) based on LangGraph for high-accuracy technical content expansion.
- **Dynamic Personas:** Configure the subject matter (e.g., Hydraulics, 5G, Thermodynamics) and the AI's persona via environment variables.
- **LaTeX Typesetting:** Direct-to-LaTeX rendering for publication-quality engineering books, with support for complex math ($\LaTeX$) and tcolorbox examples.
- **Centralized Config:** New `src/config.py` manages all paths and settings, reducing duplication and improving maintainability.
- **Robust Asset Resolution:** Enhanced "Art Department" handles image extraction, vision-based transcription, and autonomous recursive AI-generated textbook diagrams natively.
- **Intelligent Structure:** Built-in "Heading Demotion" algorithm automatically converts fragmented AI chunks back into flawless, realistic Chapter structures.

## 🛠️ Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-org/bookeducate.git
    cd bookeducate
    ```

2.  **Activate Virtual Environment:**

    ```bash
    .\venv\Scripts\activate  # Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install System Requirements:**
    - **MiKTeX / TeX Live:** Required for LaTeX PDF generation. [Install MiKTeX](https://miktex.org/howto/install-miktex)
    - **Pandoc:** Used for text processing and template rendering. [Install Pandoc](https://pandoc.org/installing.html)

5.  **Configure Environment:**
    Copy `.env.example` to `.env` and fill in your keys:

    ```env
    GOOGLE_API_KEY=your_key_here
    DEFAULT_MODEL=gemini/gemini-2.0-flash
    IMAGE_MODEL=gemini-2.5-flash

    # Customise the output
    BOOK_SUBJECT=Hydraulics and Pneumatics
    BOOK_PERSONA=Elite Professor of Mechanical Engineering
    MAX_CHUNK_CHARS=8000
    ```

## 🚀 Usage

### ▶️ Standard Workflow

To process a new book from scratch:

```bash
python main.py "path/to/your/source.pdf"
```

### 🔁 Resuming Progress

If the pipeline stops (e.g., rate limits or crash), resume effortlessly:

```bash
python main.py --resume
```

### 🎯 Pipeline Phases

1. **Deconstructor:** (Phase 1) Extracts text and images from source PDF.
2. **Expansion Swarm:** (Phase 2) Expands content using multi-agent LLMs.
3. **Art Department:** (Phase 3) Resolves source documents and transforms graphics.
4. **Typesetting (Unified):** (Phase 4) Recursively resolves all missing AI diagrams, demotes hallucinated chapters for structural integrity, and compiles publication-ready LaTeX PDFs.

Example: Run only the typesetting phase:

```bash
python main.py --phase 4
```

## 📁 File Structure

- `src/`: Core logic modules (agents, chunker, renderer, etc.)
- `src/config.py`: **[NEW]** Centralized configuration and path management.
- `templates/`: LaTeX (`bookeducate.latex`) and class files (`suhbook.cls`).
- `data/output/`: All generated artifacts (logs, JSON, .tex, .pdf).
- `clear_data.py`: Run this to purge the output directory and start fresh.

## ⚙️ Advanced Configuration

- **Chunk Size:** Increase `MAX_CHUNK_CHARS` for models with larger context windows to reduce API calls.
- **Revision Loop:** Controlled by `MAX_REVISIONS` in `src/config.py` (Default: 3).

## 📄 License

MIT License.
