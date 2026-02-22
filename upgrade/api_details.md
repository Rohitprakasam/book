# Google Image Generation Models — API Reference

| S/No | Model | Category | RPM | TPM | RPD |
|------|-------|----------|-----|-----|-----|
| 1 | Imagen 4 Fast Generate | Multi-modal generative models | 0 / 10 | N/A | 0 / 70 |
| 2 | Imagen 4 Generate | Multi-modal generative models | 0 / 10 | N/A | 0 / 70 |
| 3 | Imagen 4 Ultra Generate | Multi-modal generative models | 0 / 5 | N/A | 0 / 30 |
| 4 | Nano Banana (Gemini 2.5 Flash Preview Image) | Multi-modal generative models | 0 / 500 | 0 / 500K | 0 / 2K |
| 5 | Nano Banana Pro (Gemini 3 Pro Image) | Multi-modal generative models | 0 / 20 | 0 / 100K | 0 / 250 |

---

## 1. Imagen 4 Fast Generate

> Fastest Imagen variant. Best for high-volume, low-latency pipelines where speed matters more than maximum quality.

```python
from google import genai
from google.genai import types

client = genai.Client()  # Uses GOOGLE_API_KEY env var

response = client.models.generate_images(
    model='imagen-4.0-fast-generate-001',
    prompt='A robot holding a red skateboard, studio lighting',
    config=types.GenerateImagesConfig(
        number_of_images=4,          # 1–4 images per call
        aspect_ratio="1:1",          # "1:1" | "3:4" | "4:3" | "9:16" | "16:9"
        person_generation="allow_adult",  # "dont_allow" | "allow_adult" | "allow_all"
    )
)

for generated_image in response.generated_images:
    generated_image.image.show()  # or .save("output.png")
```

---

## 2. Imagen 4 Generate

> Standard Imagen 4 model. Balanced quality and speed. Supports up to 4 images per call and optional 2K output.

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-generate-001',
    prompt='A minimalist product shot of a perfume bottle, studio lighting, white background',
    config=types.GenerateImagesConfig(
        number_of_images=4,          # 1–4
        aspect_ratio="4:3",          # "1:1" | "3:4" | "4:3" | "9:16" | "16:9"
        image_size="2K",             # "1K" (default) | "2K"
        person_generation="allow_adult",
    )
)

for generated_image in response.generated_images:
    generated_image.image.save("output.png")
```

---

## 3. Imagen 4 Ultra Generate

> Highest quality Imagen model. Only 1 image per call. Use when you need the absolute best output for professional assets.

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-ultra-generate-001',
    prompt='Captivating photo of a woman in her 20s, street photography style, movie still, muted orange warm tones',
    config=types.GenerateImagesConfig(
        number_of_images=1,          # Ultra supports only 1 image per call
        aspect_ratio="9:16",         # "1:1" | "3:4" | "4:3" | "9:16" | "16:9"
        image_size="2K",             # "1K" | "2K"
        person_generation="allow_adult",
    )
)

for generated_image in response.generated_images:
    generated_image.image.save("ultra_output.png")
```

---

## 4. Nano Banana — Gemini 2.5 Flash Preview Image

> Conversational image generation built into Gemini. Fast, efficient, supports image editing with text + image input. Best for high-volume tasks at 1024px resolution.

```python
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# ── Text → Image ──────────────────────────────────────────────
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=["A futuristic city at sunset, cinematic wide angle shot"],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",     # "1:1"|"2:3"|"3:2"|"3:4"|"4:3"|"4:5"|"5:4"|"9:16"|"16:9"|"21:9"
        )
    )
)

for part in response.parts:
    if part.text:
        print(part.text)
    elif part.inline_data:
        part.as_image().save("flash_output.png")


# ── Image + Text → Edited Image ────────────────────────────────
input_image = Image.open("my_photo.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[
        "Add a wizard hat to the subject, keep everything else the same",
        input_image,                 # Pass PIL image directly (works up to 3 input images)
    ],
    config=types.GenerateContentConfig(
        response_modalities=['IMAGE'],  # Image-only response
    )
)

for part in response.parts:
    if part.inline_data:
        part.as_image().save("edited_output.png")
```

---

## 5. Nano Banana Pro — Gemini 3 Pro Image Preview

> Most powerful conversational image model. Supports Thinking mode, Google Search grounding, 4K output, up to 14 reference images, and accurate text rendering. Use for professional asset production.

```python
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# ── Text → Image (High-Res) ────────────────────────────────────
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=["Da Vinci style anatomical sketch of a Monarch butterfly on parchment, detailed notes in English"],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio="1:1",      # "1:1"|"2:3"|"3:2"|"3:4"|"4:3"|"4:5"|"5:4"|"9:16"|"16:9"|"21:9"
            image_size="4K",         # "1K" (default) | "2K" | "4K"  ← must be UPPERCASE
        )
    )
)

for part in response.parts:
    if part.text:
        print(part.text)
    elif part.inline_data:
        part.as_image().save("pro_output.png")


# ── Multi-Turn Conversational Editing ──────────────────────────
chat = client.chats.create(
    model="gemini-3-pro-image-preview",
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
    )
)

response = chat.send_message("Create a logo for a coffee brand called 'Dawn Brew', minimalist style")
for part in response.parts:
    if part.inline_data:
        part.as_image().save("logo_v1.png")

# Model remembers the previous image — just describe the change
response = chat.send_message("Make the colors warmer and add a small coffee cup icon")
for part in response.parts:
    if part.inline_data:
        part.as_image().save("logo_v2.png")


# ── Google Search Grounding (Real-time data → Image) ───────────
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=["Visualize today's weather forecast for London as a clean, modern weather card with outfit suggestions"],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(aspect_ratio="9:16"),
        tools=[{"google_search": {}}]   # Model searches live before generating
    )
)

for part in response.parts:
    if part.inline_data:
        part.as_image().save("weather_card.png")


# ── Multi-Image Input (up to 14 reference images) ──────────────
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[
        "Office group photo of these people making funny faces",
        Image.open("person1.png"),   # Up to 5 person images for character consistency
        Image.open("person2.png"),
        Image.open("person3.png"),
    ],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(aspect_ratio="5:4", image_size="2K")
    )
)

for part in response.parts:
    if part.inline_data:
        part.as_image().save("group_photo.png")
```

---

## Quick Comparison

| Feature | Imagen 4 Fast | Imagen 4 | Imagen 4 Ultra | Nano Banana (Flash) | Nano Banana Pro |
|---------|:---:|:---:|:---:|:---:|:---:|
| Max images/call | 4 | 4 | **1** | 1 | 1 |
| Max resolution | 2K | 2K | 2K | 1024px | **4K** |
| Image editing | ❌ | ❌ | ❌ | ✅ | ✅ |
| Multi-turn chat | ❌ | ❌ | ❌ | ✅ | ✅ |
| Google Search | ❌ | ❌ | ❌ | ❌ | ✅ |
| Thinking mode | ❌ | ❌ | ❌ | ❌ | ✅ |
| Multi-image input | ❌ | ❌ | ❌ | up to 3 | **up to 14** |

> ⚠️ **Note:** Always use uppercase `"1K"`, `"2K"`, `"4K"` — lowercase will be rejected by the API.
> All generated images include a **SynthID watermark**.