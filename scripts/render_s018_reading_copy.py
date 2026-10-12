#!/usr/bin/env python3
"""Render S018 with supported flat reference bullets and suitable table widths.

The shared prose builder and Markdown source are not changed. Each Markdown
reference-list marker becomes a bullet; the reference text is preserved.
No math parser or formula substitution is used.
"""
import argparse
from copy import copy
from pathlib import Path

import render_reading_copy as base


ORIGINAL_PARSE = base.parse_markdown


def parse_markdown(text):
    blocks, pending = [], []
    for line in text.splitlines():
        if line.startswith('- '):
            if pending:
                blocks.extend(ORIGINAL_PARSE('\n'.join(pending)))
                pending.clear()
            blocks.append(base.Block('paragraph', '\u2022 ' + line[2:]))
        else:
            pending.append(line)
    if pending:
        blocks.extend(ORIGINAL_PARSE('\n'.join(pending)))
    return blocks


def footer_text(raw):
    if '**State: Working notes.**' in raw:
        return 'AI-assisted working notes | No human peer review'
    if '**State: Complete-study draft.**' in raw:
        return 'AI-assisted complete-study draft | No human peer review'
    raise ValueError('Unknown source state; check the footer before rendering.')


def build(source, destination, link_base, fonts):
    original_table, original_paragraph, original_parse = base.Table, base.Paragraph, base.parse_markdown
    original_doc = base.ReadingDoc
    footer = footer_text(source.read_text(encoding='utf-8'))

    class S018Table(original_table):
        def __init__(self, data, colWidths=None, **kwargs):
            width = sum(colWidths)
            if len(data[0]) == 5:
                colWidths = [width*r for r in [.25,.22,.17,.18,.18]]
            elif len(data[0]) == 3:
                colWidths = [width*r for r in [.32,.34,.34]]
            super().__init__(data,colWidths=colWidths,**kwargs)

    class S018Paragraph(original_paragraph):
        def __init__(self,text,style,*args,**kwargs):
            if text is not None and text.startswith('\u2022 '):
                style = copy(style)
                style.leftIndent = 10
                style.firstLineIndent = -10
                style.spaceAfter = 6.5
            super().__init__(text,style,*args,**kwargs)

    class S018Doc(original_doc):
        def build(self, story, **kwargs):
            def furniture(canvas, doc):
                canvas.saveState()
                canvas.setFillColor(base.colors.HexColor('#52616A'))
                canvas.setFont('ReadingRegular', 8)
                margin, inch = .78 * base.inch, base.inch
                if doc.page > 1:
                    canvas.drawString(margin, 11*inch-.38*inch, 'S018 | '+self.title)
                    canvas.setStrokeColor(base.colors.HexColor('#CDD8DD'))
                    canvas.setLineWidth(.35)
                    canvas.line(margin, 11*inch-.45*inch, 8.5*inch-margin, 11*inch-.45*inch)
                canvas.drawString(margin, .34*inch, footer)
                canvas.drawRightString(8.5*inch-margin, .34*inch, str(doc.page))
                canvas.restoreState()
            kwargs['onFirstPage'] = furniture
            kwargs['onLaterPages'] = furniture
            return super().build(story, **kwargs)

    try:
        base.ReadingDoc = S018Doc
        base.Table,base.Paragraph,base.parse_markdown = S018Table,S018Paragraph,parse_markdown
        base.build(source,destination,link_base,'S018',fonts)
    finally:
        base.ReadingDoc = original_doc
        base.Table,base.Paragraph,base.parse_markdown = original_table,original_paragraph,original_parse


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',type=Path)
    p.add_argument('destination',type=Path)
    p.add_argument('--link-base',required=True)
    for name in ['regular','bold','italic','bold-italic']:
        p.add_argument('--font-'+name,type=Path,required=True)
    a=p.parse_args()
    build(a.source,a.destination,a.link_base,{'Regular':a.font_regular,'Bold':a.font_bold,
          'Italic':a.font_italic,'BoldItalic':a.font_bold_italic})
