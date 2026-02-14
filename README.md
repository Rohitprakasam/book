# BookForge 📚🚀

**Turn raw PDFs into comprehensive, expanded textbooks using AI.**

BookForge is an intelligent pipeline that deconstructs source material (PDFs), expands the content by **5x** using a "First-Principles" AI swarm, and republishes it as a polished HTML5 website or a print-ready PDF.

## ✨ Features

-   **Deep Content Expansion:** Uses a LangGraph swarm (Analyst, Drafter, Critic) to analyze and expand every topic.
-   **Math-Aware:** Perfect rendering of complex equations using MathJax (HTML) and LaTeX (PDF).
-   **Multi-Format Output:**
    -   **HTML5:** Instant, responsive, and searchable (Zero compile time).
    -   **PDF:** High-quality print output via Headless Edge (bypassing LaTeX errors).
-   **Visuals:** Integrated "Art Department" to propose and generate diagrams (Gemini 2.5 Flash Image).

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/bookforge.git
    cd bookforge
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate # Mac/Linux
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install System Requirements:**
    -   **Pandoc:** Required for document conversion. [Install Pandoc](https://pandoc.org/installing.html)
    -   **Microsoft Edge:** Required for HTML-to-PDF conversion.

5.  **Configure Environment:**
    Create a `.env` file in the root directory:
    ```env
    GEMINI_API_KEY=your_google_ai_key_here
    DEFAULT_MODEL=gemini-1.5-flash
    IMAGE_MODEL=gemini-2.5-flash-image
    ```

## 🚀 Usage

### 1. Generate the Book
Run the main pipeline to ingest your PDF and generate the expanded draft:
```bash
python main.py --file "path/to/your/source.pdf"
```

### 2. Publish as HTML (Recommended)
Generate a clean, responsive HTML version of the book:
```bash
python publish_html.py
```
*Output:* `data/output/BookForge_Final.html`

### 3. Convert to PDF
Convert the HTML version to a PDF using the headless browser engine:
```bash
python pdf_printer.py
```
*Output:* `data/output/BookForge_Final_Print.pdf`

### 4. Cleanup
Remove temporary build files and intermediates to save space:
```bash
python cleanup.py
```

## 📂 Project Structure

-   `src/`: Core logic (Agents, Publisher, Resolver).
-   `templates/`: CSS and LaTeX templates.
-   `data/`: Input PDFs and generated Output.
-   `main.py`: Pipeline orchestrator.
-   `publish_html.py`: HTML generator script.
-   `pdf_printer.py`: PDF converter script.

## 📄 License
MIT License.
