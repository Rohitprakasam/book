# BookEducate 5.0 — Frontend API Integration Contracts

This document outlines the API contracts required for the external frontend team (React/Next.js/Vue) to integrate with the BookForge 5.0 Python backend engine.

The backend will run locally on **`http://localhost:3030`**. All cross-origin requests (CORS) from the frontend development server (e.g., `localhost:8000`) must be approved by the backend.

---

## 1. Upload Contract (`POST /api/v1/generate`)

**Purpose:** The frontend uses this endpoint to submit the initial user configuration and the source PDF document. Because it includes a file, this must use `multipart/form-data`.

**Request Format:** `multipart/form-data`

- `file`: (Binary / File) The source PDF or txt document.
- `config`: (Stringified JSON) The generation settings.

**Example `config` payload:**

```json
{
  "book_subject": "General Engineering",
  "book_persona": "Senior Engineering Professor",
  "target_pages": 600
}
```

**Response Format:** `application/json`

```json
// Success (202 Accepted)
{
  "status": "processing",
  "job_id": "job_12345abcde",
  "message": "Upload successful. Generation pipeline started."
}

// Error (400 Bad Request)
{
  "status": "error",
  "error_code": "INVALID_FILE_TYPE",
  "message": "Only .pdf and .txt files are supported."
}
```

---

## 2. Progress Contract (`GET /api/v1/jobs/{job_id}/progress`)

**Purpose:** Book generation takes 2 to 10 hours. A standard HTTP request will timeout. The frontend MUST stream progress updates dynamically using **Server-Sent Events (SSE)**.

**Streaming Response Format (Server-Sent Event):** `text/event-stream`

```text
data: {
data:   "job_id": "job_12345abcde",
data:   "progress_percentage": 15,
data:   "current_phase": "Phase 2 - The Expansion Swarm",
data:   "current_task": "Drafting chunk 22 of 146...",
data:   "status": "running"
data: }
```

_Frontend Behavior:_ Listen to this stream and update a circular/linear loading bar (`progress_percentage`) and a text status label (`current_phase` / `current_task`).

---

## 3. Live Logs Contract (`GET /api/v1/jobs/{job_id}/logs`)

**Purpose:** Streams every single terminal log (from Phase 1: Deconstruction all the way to Phase 6: Sync) directly to the Frontend Loading Page. This ensures the user gets a "Live Terminal" view of the AI Swarm making decisions under the hood while they wait.

**How to implement on Loading Page:** The frontend should poll this endpoint (or connect to it via SSE) and append the new lines to a scrolling `<pre>` terminal window inside the Loading UI.

**Response Format:** `application/json` (Pagination supported)

```json
// Success (200 OK)
{
  "job_id": "job_12345abcde",
  "logs": [
    {
      "timestamp": "2026-02-23T10:15:00Z",
      "level": "INFO",
      "source": "Phase 2 - Router",
      "message": "Sending back for revision 1"
    },
    {
      "timestamp": "2026-02-23T10:15:05Z",
      "level": "WARN",
      "source": "Phase 4 - Structurer",
      "message": "Internet connection lost. Pausing for 30s before retrying..."
    },
    {
      "timestamp": "2026-02-23T10:15:10Z",
      "level": "INFO",
      "source": "Phase 5 - Typesetting",
      "message": "Rendering LaTeX PDF Document..."
    }
  ],
  "next_cursor": "eyJ0aW1lc3RhbXAiOiAiMjAyNi0wMi0ye"
}
```

---

## 4. Download Contract (`GET /api/v1/jobs/{job_id}/download`)

**Purpose:** Once the `Progress Contract` reports `"status": "completed"`, the frontend displays a "Download PDF" button that hits this endpoint.

**Response Format:** `application/pdf`

- **Headers:**
  - `Content-Type: application/pdf`
  - `Content-Disposition: attachment; filename="BookEducate_Final.pdf"`
- **Body:** Boundary binary file data.

---

## 5. Error Contract

**Purpose:** Standardized error catching across all endpoints for terminal failures (e.g., out of memory, complete API Ban).

**Format (Included in Progress SSE or standard JSON responses):**

```json
{
  "status": "failed",
  "job_id": "job_12345abcde",
  "error": {
    "code": "PIPELINE_FATAL_ERROR",
    "phase_failed_in": "Phase 5 - Typesetting",
    "message": "The LaTeX compiler crashed due to extreme memory limitations.",
    "is_recoverable": false
  }
}
```
