
import subprocess
import sys
from pathlib import Path

# Paths
OUTPUT_DIR = Path("data/output")
PRESS_READY_PATH = OUTPUT_DIR / "ready_for_press.md"
HTML_OUTPUT_PATH = OUTPUT_DIR / "BookForge_Final.html"
CSS_PATH = Path("templates/style.css")

def publish_html():
    """
    Compile the press-ready Markdown into a standalone HTML file
    using Pandoc and a custom CSS stylesheet.
    """
    if not PRESS_READY_PATH.exists():
        print(f"❌ Manuscript not found: {PRESS_READY_PATH}")
        return

    if not CSS_PATH.exists():
        print(f"❌ CSS not found: {CSS_PATH}")
        # Create default CSS if missing (fallback)
        CSS_PATH.parent.mkdir(parents=True, exist_ok=True)
        CSS_PATH.write_text("body { font-family: sans-serif; max-width: 800px; margin: auto; padding: 2rem; }")

    cmd = [
        "pandoc",
        str(PRESS_READY_PATH),
        "-o", str(HTML_OUTPUT_PATH),
        "--toc",
        "--standalone",
        "--mathjax",  # For rendering math equations
        "--css", f"../../{CSS_PATH.as_posix()}", # Relative path for HTML linking if needed, or embedding
        "--metadata", f"title=BookForge Generated Book"
    ]

    print(f"🚀 Generating HTML Book: {HTML_OUTPUT_PATH}...")
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Success! Open the file here:\n{HTML_OUTPUT_PATH.absolute()}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating HTML: {e}")
    except FileNotFoundError:
        print("❌ Pandoc not found. Please install Pandoc.")

if __name__ == "__main__":
    publish_html()
