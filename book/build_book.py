#!/usr/bin/env python3
"""Build the Operation Architeuthis dossier as a typeset book.

Reads the nine deliverables from the repository root and produces:
  book/Operation-Architeuthis-Dossier.pdf   (via WeasyPrint)
  book/Operation-Architeuthis-Dossier.docx  (via LibreOffice, from a Word-friendly HTML variant)

Usage:  python3 book/build_book.py [--format pdf|docx|all]
Deps :  pip install weasyprint markdown   ·   LibreOffice (soffice) for the .docx
"""
import argparse, csv, html, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
BASENAME = "Operation-Architeuthis-Dossier"
DATE = "August 30, 2026"

MD_EXT = ["tables", "smarty", "sane_lists"]

BADGES = [
    ("✅", "badge-v", "VERIFIED"),
    ("🔶", "badge-c", "FIRST-CLAIMED"),
    ("⚠️", "badge-d", "DISPUTED"),
    ("⚠", "badge-d", "DISPUTED"),
]

def render_md(path, demote=1):
    """Markdown file -> HTML: drop its own H1, swap emoji for badges, demote headings."""
    import markdown as md
    text = open(os.path.join(REPO, path), encoding="utf-8").read()
    text = re.sub(r"^# .*\n", "", text, count=1)
    for emoji, cls, label in BADGES:
        text = text.replace(emoji, f'<span class="badge {cls}">{label}</span>')
    out = md.markdown(text, extensions=MD_EXT)
    for lvl in range(6 - demote, 0, -1):
        out = out.replace(f"<h{lvl}>", f"<h{lvl+demote}>").replace(f"</h{lvl}>", f"</h{lvl+demote}>")
    return out

CATEGORY_NAMES = {
    "A": "A — direct observation of living animals",
    "B": "B — physical specimen evidence",
    "C": "C — indirect evidence",
    "D": "D — informed inference",
    "E": "E — speculation / anecdote",
}
PREFIX_SECTIONS = [
    ("LIV", "Live Observation and Imaging"),
    ("SPE", "Specimens and Size"),
    ("TAX", "Taxonomy, Genetics, and Distribution"),
    ("DEP", "Depth, Habitat, and Physiology"),
    ("DIE", "Diet, Hunting, and Predators"),
    ("REP", "Reproduction, Growth, and Lifespan"),
    ("SWH", "Sperm Whale Interactions"),
    ("MYT", "Myths, History, and Misidentifications"),
]

def render_ledger():
    rows = list(csv.DictReader(open(os.path.join(REPO, "evidence-ledger.csv"), encoding="utf-8")))
    by_prefix = {}
    for r in rows:
        by_prefix.setdefault(r["claim_id"].split("-")[0], []).append(r)
    parts = []
    for prefix, title in PREFIX_SECTIONS:
        parts.append(f"<h2>{html.escape(title)} ({prefix})</h2>")
        for r in by_prefix.get(prefix, []):
            cat = CATEGORY_NAMES.get(r["evidence_category"].strip(), r["evidence_category"])
            head = (f'<b>{html.escape(r["claim_id"])}</b>'
                    f' &nbsp;·&nbsp; Category {html.escape(cat)}'
                    f' &nbsp;·&nbsp; confidence: {html.escape(r["confidence"])}'
                    f' &nbsp;·&nbsp; {html.escape(r["direct_or_inferred"] or "—")}')
            meta = (f'<b>Source:</b> {html.escape(r["source"])} ({html.escape(r["publication_year"])}; '
                    f'{html.escape(r["source_type"])}). '
                    f'<b>Limitations:</b> {html.escape(r["limitations"])} '
                    f'<b>Identifier:</b> {html.escape(r["citation_or_identifier"])}')
            parts.append(
                f'<div class="claim"><div class="claim-head">{head}</div>'
                f'<p class="claim-text">{html.escape(r["claim"])}</p>'
                f'<p class="claim-meta">{meta}</p></div>')
    return "\n".join(parts), len(rows)

