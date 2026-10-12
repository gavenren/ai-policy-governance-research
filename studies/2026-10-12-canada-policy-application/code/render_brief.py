"""Build the one-page PDF from the policy brief Markdown."""

from functools import partial
from html import escape
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "policy-brief.md"
OUTPUT = ROOT / "output/pdf/canada-policy-brief.pdf"
PAPER_URL = (
    "https://github.com/gavenren/ai-policy-governance-research/blob/"
    "3edc96d95770b48dcc81c37af85c9064ef32a743/studies/2026-10-12-canada-policy-application/paper.md"
)


def inline(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(
        r"\[([^\]]+)\]\(paper\.md\)",
        lambda match: f'<a href="{PAPER_URL}" color="#176B73">{match[1]}</a>',
        text,
    )
    return text


def page_frame(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#176B73"))
    canvas.setLineWidth(2)
    canvas.line(42, 759, 570, 759)
    canvas.setFillColor(colors.HexColor("#647079"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(42, 24, "AI Policy and Governance Research")
    canvas.drawRightString(570, 24, str(doc.page))
    canvas.restoreState()


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    body = ParagraphStyle(
        "Body", fontName="Helvetica", fontSize=10.3, leading=12.8,
        textColor=colors.HexColor("#1E2B32"), alignment=TA_LEFT,
        spaceAfter=5.4,
    )
    title = ParagraphStyle(
        "Title", parent=body, fontName="Helvetica-Bold", fontSize=19,
        leading=23, spaceAfter=3, textColor=colors.HexColor("#143C44"),
    )
    meta = ParagraphStyle(
        "Meta", parent=body, fontSize=9, leading=11,
        textColor=colors.HexColor("#647079"), spaceAfter=9,
    )
    heading = ParagraphStyle(
        "Heading", parent=body, fontName="Helvetica-Bold", fontSize=11.4,
        leading=14, spaceBefore=5.5, spaceAfter=4,
        textColor=colors.HexColor("#176B73"), keepWithNext=True,
    )
    item = ParagraphStyle("Item", parent=body, leftIndent=13, firstLineIndent=-13)
    note = ParagraphStyle("Note", parent=body, fontSize=8.8, leading=10.8, spaceBefore=3)
    story = []
    for block in SOURCE.read_text().strip().split("\n\n"):
        if block.startswith("# "):
            story.append(Paragraph(inline(block[2:]), title))
        elif block.startswith("## "):
            story.append(Paragraph(inline(block[3:]), heading))
        elif block.startswith("One-page"):
            story.append(Paragraph(inline(block), meta))
        elif re.match(r"\d+\. ", block):
            for line in block.splitlines():
                story.append(Paragraph(inline(line), item))
        elif block.startswith("**Basis and limits:"):
            story.append(Paragraph(inline(block), note))
        else:
            story.append(Paragraph(inline(block), body))
    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=letter, leftMargin=42, rightMargin=42,
        topMargin=42, bottomMargin=39, title="Canada: A Secure Living After Wages - Policy Brief",
        author="Codex", subject="Action order and funding for an economy after wages",
    )
    doc.build(
        story, onFirstPage=page_frame, onLaterPages=page_frame,
        canvasmaker=partial(Canvas, invariant=1),
    )
    print(OUTPUT)


if __name__ == "__main__":
    build()
