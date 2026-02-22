import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).parent))

from src.renderer_latex import render_page_latex

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "data" / "output"
JSON_PATH = OUTPUT_DIR / "book_structure.json"

def main():
    print("🚀 BookForge PDF Recovery Recompiler")
    print("====================================")
    
    if not JSON_PATH.exists():
        print(f"❌ Could not find {JSON_PATH}. Are you sure Phase 4 finished?")
        return

    print("📄 Loading existing book_structure.json...")
    full_structure = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    print("🧩 Rendering LaTeX code (with new brace-balancing and greek logic)...")
    latex_parts = []
    for chapter in full_structure.get("sections", []):
        try:
            latex_parts.append(render_page_latex(chapter))
        except Exception as e:
            print(f"   ⚠️ LaTeX render error: {e} — skipping chapter")

    tex_out = OUTPUT_DIR / "BookEducate.tex"
    template_path = BASE_DIR / "templates" / "bookeducate.latex"
    
    if not template_path.exists():
        print(f"❌ LaTeX Template not found at {template_path}")
        return

    template_content = template_path.read_text(encoding="utf-8")

    # Clean Pandoc conditionals from template
    template_content = re.sub(r'\$if\(.*?\)\$.*?\$endif\$', '', template_content, flags=re.DOTALL)
    template_content = re.sub(r'\$for\(.*?\)\$.*?\$endfor\$', '', template_content, flags=re.DOTALL)

    latex_body = "\n".join(latex_parts)

    # Auto-balance braces to prevent Emergency Stops
    open_braces = latex_body.count('{') - latex_body.count(r'\{')
    close_braces = latex_body.count('}') - latex_body.count(r'\}')
    net_braces = open_braces - close_braces
    if net_braces > 0:
        print(f"   ⚠️ Auto-balancing: inserting {net_braces} missing closing braces.")
        latex_body += "}\n" * net_braces
    elif net_braces < 0:
        print(f"   ⚠️ Auto-balancing: inserting {-net_braces} missing opening braces.")
        latex_body = "{" * (-net_braces) + latex_body

    # Clean stray \n or \t incorrectly output by the LLM as text
    def fix_n_command(match):
        cmd = match.group(1)
        valid = ['nu', 'nabla', 'nearrow', 'neg', 'newline', 'newpage', 'ni', 'nocite', 'noindent', 'nolimits', 'nonumber', 'nopagebreak', 'normalfont', 'normalsize', 'not', 'notin']
        return '\\' + cmd if cmd in valid else '\n' + cmd[1:]
    
    def fix_t_command(match):
        cmd = match.group(1)
        valid = ['tau', 'text', 'textbf', 'textit', 'texttt', 'theta', 'times', 'tilde', 'tan', 'top', 'triangle', 'to', 'today', 'tag', 'textwidth', 'textheight', 'tfrac', 'thickapprox', 'thicksim', 'textasciicircum', 'textasciitilde']
        return '\\' + cmd if cmd in valid else ' ' + cmd[1:]

    latex_body = re.sub(r'\\(n[a-zA-Z]*)', fix_n_command, latex_body)
    latex_body = re.sub(r'\\(t[a-zA-Z]*)', fix_t_command, latex_body)

    # Fix math commands illegally nested inside \text{} (e.g. \text{J/(kg\cdot K)})
    def fix_math_in_text(match):
        inner = match.group(1)
        math_symbols = ['cdot', 'times', 'Delta', 'Omega', 'Sigma', 'pi', 'mu', 'alpha', 'beta', 'gamma', 'theta']
        for sym in math_symbols:
            # Prevent double replacing if already wrapped
            inner = inner.replace('$\\' + sym + '$', '\\' + sym)
            inner = inner.replace('\\' + sym, '$\\' + sym + '$')
        return '\\text{' + inner + '}'

    latex_body = re.sub(r'\\text\{([^{}]+)\}', fix_math_in_text, latex_body)
    
    # Strip any LaTeX macros that got cut off right before an end block (e.g. \c \n \end{equation})
    latex_body = re.sub(r'\\[a-zA-Z]+\s*\n\s*\\end\{', '\n\\\\end{', latex_body)

    full_latex = template_content.replace("$body$", latex_body)
    full_latex = full_latex.replace("$title$", "BookEducate Book")
    full_latex = full_latex.replace("$author$", "BookEducate Engine")
    full_latex = full_latex.replace("$date$", "\\today")
    full_latex = re.sub(r'\$[a-zA-Z_-]+\$', '', full_latex)

    tex_out.write_text(full_latex, encoding="utf-8")
    print(f"✅ LaTeX Generated: {tex_out}")

    print("\n📕 Compiling PDF with xelatex (Pass 1/3 - Building TOC)...")
    try:
        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-output-directory", str(OUTPUT_DIR), str(tex_out)],
            check=False,
            stdout=subprocess.DEVNULL, # Hide massive output to keep terminal clean
            stderr=subprocess.STDOUT
        )
        print("📕 Compiling PDF with xelatex (Pass 2/3 - Aligning Pages)...")
        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-output-directory", str(OUTPUT_DIR), str(tex_out)],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )
        print("📕 Compiling PDF with xelatex (Pass 3/3 - Finalizing Index & Math)...")
        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-output-directory", str(OUTPUT_DIR), str(tex_out)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )
        print("\n🎉 RECOVERY COMPLETE! Your repaired BookEducate.pdf is ready in data/output/")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ LaTeX compilation failed. Check {OUTPUT_DIR / 'BookEducate.log'} for details.")

if __name__ == "__main__":
    main()
