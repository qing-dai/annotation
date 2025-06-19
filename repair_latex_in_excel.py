#!/usr/bin/env python3
import re
import pandas as pd

IN  = "high_confidence_for_annotation.xlsx"
OUT = "high_confidence_for_annotation_latex_fixed.xlsx"

# def repair_latex(s: str) -> str:
#     # 1) back-slash any common LaTeX words
#     for cmd in ("lambda","gamma","vartheta","Delta","theta",
#                 "frac","propto","in","mathbb"):
#         s = re.sub(rf"\b{cmd}\b", rf"\\{cmd}", s)
#     # 2) collapse stray spaces in subscripts & superscripts
#     s = re.sub(r"_\s*\{\s*([^}]+)\s*\}", r"_{\1}", s)
#     s = re.sub(r"\^\s*\{\s*([^}]+)\s*\}", r"^{\1}", s)
#     # 3) tighten up parentheses
#     s = re.sub(r"\\left\(\s*(.*?)\s*\\right\)", r"\\left(\1\\right)", s)
#     # 4) remove any stray double-slashes
#     s = s.replace("\\\\", "\\")
#     # 5) wrap in display-mode if not already
#     if not s.strip().startswith("$$"):
#         s = "$$" + s.strip() + "$$"
#     return s



def repair_latex(s: str) -> str:
    # 1) Remove any stray \displaystyle
    s = re.sub(r'\\displaystyle', '', s)

    # 2) Split narrative vs math blocks
    parts = re.split(r'(\$\$.*?\$\$)', s, flags=re.DOTALL)
    out = []

    for part in parts:
        if part.startswith('$$') and part.endswith('$$'):
            # ---- we’re in a math block ----
            mb = part.strip('$')       # drop all leading/trailing $
            mb = mb.strip()

            # 2a) Handle array → align*
            #    pull out the array content
            arr = re.search(r'\\begin\{array\}\{r c l\}(.+?)\\end\{array\}', mb, flags=re.DOTALL)
            if arr:
                body = arr.group(1).strip()
                # split the two lines on \\ 
                lines = [ln.strip() for ln in body.split(r'\\') if ln.strip()]
                # collapse spaces around tokens in each line
                def clean_line(ln):
                    ln = re.sub(r'\s*([=+,-])\s*', r'\1', ln)
                    ln = re.sub(r'_\s*\{\s*([^}]+)\}', r'_{\1}', ln)
                    ln = re.sub(r'\^\s*\{\s*([^}]+)\}', r'^{\1}', ln)
                    return ln
                lines = [clean_line(ln) for ln in lines]
                # join into an align* environment
                mb = r'\begin{align*}' + r' \\ '.join(lines) + r'\end{align*}'
            else:
                # 2b) Not an array: just collapse common spaces
                mb = re.sub(r'\s+', ' ', mb).strip()

            # 2c) ensure leading backslashes on commands
            for cmd in ("lambda","gamma","vartheta","Delta","theta","frac","propto","in","mathbb","alpha","beta"):
                mb = re.sub(rf'(?<!\\)\b{cmd}\b', rf'\\{cmd}', mb)

            # 3) wrap clean math back in $$…$$
            out.append(f'$$ {mb} $$')

        else:
            # ---- narrative or empty ----
            out.append(part)

    return ''.join(out)



df = pd.read_excel(IN, dtype=str)
df["chunk_text"] = df["chunk_text"].fillna("").map(repair_latex)
df.to_excel(OUT, index=False)
print(f"✅ Wrote repaired chunks to {OUT}")

# example run
# chunk = """$$ \\lambda _{n } = \\frac { \\lambda _{u } } { 2 n \\gamma ^{2 } } 
# \\left(1 + \\frac { K ^{2 } } { 2 } \\right) , $$ while ... 
# $\\begin{array}{r}{ \\Delta \\theta \\propto \\frac{1}{L} }\\end{array}$ ."""
# chunk = """$$ After the emission of a photon, the action of our single electron is $$ 
# \\begin{array} { r c l } { { J _ { y } ^ { \\prime } } } & { { = } } & { { \\displaystyle \\frac { 1 } { 2 } 
# \\gamma _ { y } y ^ { 2 } + \\alpha _ { y } y p _ { y } \\left( 1 - \\frac { d p } { P _ { 0 } } \\right) + \\frac { 1 } { 2 } \\beta _ { y } p _ { y } ^ { 2 } \\left( 1 - \\frac { d p } { P _ { 0 } } \\right) ^ { 2 } } } \\\\ { { } } & { { } } & { { } } \\\\ { { } } & { { = } } & { { \\displaystyle \\frac { 1 } { 2 } \\gamma _ { y } y ^ { 2 } + \\alpha _ { y } y p _ { y } - \\alpha _ { y } y p _ { y } \\frac { d p } { P _ { 0 } } + \\frac { 1 } { 2 } \\beta _ { y } p _ { y } ^ { 2 } - 2 \\cdot \\frac { 1 } { 2 } \\beta _ { y } p _ { y } ^ { 2 } \\frac { d p } { P _ { 0 } } + \\frac { 1 } { 2 } \\beta p _ { y } ^ { 2 } \\left( \\frac { d p } { P _ { 0 } } \\right) ^ { 2 } . } } \\end{array}
# """
# print(repair_latex(chunk))