def chapters():
    ledger_html, n = render_ledger()
    return [
        ("about",    "About This Document",                 render_md("README.md")),
        ("exec",     "Executive Summary",                   render_md("executive-summary.md")),
        ("dossier",  "The Full Dossier: Twelve Questions",  render_md("full-dossier.md")),
        ("timeline", "Observation Timeline, 1639–2026",     render_md("observation-timeline.md")),
        ("myths",    "Myths and Evidence",                  render_md("myths-and-evidence.md")),
        ("open",     "Unresolved Questions",                render_md("unresolved-questions.md")),
        ("biblio",   "Annotated Bibliography",              render_md("annotated-bibliography.md")),
        ("audit",    "Source Quality Audit",                render_md("source-quality-audit.md")),
        ("ledger",   f"Appendix A — The Evidence Ledger ({n} Claims)", ledger_html),
    ]

SUBTITLE = ("An evidence audit of <i>Architeuthis dux</i> — what humanity knows, "
            "how it knows it, and what remains unresolved.")
BLURB = ("A source-grounded literature review built on a 251-claim evidence ledger, "
         "196 independent citation checks, and a strict separation of direct observation, "
         "specimen evidence, inference, and myth.")
FOOT = (f"Compiled {DATE} · Literature review and evidence audit — no original biological theory proposed<br>"
        "Evidence categories: A direct observation · B physical specimen · C indirect · "
        "D informed inference · E speculation/anecdote")

