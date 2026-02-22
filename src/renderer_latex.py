
import json
import re
from typing import Dict, List, Any


def escape_latex(text: str) -> str:
    """
    Escapes LaTeX special characters in normal text.
    NOTE: We intentionally do NOT escape { and } because the text may 
    contain legitimate LaTeX commands (e.g. \frac{a}{b}).
    """
    if not text: return ""
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    escaped = "".join(replacements.get(c, c) for c in text)
    # Neutralize rogue list items that the LLM hallucinated outside of list environments
    escaped = escaped.replace(r'\item', r'\textbullet{} ')
    return escaped

def auto_balance_braces(text: str) -> str:
    """
    Ensures that curly braces {} are balanced. If the LLM generated an unclosed 
    bracket inside a block (e.g. `\text{`), this appends `}` to prevent Emergency Stops.
    If it generated an extra closing brace, this prepends `{` to prevent fatal group errors.
    """
    if not text: return ""
    open_braces = text.count('{') - text.count(r'\{')
    close_braces = text.count('}') - text.count(r'\}')
    net_braces = open_braces - close_braces
    if net_braces > 0:
        return text + "}" * net_braces
    elif net_braces < 0:
        return "{" * (-net_braces) + text
    return text

def render_mixed_content_latex(text: str) -> str:
    r"""
    Splits text by $$ ... $$, $ ... $, \[ ... \], \( ... \), and \begin{math_env} ... \end{math_env} blocks.
    - Text parts are escaped.
    - Math parts are kept as is (or wrapped appropriately).
    """
    if not text: return ""
    
    envs = r'equation|equation\*|align|align\*|eqnarray|eqnarray\*|cases|pmatrix|bmatrix|vmatrix|math|displaymath'
    pattern = rf'(\$\$.*?\$\$|\$.*?\$|\\\[.*?\\\]|\\\(.*?\\\)|\\begin\{{(?:{envs})\}}[\s\S]*?\\end\{{(?:{envs})\}})'
    parts = re.split(pattern, text, flags=re.DOTALL)
    latex_out = []
    
    for part in parts:
        if not part: continue
        
        if part.startswith('$$') and part.endswith('$$'):
            # Display math: $$ ... $$
            math_content = part[2:-2].strip()
            latex_out.append(f"\\[ {math_content} \\]")
        elif part.startswith('$') and part.endswith('$'):
            # Inline math: $ ... $
            math_content = part[1:-1].strip()
            latex_out.append(f"\\( {math_content} \\)")
        elif part.startswith(r'\[') and part.endswith(r'\]'):
            # Display math: \[ ... \]
            math_content = part[2:-2].strip()
            latex_out.append(f"\\[ {math_content} \\]")
        elif part.startswith(r'\(') and part.endswith(r'\)'):
            # Inline math: \( ... \)
            math_content = part[2:-2].strip()
            latex_out.append(f"\\( {math_content} \\)")
        elif part.startswith(r'\begin{'):
            # Raw LaTeX math environment inside paragraph -> Pass through untouched
            latex_out.append(part)
        else:
            if part.strip():
                # Text node -> Escape it
                escaped = escape_latex(part)
                # Neutralize stray math delimiters that would otherwise force LaTeX into math mode and crash
                escaped = escaped.replace(r'\(', '( ').replace(r'\)', ' )')
                escaped = escaped.replace(r'\[', '[ ').replace(r'\]', ' ]')
                latex_out.append(escaped)
            else:
                # Preserve whitespace if strictly needed
                if part:
                    latex_out.append(" ")

    return "".join(latex_out)


