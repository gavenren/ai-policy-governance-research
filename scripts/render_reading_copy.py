#!/usr/bin/env python3
"""Build faithful reading copies of the programme's prose-only Markdown papers.

Requires ReportLab. Fonts are supplied by the caller and are not distributed.
Only the source constructs used by S010/S013 are supported. Unsupported block
syntax fails rather than being silently removed. No network access is used.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from hashlib import sha256
from html import escape
from pathlib import Path
import re
from urllib.parse import urljoin

import reportlab
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether


@dataclass
class Block:
    kind: str
    text: str = ''
    level: int = 0
    rows: list | None = None


def parse_markdown(text):
    blocks, pending, rows = [], [], []
    def flush_text():
        if pending:
            blocks.append(Block('paragraph', ' '.join(pending)))
            pending.clear()
    def flush_table():
        if rows:
            assert len({len(r) for r in rows}) == 1, 'Unequal table row lengths'
            blocks.append(Block('table', rows=list(rows)))
            rows.clear()
    for line in text.splitlines() + ['']:
        if line.startswith('|'):
            flush_text()
            cells = [p.strip() for p in line.strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', p.replace(' ', '')) for p in cells):
                rows.append(cells)
            continue
        flush_table()
        if not line.strip():
            flush_text()
        elif (m := re.match(r'^(#{1,3}) (.*)$', line)):
            flush_text()
            blocks.append(Block('heading', m[2], len(m[1])))
        elif line.startswith('> '):
            flush_text()
            blocks.append(Block('disclosure', line[2:]))
        else:
            assert not re.match(r'^(#{4,}|```|~~~|[-*+] |\d+\. |<|\\|\$)', line), f'Unsupported block: {line}'
            pending.append(line)
    return blocks


# Source text contains simple non-nested links/emphasis, checked by validation.
TOKEN = re.compile(r'(\[[^\]]+\]\([^)]+\)|\*\*[^*]+\*\*|(?<!\*)\*[^*]+\*(?!\*)|`[^`]+`)')
LINK = re.compile(r'^\[([^\]]+)\]\(([^)]+)\)$')


def plain(text):
    out = []
    for part in TOKEN.split(text):
        if (m := LINK.match(part)):
            out.append(plain(m[1]))
        elif part.startswith('**') and part.endswith('**'):
            out.append(part[2:-2])
        elif part.startswith('*') and part.endswith('*'):
            out.append(part[1:-1])
        elif part.startswith('`') and part.endswith('`'):
            out.append(part[1:-1])
        else:
            out.append(part)
    return ''.join(out)


def inline(text, link_base):
    out = []
    for part in TOKEN.split(text):
        if (m := LINK.match(part)):
            target = escape(urljoin(link_base, m[2]), quote=True)
            out.append(f'<link color="#185B77" href="{target}">{inline(m[1], link_base)}</link>')
        elif part.startswith('**') and part.endswith('**'):
            out.append('<b>' + escape(part[2:-2]) + '</b>')
        elif part.startswith('*') and part.endswith('*'):
            out.append('<i>' + escape(part[1:-1]) + '</i>')
        elif part.startswith('`') and part.endswith('`'):
            # Keep full text; use the same serif font to avoid smaller file paths.
            out.append('<font color="#334655">' + escape(part[1:-1]) + '</font>')
        else:
            out.append(escape(part))
    return ''.join(out)


class ReadingDoc(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'outline'):
            title, key, level = flowable.outline
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=level, closed=False)


def build(source, destination, link_base, study_id, fonts):
    reportlab.rl_config.invariant = True
    for style, path in fonts.items():
        pdfmetrics.registerFont(TTFont('Reading' + style, str(path)))
    pdfmetrics.registerFontFamily('ReadingRegular', normal='ReadingRegular', bold='ReadingBold', italic='ReadingItalic', boldItalic='ReadingBoldItalic')
    blocks = parse_markdown(source.read_text(encoding='utf-8'))
    assert blocks[0].kind == 'heading' and blocks[0].level == 1
    title = plain(blocks[0].text)
    body = ParagraphStyle('Body', fontName='ReadingRegular', fontSize=11, leading=14.4,
                          spaceAfter=7.4, allowWidows=False, allowOrphans=False,
                          splitLongWords=False, textColor=colors.HexColor('#15212A'))
    styles = {
        1: ParagraphStyle('Title', parent=body, fontName='ReadingBold', fontSize=22, leading=26, spaceAfter=7, keepWithNext=True),
        2: ParagraphStyle('Section', parent=body, fontName='ReadingBold', fontSize=13.2, leading=16.5, spaceBefore=12, spaceAfter=7, keepWithNext=True),
        3: ParagraphStyle('Subsection', parent=body, fontName='ReadingBold', fontSize=11.7, leading=15, spaceBefore=9, spaceAfter=5, keepWithNext=True),
    }
    subtitle = ParagraphStyle('Subtitle', parent=body, fontSize=13, leading=17, spaceAfter=12, keepWithNext=True, textColor=colors.HexColor('#455660'))
    disclosure = ParagraphStyle('Disclosure', parent=body, fontSize=9.2, leading=12, spaceAfter=5, textColor=colors.HexColor('#455660'))
    cell = ParagraphStyle('Cell', parent=body, fontSize=9.4, leading=12.2, spaceAfter=0)
    cell_head = ParagraphStyle('CellHeader', parent=cell, fontName='ReadingBold')
    source_style = ParagraphStyle('Source', parent=disclosure, fontSize=8.5, leading=11, spaceAfter=10)
    margin, width = .78 * inch, 6.94 * inch
    story = []
    for i, block in enumerate(blocks):
        if block.kind == 'heading':
            is_subtitle = i == 1 and block.level == 2
            para = Paragraph(inline(block.text, link_base), subtitle if is_subtitle else styles[block.level])
            if not is_subtitle:
                para.outline = (plain(block.text), f'heading-{i}', block.level - 1)
            story.append(para)
            if is_subtitle:
                story.append(Paragraph(f'PDF reading copy · <link color="#185B77" href="{escape(link_base, quote=True)}">Versioned manuscript source</link> · {study_id}', source_style))
        elif block.kind in ('paragraph', 'disclosure'):
            style = disclosure if block.kind == 'disclosure' or block.text.startswith('**State:') else body
            story.append(Paragraph(inline(block.text, link_base), style))
        elif block.kind == 'table':
            n = len(block.rows[0])
            if n == 6:
                ratios = [.08, .15, .15, .21, .21, .20]
            elif n == 5:
                ratios = [.075, .19, .18, .19, .365]
            elif n == 3 and study_id == 'S010':
                ratios = [.32, .35, .33]
            elif n == 3:
                ratios = [.37, .38, .25]
            else:
                ratios = [1 / n] * n
            data = [[Paragraph(inline(c, link_base), cell_head if row == 0 else cell) for c in cells] for row, cells in enumerate(block.rows)]
            table = Table(data, colWidths=[width * x for x in ratios], repeatRows=1, hAlign='LEFT', splitByRow=1)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EAF0F3')),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LINEBELOW', (0, 0), (-1, 0), .7, colors.HexColor('#607A89')),
                ('LINEBELOW', (0, 1), (-1, -1), .3, colors.HexColor('#D4DEE4')),
                ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
                ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            story.append(KeepTogether([table, Spacer(1, 8)]))
    destination.parent.mkdir(parents=True, exist_ok=True)
    doc = ReadingDoc(str(destination), pagesize=(8.5 * inch, 11 * inch),
        leftMargin=margin, rightMargin=margin, topMargin=.70 * inch, bottomMargin=.68 * inch,
        title=title, author='AI-assisted research draft; no human review',
        subject=f'{study_id}: reading copy; manuscript SHA-256 {sha256(source.read_bytes()).hexdigest()}',
        creator='ReportLab reading-copy builder', pageCompression=1)
    def furniture(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(colors.HexColor('#52616A'))
        canvas.setFont('ReadingRegular', 8)
        if doc.page > 1:
            canvas.drawString(margin, 11 * inch - .38 * inch, study_id + ' | ' + title)
            canvas.setStrokeColor(colors.HexColor('#CDD8DD'))
            canvas.setLineWidth(.35)
            canvas.line(margin, 11 * inch - .45 * inch, 8.5 * inch - margin, 11 * inch - .45 * inch)
        canvas.drawString(margin, .34 * inch, 'AI-assisted complete-study draft | No human peer review')
        canvas.drawRightString(8.5 * inch - margin, .34 * inch, str(doc.page))
        canvas.restoreState()
    doc.build(story, onFirstPage=furniture, onLaterPages=furniture)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('destination', type=Path)
    p.add_argument('--link-base', required=True, help='Version-pinned public URL of the Markdown source')
    p.add_argument('--study-id', required=True)
    for key in ['regular', 'bold', 'italic', 'bold-italic']:
        p.add_argument('--font-' + key, type=Path, required=True)
    a = p.parse_args()
    build(a.source, a.destination, a.link_base, a.study_id,
          {'Regular':a.font_regular, 'Bold':a.font_bold, 'Italic':a.font_italic, 'BoldItalic':a.font_bold_italic})