PDF_CSS = """
@page { size: A4; margin: 22mm 19mm 20mm 19mm;
  @top-center { content: "OPERATION ARCHITEUTHIS · AN EVIDENCE AUDIT OF THE GIANT SQUID";
                font-family: "DejaVu Sans"; font-size: 6.5pt; letter-spacing: 1.2px; color: #8a8a8a; }
  @bottom-center { content: counter(page); font-family: "DejaVu Sans"; font-size: 8pt; color: #666; } }
@page cover { margin: 0; @top-center { content: none; } @bottom-center { content: none; } }
@page toc   { @top-center { content: none; } }
html { font-family: "DejaVu Serif", serif; font-size: 9.6pt; line-height: 1.45; color: #1c1c1c; }
body { margin: 0; }
.cover { page: cover; height: 297mm; background: #0b1d2a; color: #e9eef2;
         display: flex; flex-direction: column; justify-content: space-between; }
.cover-inner { padding: 34mm 26mm 0 26mm; }
.cover .kicker { font-family: "DejaVu Sans"; font-size: 10pt; letter-spacing: 4px; color: #7fb2c9; }
.cover h1 { font-family: "DejaVu Sans"; font-weight: bold; font-size: 33pt; line-height: 1.12;
            margin: 10mm 0 6mm 0; color: #ffffff; border: none; }
.cover .subtitle { font-size: 13pt; color: #c7d5dd; line-height: 1.5; max-width: 140mm; }
.cover .rule { width: 42mm; height: 1.2mm; background: #7fb2c9; margin: 10mm 0; }
.cover .foot { padding: 0 26mm 24mm 26mm; font-family: "DejaVu Sans"; font-size: 8.5pt;
               color: #9db4c0; line-height: 1.7; }
.toc { page: toc; page-break-before: always; }
.toc h1 { border: none; }
.toc ul { list-style: none; padding: 0; margin: 6mm 0; }
.toc li { margin: 0 0 3.4mm 0; font-family: "DejaVu Sans"; font-size: 10.5pt; }
.toc a { text-decoration: none; color: #1c1c1c; display: block; }
.toc a::after { content: leader('.') " " target-counter(attr(href), page); }
.chapter { page-break-before: always; }
h1 { font-family: "DejaVu Sans"; font-size: 19pt; line-height: 1.2; margin: 0 0 7mm 0;
     padding-bottom: 3mm; border-bottom: 1.6pt solid #0b1d2a; color: #0b1d2a; }
h2 { font-family: "DejaVu Sans"; font-size: 12.5pt; color: #0b1d2a; margin: 7mm 0 2.5mm 0; }
h3 { font-family: "DejaVu Sans"; font-size: 10.5pt; color: #23455c; margin: 5mm 0 2mm 0; }
p  { margin: 0 0 2.6mm 0; text-align: justify; hyphens: auto; }
li { margin: 0 0 1.6mm 0; }
ul, ol { margin: 0 0 2.8mm 0; padding-left: 5.5mm; }
hr { border: none; border-top: 0.5pt solid #bbb; margin: 5mm 0; }
code { font-family: "DejaVu Sans Mono"; font-size: 7.6pt; background: #f1f4f6;
       padding: 0 1.5pt; border-radius: 2pt; }
a { color: #1c4966; text-decoration: none; }
table { border-collapse: collapse; width: 100%; margin: 3mm 0 4mm 0; font-size: 8.4pt; }
th { font-family: "DejaVu Sans"; font-size: 7.6pt; text-align: left; background: #0b1d2a;
     color: #fff; padding: 1.6mm 2mm; }
td { padding: 1.5mm 2mm; border-bottom: 0.4pt solid #ccd4d9; vertical-align: top; }
tr { page-break-inside: avoid; }
.badge { font-family: "DejaVu Sans"; font-size: 6.4pt; font-weight: bold; letter-spacing: 0.4px;
         padding: 0.4mm 1.4mm; border-radius: 2pt; white-space: nowrap; }
.badge-v { background: #e2f2e4; color: #1c6b2a; }
.badge-c { background: #fdf0d7; color: #8a6206; }
.badge-d { background: #fbe3e0; color: #a03325; }
.claim { page-break-inside: avoid; margin: 0 0 3.4mm 0; padding: 2.2mm 2.8mm;
         background: #f7f9fa; border-left: 2.4pt solid #23455c; }
.claim-head { font-family: "DejaVu Sans"; font-size: 7.2pt; color: #23455c; margin-bottom: 1.2mm; }
.claim-text { font-size: 8.2pt; margin: 0 0 1.2mm 0; }
.claim-meta { font-size: 7.2pt; color: #555; margin: 0; text-align: left; }
"""

# Word-friendly variant: standard font names, no @page tricks, explicit page breaks.
DOCX_CSS = """
body { font-family: Georgia, serif; font-size: 10pt; line-height: 1.4; color: #1c1c1c; }
h1 { font-family: Calibri, Arial, sans-serif; font-size: 20pt; color: #0b1d2a;
     border-bottom: 2px solid #0b1d2a; padding-bottom: 4px; }
h2 { font-family: Calibri, Arial, sans-serif; font-size: 14pt; color: #0b1d2a; }
h3 { font-family: Calibri, Arial, sans-serif; font-size: 11.5pt; color: #23455c; }
p { margin: 0 0 8px 0; }
code { font-family: "Courier New", monospace; font-size: 8.5pt; color: #23455c; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; }
th { background: #0b1d2a; color: #ffffff; text-align: left; padding: 4px 6px;
     font-family: Calibri, Arial, sans-serif; font-size: 8.5pt; }
td { border-bottom: 1px solid #ccd4d9; padding: 4px 6px; vertical-align: top; }
.badge { font-family: Calibri, Arial, sans-serif; font-size: 7.5pt; font-weight: bold; }
.badge-v { color: #1c6b2a; } .badge-c { color: #8a6206; } .badge-d { color: #a03325; }
.claim { margin: 0 0 10px 0; padding: 6px 8px; background: #f2f5f7; }
.claim-head { font-family: Calibri, Arial, sans-serif; font-size: 8pt; color: #23455c; }
.claim-text { font-size: 9pt; margin: 3px 0; }
.claim-meta { font-size: 8pt; color: #555555; margin: 0; }
.cover-title { font-family: Calibri, Arial, sans-serif; font-size: 34pt; font-weight: bold;
               color: #0b1d2a; margin: 90px 0 10px 0; border: none; }
.cover-kicker { font-family: Calibri, Arial, sans-serif; font-size: 11pt; letter-spacing: 3px;
                color: #23455c; }
.cover-sub { font-size: 13pt; color: #333333; }
.cover-foot { font-size: 9pt; color: #666666; }
"""