def render_paragraph_with_images(text: str) -> str:
    """
    Detects markdown image syntax `![alt](path)` inside a paragraph and
    converts it to LaTeX figure environments, preserving surrounding text.

    This ensures images from the Art Department render correctly in LaTeX.
    """
    image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    out: List[str] = []
    last_end = 0

    for match in image_pattern.finditer(text):
        # Text before the image
        before = text[last_end:match.start()]
        if before.strip():
            out.append(escape_latex(before) + "\n\n")

        alt = match.group(1).strip()
        path = match.group(2).strip().replace("\\", "/")

        # Normalize path for LaTeX: strip leading /data/output/ if present
        path = re.sub(r"^/data/output/", "", path)

        caption = escape_latex(alt) if alt else ""

        figure_latex = (
            "\\begin{figure}[h]\n"
            "\\centering\n"
            f"\\includegraphics[width=0.9\\textwidth]{{{path}}}\n"
            f"\\caption{{{caption}}}\n"
            "\\end{figure}\n"
        )
        out.append(figure_latex)

        last_end = match.end()

    # Any remaining text after the last image
    after = text[last_end:]
    if after.strip():
        out.append(escape_latex(after) + "\n\n")

    return "".join(out)

def render_section_latex(section: Dict[str, Any]) -> str:
    """
    Renders a single structure block into LaTeX.
    """
    if not section: return ""
    stype = section.get("type")
    
    if stype == "heading":
        level = section.get("level", 1)
        text = auto_balance_braces(render_mixed_content_latex(section.get("text", "")))
        if level == 1:
            return f"\\chapter{{{text}}}\n"
        elif level == 2:
            return f"\\section{{{text}}}\n"
        elif level == 3:
            return f"\\subsection{{{text}}}\n"
        elif level >= 4:
            return f"\\subsubsection{{{text}}}\n"
    
    elif stype == "paragraph":
        text = section.get("text", "")
        if "![" in text and "](" in text:
            rendered = render_paragraph_with_images(text)
            return auto_balance_braces(rendered) + "\n\n"
        
        text = auto_balance_braces(render_mixed_content_latex(text))
        return f"{text}\n\n"
    
    elif stype == "equation":
        latex = auto_balance_braces(section.get("latex", ""))
        return f"\\begin{{equation}}\n{latex}\n\\end{{equation}}\n"
    
    elif stype == "example_problem":
        title = auto_balance_braces(escape_latex(section.get("title", "Example Problem")))
        prob_stmt = auto_balance_braces(render_mixed_content_latex(section.get("problem_statement", "")))
        steps = section.get("solution_steps") or []
        # Clean up repetitive prefix if the LLM auto-generated it
        if prob_stmt.lower().startswith("problem statement:"):
            prob_stmt = prob_stmt[18:].strip()
            
        # Using standard breakable environment defined in template
        latex = [
            f"\\begin{{exampleproblem}}[{title}]",
            f"\\textbf{{Problem Statement:}} {prob_stmt}",
            "",
            "\\begin{solution}"
        ]
        
        for step in steps:
            for block in step:
                # blocks inside steps are just paragraphs or equations
                btype = block.get("type")
                if btype == "paragraph":
                    latex.append(auto_balance_braces(render_mixed_content_latex(block.get("text", ""))))
                elif btype == "equation":
                    eq_latex = auto_balance_braces(block.get("latex", ""))
                    latex.append(f"\\begin{{equation}}\n{eq_latex}\n\\end{{equation}}")
        
        latex.append("\\end{solution}")
        latex.append("\\end{exampleproblem}\n")
        return "\n".join(latex)
    
    elif stype == "list":
        items = section.get("items") or []
        latex = ["\\begin{itemize}"]
        for item in items:
            item_text = auto_balance_braces(render_mixed_content_latex(item))
            latex.append(f"  \\item {item_text}")
        latex.append("\\end{itemize}\n")
        return "\n".join(latex)

    return ""

def render_page_latex(chapter_structure: Dict[str, Any]) -> str:
    """
    Renders a full chapter from JSON structure to LaTeX body.
    """
    sections = chapter_structure.get("sections") or []
    if not sections: return ""
    
    latex_parts = []
    
    # Optional: If the top level struct has a title, maybe it's the chapter title?
    # Logic in stricturer puts headings inside 'sections'.
    # But usually 'full_structure' has 'type': 'chapter'
    
    # We just iterate
    for section in sections:
        latex_parts.append(render_section_latex(section))
        
    return "\n".join(latex_parts)
