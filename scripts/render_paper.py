#!/usr/bin/env python3
"""Render this programme's simple Markdown papers with ReportLab.

No network access. Requires reportlab; PDF verification uses pypdf/pypdfium2
separately. This deliberately supports only the Markdown constructs used here.
"""
import argparse
from html import escape
from pathlib import Path
import re
from urllib.parse import urljoin

import reportlab
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


def inline(text, link_base):
    text = text.replace("—", " - ").replace("–", "-").replace("‑", "-")
    text = escape(text)
    text = re.sub(r"\[([^]]+)\]\(([^)]+)\)",
                  lambda m: f'<link color="#155B78" href="{urljoin(link_base, m[2])}">{m[1]}</link>', text)
    text = re.sub(r"`([^`]+)`", r'<font name="VeraMono" size="8">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r'<b>\1</b>', text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r'<i>\1</i>', text)
    return text


def build(source, destination, link_base):
    reportlab.rl_config.invariant = True
    render_inline = lambda text: inline(text, link_base)
    fonts = Path(reportlab.__file__).parent / "fonts"
    for name, filename in [("Vera", "Vera.ttf"), ("VeraBold", "VeraBd.ttf"),
                           ("VeraItalic", "VeraIt.ttf"), ("VeraMono", "Vera.ttf")]:
        pdfmetrics.registerFont(TTFont(name, str(fonts / filename)))
    pdfmetrics.registerFontFamily("Vera", normal="Vera", bold="VeraBold", italic="VeraItalic", boldItalic="VeraBold")
    body = ParagraphStyle("Body", fontName="Vera", fontSize=9.3, leading=13.5,
                          spaceAfter=7, alignment=TA_LEFT, splitLongWords=True,
                          allowWidows=False, allowOrphans=False)
    styles = {
        1: ParagraphStyle("Title", parent=body, fontName="VeraBold", fontSize=20, leading=25, spaceAfter=11, keepWithNext=True),
        2: ParagraphStyle("Section", parent=body, fontName="VeraBold", fontSize=12, leading=16, spaceBefore=11, spaceAfter=7, keepWithNext=True),
        3: ParagraphStyle("Subsection", parent=body, fontName="VeraBold", fontSize=10.3, leading=14, spaceBefore=8, spaceAfter=5, keepWithNext=True),
    }
    cell = ParagraphStyle("Cell", parent=body, fontSize=8, leading=11, spaceAfter=0)
    story, pending, rows = [], [], []
    width = 6.95 * inch

    def flush_text():
        if pending:
            story.append(Paragraph(render_inline(" ".join(pending)), body))
            pending.clear()

    def flush_table():
        if not rows:
            return
        count = len(rows[0])
        fractions = [0.32, 0.16, 0.14, 0.38] if count == 4 else ([0.28, 0.25, 0.47] if count == 3 else [1 / count] * count)
        data = [[Paragraph(render_inline(c), cell) for c in row] for row in rows]
        table = Table(data, colWidths=[width * f for f in fractions], repeatRows=1, hAlign="LEFT")
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E7EDF1")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LINEBELOW", (0, 0), (-1, 0), 0.7, colors.HexColor("#6C8290")),
            ("LINEBELOW", (0, 1), (-1, -1), 0.3, colors.HexColor("#D6DFE4")),
            ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        story.extend([table, Spacer(1, 8)])
        rows.clear()

    lines = source.read_text(encoding="utf-8").splitlines()
    for line in lines + [""]:
        if line.startswith("|"):
            flush_text()
            parts = [p.strip() for p in line.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-+:?", p.replace(" ", "")) for p in parts):
                rows.append(parts)
            continue
        flush_table()
        if not line.strip():
            flush_text()
        elif (match := re.match(r"^(#{1,3}) (.*)$", line)):
            flush_text()
            story.append(Paragraph(render_inline(match[2]), styles[len(match[1])]))
        elif re.match(r"^\d+\. ", line):
            flush_text()
            story.append(Paragraph(render_inline(line), body))
        else:
            pending.append(line)

    destination.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(destination), pagesize=(8.5 * inch, 11 * inch),
                            leftMargin=.775 * inch, rightMargin=.775 * inch,
                            topMargin=.65 * inch, bottomMargin=.65 * inch,
                            title=lines[0].lstrip("# "),
                            author="AI-assisted research draft; no human review",
                            subject="Reproducible AI policy and governance research")
    def footer(canvas, _doc):
        canvas.saveState()
        canvas.setFont("Vera", 7.2)
        canvas.setFillColor(colors.HexColor("#52616B"))
        canvas.drawString(.775 * inch, .36 * inch, "AI Policy and Governance Research | AI-assisted study draft")
        canvas.drawRightString(7.725 * inch, .36 * inch, str(_doc.page))
        canvas.restoreState()
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--link-base", required=True, help="Public URL corresponding to the Markdown source, used to resolve relative links")
    args = parser.parse_args()
    build(args.source, args.destination, args.link_base)
