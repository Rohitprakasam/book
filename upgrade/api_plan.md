# BookEducate 5.0 — Multi-Model API Rate Strategy

Based on the Google Image Generation limitations provided, generating a massive 600-page textbook (which could easily request over 150-200 images/diagrams) requires a strict load-balancing and fallback strategy.

We cannot use a single high-end model for everything, otherwise the generation will hard-crash midway through Phase 3 when it exhausts the daily quota (RPD).

## 📊 Summary of Rate Limits Analyzed

| Model                                              | RPM (Minute) | RPD (Daily) | Quality / Technical | Role Assignment                       |
| :------------------------------------------------- | :----------: | :---------: | :------------------ | :------------------------------------ |
| **Nano Banana** (`gemini-2.5-flash-image`)         |     500      |  **2,000**  | Standard 1024px     | **The Workhorse (Fallback / Volume)** |
| **Nano Banana Pro** (`gemini-3-pro-image-preview`) |      20      |     250     | High (4K, Search)   | **Primary Technical Diagrammer**      |
| **Imagen 4 Generate**                              |      10      |     70      | High (2K)           | **Secondary Technical**               |
| **Imagen 4 Fast**                                  |      10      |     70      | Good (2K)           | **Tertiary Fallback**                 |
| **Imagen 4 Ultra**                                 |      5       |     30      | Extreme             | **Do Not Use** (Limit too low)        |

---

## 🏗️ Model Routing & Fallback Plan

We will implement this routing logic into `src/resolver.py` (Phase 3: The Art Department) so the engine seamlessly downshifts to cheaper models as limits are reached, ensuring the book finishes 100% of the time.

### 1. High-Priority Technical Diagramming (First 250 Images)

For complex engineering diagrams, we need the highest technical accuracy. The engine will **first attempt** to generate the image using:

1. **Model:** `gemini-3-pro-image-preview` (Nano Banana Pro)
2. **Why:** It has an excellent balance of technical quality (4K) and a reasonably high limit (250 RPD / 20 RPM).
3. **Behavior:** The engine will sleep briefly to respect the 20 Requests Per Minute ceiling.

### 2. Secondary High-Quality Spillover

If Nano Banana Pro hits its 250 RPD limit (or throws a transient 429 error), the engine will immediately trigger the first fallback.

1. **Model:** `imagen-4.0-generate-001`
2. **Limit:** 70 RPD / 10 RPM.
3. **Why:** Still offers excellent 2K technical diagrams.

### 3. Infinite Volume Fallback (The 2,000 RPD Savior)

Once the premium models have exhausted their quotas (~320 images total), or if the pipeline needs to execute highly rapid continuous generations without worrying about minute-by-minute rate locks, the engine activates the ultimate fallback.

1. **Model:** `gemini-2.5-flash-image` (Nano Banana)
2. **Limit:** 2,000 RPD / 500 RPM.
3. **Why:** With 500 Requests Per Minute, "rate limiting" effectively disappears. It can generate standard 1024px images endlessly. The technical quality is slightly lower than Pro, but it guarantees the 600-page book will ALWAYS finish without crashing or leaving blank image holes.

---

## ⚙️ How to Update `.env` for this Strategy

When we wire up the backend, your `IMAGE_MODEL` variables in the `.env` file should be configured in this exact priority order so the Python `try/except` fallback loop cascades correctly down the quality ladder:

```env
# Phase 3 Art Department priority routing
IMAGE_MODEL=gemini-3-pro-image-preview
IMAGE_MODEL_FALLBACKS=imagen-4.0-generate-001,imagen-4.0-fast-generate-001,gemini-2.5-flash-image
```

Using this architecture, the Engine will always attempt to give you the most detailed 4K technical diagrams possible, but will mathematically never fail to generate a book because the 2,000-RPD Nano Banana acts as the ultimate safety net.