def build_pdf(chs, out):
    from weasyprint import HTML
    toc = "\n".join(f'<li><a href="#ch-{cid}">{html.escape(t)}</a></li>' for cid, t, _ in chs)
    body = "\n".join(f'<section class="chapter" id="ch-{cid}"><h1>{html.escape(t)}</h1>\n{b}\n</section>'
                     for cid, t, b in chs)
    doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Operation Architeuthis</title><style>{PDF_CSS}</style></head><body>
<div class="cover"><div class="cover-inner">
  <div class="kicker">OPERATION ARCHITEUTHIS</div><h1>The Giant Squid</h1>
  <div class="subtitle">{SUBTITLE}</div><div class="rule"></div>
  <div class="subtitle" style="font-size:10pt;">{BLURB}</div></div>
  <div class="foot">{FOOT}</div></div>
<section class="toc"><h1>Contents</h1><ul>{toc}</ul>
<p style="font-family:'DejaVu Sans';font-size:8pt;color:#666;">In-text codes such as
<code>[LIV-01]</code> point to entries in Appendix A, the evidence ledger. References in the text to
project file names (e.g. <code>evidence-ledger.csv</code>) correspond to the chapters of this book.</p>
</section>
{body}</body></html>"""
    HTML(string=doc).write_pdf(out)
    print("wrote", out)

def build_docx(chs, out):
    toc = "\n".join(f"<li>{html.escape(t)}</li>" for _, t, _ in chs)
    body = "\n".join(
        f'<h1 style="page-break-before: always;">{html.escape(t)}</h1>\n{b}'
        for _, t, b in chs)
    doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Operation Architeuthis</title><style>{DOCX_CSS}</style></head><body>
<p class="cover-kicker">OPERATION ARCHITEUTHIS</p>
<p class="cover-title">The Giant Squid</p>
<p class="cover-sub">{SUBTITLE}</p><p class="cover-sub" style="font-size:10.5pt;">{BLURB}</p>
<p class="cover-foot">{FOOT}</p>
<h1 style="page-break-before: always;">Contents</h1><ul>{toc}</ul>
<p style="font-size:9pt;color:#666666;">Tip: for a live table of contents with page numbers, use
References &rarr; Table of Contents in Word — all chapter titles are Heading 1. In-text codes such as
<code>[LIV-01]</code> point to entries in Appendix A, the evidence ledger.</p>
{body}</body></html>"""
    tmp_html = os.path.join(HERE, f"{BASENAME}.tmp.html")
    open(tmp_html, "w", encoding="utf-8").write(doc)
    subprocess.run(["soffice", "--headless", "--convert-to", "docx:MS Word 2007 XML",
                    "--outdir", HERE, tmp_html],
                   check=True, capture_output=True, timeout=300)
    produced = os.path.join(HERE, f"{BASENAME}.tmp.docx")
    os.replace(produced, out)
    os.remove(tmp_html)
    print("wrote", out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--format", choices=["pdf", "docx", "all"], default="all")
    args = ap.parse_args()
    chs = chapters()
    if args.format in ("pdf", "all"):
        build_pdf(chs, os.path.join(HERE, f"{BASENAME}.pdf"))
    if args.format in ("docx", "all"):
        build_docx(chs, os.path.join(HERE, f"{BASENAME}.docx"))
