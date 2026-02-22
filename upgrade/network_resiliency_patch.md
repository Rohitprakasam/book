# BookEducate 5.0 — Network Offline Recovery Patch

> **Purpose:**
> By default, the `litellm` API wrapper attempts a failing connection 3 times before skipping the section and moving on. If your home network drops for 5+ minutes during a 10-hour book generation, entire sections of the PDF will be permanently missing.
>
> This patch replaces those brittle try/catches with an **Infinite 30-Second Ping Loop**. When the WiFi disconnects, the agents will freeze, print `[📡 Internet disconnected. Sleeping 30s...]`, and quietly wait until you restore the connection.

---

## 🟢 Patch 1: The Swarm Agents (`src/agents.py`)

Open `src/agents.py`. There are **three** Litellm calls in here that need to be wrapped.

### 1. Analyst Node (approx. line 146)

Find the `response = litellm.completion(...)` block for the Analyst. Replace the simple `response = ...` with this:

```python
        # INFINITE NETWORK RETRY LOOP
        while True:
            try:
                response = litellm.completion(
                    model=model,
                    timeout=LLM_TIMEOUT,
                    messages=[
                        {"role": "system", "content": ANALYST_SYSTEM_PROMPT.replace(
                            "{BOOK_PERSONA}", os.getenv("BOOK_PERSONA", "Elite Professor specializing in the subject matter")
                        ).replace(
                            "{BOOK_SUBJECT}", os.getenv("BOOK_SUBJECT", "Engineering")
                        ).replace(
                            "{TARGET_CHARS}", str(state.get("target_chars", 8000))
                        )},
                        {
                            "role": "user",
                            "content": f"Here is the chapter text to analyse:\n\n{chunk}",
                        },
                    ],
                    api_key=api_key if model.startswith("gemini/") else None,
                )
                break # Success! Break the infinite loop.
            except litellm.APIConnectionError:
                print(f"[Analyst] 📡 Internet disconnected. Sleeping 30s...")
                time.sleep(30)
            except Exception as other_err:
                if "11001" in str(other_err).lower() or "getaddrinfo" in str(other_err).lower():
                    print(f"[Analyst] 📡 Internet disconnected. Sleeping 30s...")
                    time.sleep(30)
                else:
                    raise # Re-raise real errors (like Rate Limits) to the main try/except
```

### 2. Drafter & Critic Nodes

Repeat the exact same `while True` logic for the `litellm.completion()` calls inside `drafter_node()` and `critic_node()`.

---

## 🟢 Patch 2: The JSON Structurer (`src/structurer.py`)

Open `src/structurer.py`.

Find the `response = litellm.completion(...)` block around line 113. Replace it with this infinite loop:

```python
            # INFINITE NETWORK RETRY LOOP
            while True:
                try:
                    response = litellm.completion(
                        model=model,
                        timeout=300,  # 5 minutes timeout
                        messages=[
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": text_chunk}
                        ],
                        api_key=api_key if model.startswith("gemini/") else None,
                    )
                    break # Success! Break the infinite loop.
                except litellm.APIConnectionError:
                    print(f"[Structurer] 📡 Internet disconnected. Sleeping 30s...")
                    time.sleep(30)
                except Exception as other_err:
                    if "11001" in str(other_err).lower() or "getaddrinfo" in str(other_err).lower():
                        print(f"[Structurer] 📡 Internet disconnected. Sleeping 30s...")
                        time.sleep(30)
                    else:
                        raise # Re-raise real errors (like Rate Limits) to the main try/except
```

---

## 🟢 Patch 3: The PDF Fallback Recovery Script (`recover_json.py`)

Since your _current_ 600-page book had ~20 sections fail (sections 1750-1770) due to an outage before the patch, you can actually repair the `book_structure.json` file instantly WITHOUT running the 10-hour script again.

I've provided the recovery tool logic. Follow these steps:

1. When `main.py` fully finishes building the PDF.
2. Ask the Antigravity Agent: `"Run the JSON recovery to fix the 20 network-dropped fallback chunks from the current generation."`
3. We will write a small script to loop through `book_structure.json`, find the 20 `type: paragraph` chunks, re-run them through the Structurer LLM, save the clean JSON format, and instantly print the repaired PDF using `python main.py --phase 3`.
