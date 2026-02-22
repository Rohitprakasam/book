# BookEducate 5.0 — Backend Server Architecture Plan

Currently, BookForge 5.0 is a Command Line Interface (CLI) application run via `python main.py`. To accommodate the external frontend team, we must wrap `main.py` inside an asynchronous web server.

We will use **FastAPI**. It is native to Python, integrates perfectly with LangGraph, and natively supports Server-Sent Events (SSE) and asynchronous background tasks (which are required for a 10-hour generation).

---

## 1. Core Stack

- **Framework:** FastAPI (`pip install fastapi uvicorn`)
- **Streaming Protocol:** `sse-starlette` (for sending Progress & Logs via SSE)
- **Port:** `http://localhost:3030`
- **Concurrency:** `asyncio` and FastAPI `BackgroundTasks`

## 2. Directory Structure Update

We will create a new directory inside BookForge to isolate the server logic from the AI Swarm logic:

```text
bookforge_local/
├── server/
│   ├── api.py           # The FastAPI application & route definitions
│   ├── sse_manager.py   # Handles pub/sub broadcasting for progress bars
│   └── jobs.py          # State dictionary tracking active 10-hour book generations
├── src/
│   └── agents.py        # (The existing AI tools)
└── main.py              # (Will be refactored to be callable by api.py)
```

## 3. Implementation Steps

### Step A: CORS Configuration

The frontend (e.g., `localhost:3000`) will be blocked by the browser if the backend does not explicitly allow it.

```python
# server/api.py
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="BookEducate Engine API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"], # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Step B: The Generation Endpoint

When the frontend uploads the PDF, FastAPI must save the PDF to `/data/input/`, generate a unique `job_id`, and immediately return `202 Accepted` to the frontend **before** starting the 10-hour `main.py` pipeline.

We achieve this using `BackgroundTasks`:

```python
@app.post("/api/v1/generate")
async def start_generation(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    config: str = Form(...)
):
    job_id = generate_unique_id()
    save_upload_to_disk(file, job_id)

    # Start the 10 hour BookForge engine in the background
    background_tasks.add_task(run_bookforge_pipeline, job_id, config)

    return {"status": "processing", "job_id": job_id}
```

### Step C: Server-Sent Events (SSE) for Progress

Because the generation takes 10+ hours, we cannot use a standard HTTP request. We will yield a continuous stream of data chunks using `EventSourceResponse`.

We will modify `src/graph.py` and `src/structurer.py` to `yield` or `publish` status updates to an in-memory Redis or Python Queue. The `/progress` endpoint will consume that queue and stream it to the React frontend component.

### Step D: Capturing Phase 1-6 Terminal Logs

To support the Live Logs Contract, we will intercept Python's standard output (`sys.stdout`) during the 10-hour background task. Every time an agent calls `print()` (from Phase 1 deconstruction all the way to Phase 6 syncing), that text will be captured as a `{ level: "INFO", message: "..."}` object and pushed to a queue for the `/logs` endpoint to stream directly to the frontend loading interface.

### Step E: The Download Router

Once the job state is marked as "completed", the frontend hits `/download` to retrieve the final PDF.

```python
from fastapi.responses import FileResponse

@app.get("/api/v1/jobs/{job_id}/download")
async def download_book(job_id: str):
    pdf_path = f"./data/output/{job_id}_BookEducate.pdf"
    if os.path.exists(pdf_path):
        return FileResponse(path=pdf_path, filename="BookEducate_Final.pdf")
    return {"error": "File not found or not finished."}
```
