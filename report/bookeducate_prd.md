# Product Requirements Document (PRD)

**Product Name:** BookEducate 5.0
**Document Version:** 1.0

## 1. Product Vision & Objective

BookEducate 5.0 aims to democratize the creation of high-quality educational textbooks by automating the expansion, illustration, and typesetting of minimal source PDFs. It serves as an autonomous ghostwriter, illustrator, and typesetter for educators, engineers, and publishers.

## 2. Target Audience

- **University Professors & Educators:** Needing to instantly turn lecture slides or brief syllabi into comprehensive course textbooks.
- **Technical Writers:** Seeking to expand brief mechanical or software documentation into highly detailed manuals.
- **EdTech Platforms:** Looking to dynamically generate copyright-free, targeted learning materials.

## 3. Core Features

### 3.1 PDF Deconstruction & Visual Triage

- **Requirement:** System must extract text and images from any unencrypted PDF.
- **Feature:** Advanced Visual Triage to discard useless artifacts (e.g., logos <80px) and preserve critical academic charts (`[ORIGINAL_ASSET]`).

### 3.2 AI Expansion Swarm

- **Requirement:** System must expand the extracted syllabus by 5x-10x.
- **Feature:** A multi-agent network (Analyst -> Drafter -> Critic) generating step-by-step math derivations, historical context, and mirror practice problems without hallucinating false mechanics.

### 3.3 Autonomous Art Generation

- **Requirement:** System must visually explain complex mechanisms described in text.
- **Feature:** The Drafter injects `[NEW_DIAGRAM]` tags natively into the text. The Art Department module intercepts these tags, invokes Google Gemini's Image generation, and embeds the visuals.

### 3.4 LaTeX Typesetting Engine

- **Requirement:** Output must reflect a professional, academic standard.
- **Feature:** Automated structuring into JSON, programmatic heading demotion for logical flow, and native compilation to strictly formatted LaTeX source code, rendered directly to a final PDF.

## 4. Non-Functional Requirements (NFRs)

- **Fault Tolerance:** If a chunk fails AI expansion or an image API times out, the system must gracefully degrade (e.g., leaving placeholder text/images) rather than crashing the pipeline.
- **Data Isolation:** Fresh executions must systematically purge the `chroma_db` vector database to prevent contextual hallucination spanning different book subjects.
- **Scalability:** The pipeline must support massive documents (up to 1000+ output pages) using optimized pagination and token chunking algorithms.

## 5. Cost Estimation & API Billing (2026)

BookEducate 5.0 relies primarily on the Google Gemini API ecosystem for text expansion, diagramming, and visual triage. Below is the operational cost structure based on standard 2026 pricing.

### 5.1 LLM Token Pricing Matrices

| Model Tier                | Input Tokens | Output Tokens | Context Cache | Batch Input | Batch Output | Ideal BookEducate Use Case                                   |
| :------------------------ | :----------- | :------------ | :------------ | :---------- | :----------- | :--------------------------------------------------------- |
| **Gemini 2.5 Flash-Lite** | $0.10 / 1M   | $0.40 / 1M    | $0.01 / 1M    | $0.05 / 1M  | $0.20 / 1M   | **Basic structuring & triage** (Most affordable, ~$0.50/M) |
| **Gemini 2.5 Flash**      | $0.30 / 1M   | $2.50 / 1M    | $0.03 / 1M    | $0.15 / 1M  | $1.25 / 1M   | **Core Expansion Swarm** (Best cost/performance, ~$2.80/M) |
| **Gemini 3 Flash**        | $0.50 / 1M   | $3.00 / 1M    | $0.05 / 1M    | $0.25 / 1M  | $1.50 / 1M   | Heavy automated drafting (~$3.50/M)                        |
| **Gemini 2.5 Pro**        | $1.25 / 1M   | $10.00 / 1M   | $0.31 / 1M    | -           | -            | Deep academic reasoning (~$11.25/M)                        |
| **Gemini 3 Pro**          | $2.00 / 1M   | $12.00 / 1M   | N/A           | -           | -            | Premium quality synthesis (~$14.00/M)                      |

_(Note: Long prompts >200K tokens incur roughly 2x input/output rates on Pro models)._

### 5.2 Art Department (Image Generation) Pricing

BookEducate 5.0 generates custom technical diagrams via native image models (e.g., `gemini-2.5-flash-image`). Image prompts are charged standard token rates, with flat fees per rendered image:

- **Standard Image (up to 1024×1024):** ~$0.039 per successful image.
- **Large Image (up to 2048×2048):** ~$0.134 per successful image.
- **4K Image Generation:** ~$0.240 per successful image.

### 5.3 Pipeline Optimization Strategy

- **Batch Processing:** Whenever feasible, Phase 2 chunk processing will be batched to reduce token costs by up to 50%.
- **Context Caching:** To prevent paying repeatedly for the static `BOOK_PERSONA` and `BOOK_SUBJECT` instructions on every isolated chunk, the Swarm utilizes context caching to drop input rates to ~$0.03 per million.

### 5.4 Real-World Sample Calculation (Massive 1500-Page Output)

Below is an estimated API cost breakdown for taking a highly condensed **150-page source PDF** and using the Swarm to expand it 10x into a **massive 1500-page fully illustrated technical textbook**, assuming the use of **Gemini 2.5 Flash** for text and **Gemini 2.5 Flash-Image** for diagrams.

| Resource Type                                                                    | Consumption Estimate                      | Calculation               | Estimated Cost |
| :------------------------------------------------------------------------------- | :---------------------------------------- | :------------------------ | :------------- |
| **Input Tokens** (Source parsing, System Context, Prompts across ~100 LLM calls) | ~2,000,000 tokens                         | 2.0M × $0.30              | **$0.60**      |
| **Output Tokens** (1500 pages @ ~500 tokens/page)                                | ~750,000 tokens _(inc. JSON Structuring)_ | 0.75M × $2.50             | **$1.87**      |
| **AI Image Generation** (Assumes 1 standard diagram every 5 pages)               | 300 Standard Images (1024x1024)           | 300 × $0.039              | **$11.70**     |
|                                                                                  |                                           | **Total Estimated Cost:** | **~$14.17**    |

_Conclusion:_ BookEducate 5.0 can autonomously author, structure, and illustrate a massive 1500-page collegiate-grade technical textbook (with hundreds of custom diagrams) from a 150-page syllabus for **under $15.00 in API overhead**.

## 6. Future Roadmap

- Integration of a Web GUI for live monitoring of the expansion swarm and dynamic cost tracking.
- Support for additional output formats (EPUB, HTML5 interactive textbooks).
- Deep integration with custom RAG (Retrieval-Augmented Generation) libraries for highly specialized, proprietary corporate knowledge generation.
