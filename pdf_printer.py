
import subprocess
import os
import time
from pathlib import Path

# Config
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
start_time = time.time()

# Paths
OUTPUT_DIR = Path("data/output")
HTML_PATH = OUTPUT_DIR / "BookForge_Final.html"
PDF_PATH = OUTPUT_DIR / "BookForge_Final_Print.pdf"

def print_to_pdf():
    """
    Use Microsoft Edge (Headless) to print HTML to PDF.
    This avoids LaTeX/Pandoc PDF engine issues and is much faster.
    """
    if not HTML_PATH.exists():
        print(f"❌ HTML file not found: {HTML_PATH}")
        print("Run 'publish_html.py' first.")
        return

    # Use absolute paths for the browser
    html_abs = HTML_PATH.resolve()
    pdf_abs = PDF_PATH.resolve()

    print(f"🚀 Converting HTML to PDF via Edge Headless...")
    print(f"   Input:  {html_abs}")
    print(f"   Output: {pdf_abs}")

    # Edge Command Line Arguments for Headless PDF Printing
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={str(pdf_abs)}",
        "--no-pdf-header-footer",  # Clean output
        str(html_abs)
    ]

    try:
        # Run Edge
        subprocess.run(cmd, check=True)
        
        # Verify output
        if PDF_PATH.exists() and PDF_PATH.stat().st_size > 0:
            elapsed = time.time() - start_time
            size_mb = PDF_PATH.stat().st_size / (1024 * 1024)
            print(f"\n✅ Success! PDF Generated in {elapsed:.1f}s")
            print(f"📂 File: {pdf_abs} ({size_mb:.2f} MB)")
        else:
            print("\n❌ PDF file was not created. Edge exited without error but no file appeared.")
            print("Tip: Make sure the output directory is writable and the file isn't open.")

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Edge conversion failed: {e}")
    except FileNotFoundError:
        print(f"\n❌ Microsoft Edge not found at: {EDGE_PATH}")
        print("Please check the path or install Edge.")

if __name__ == "__main__":
    print_to_pdf()
