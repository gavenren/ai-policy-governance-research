#!/usr/bin/env python3
"""Render S017 with supported flat reference bullets and suitable table widths.

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


def build(source, destination, link_base, fonts):
    original_table, original_paragraph, original_parse = base.Table, base.Paragraph, base.parse_markdown

    class S017Table(original_table):
        def __init__(self, data, colWidths=None, **kwargs):
            width = sum(colWidths)
            if len(data[0]) == 5:
                colWidths = [width*r for r in [.13,.18,.23,.25,.21]]
            elif len(data[0]) == 3:
                colWidths = [width*r for r in [.26,.29,.45]]
            super().__init__(data,colWidths=colWidths,**kwargs)

    class S017Paragraph(original_paragraph):
        def __init__(self,text,style,*args,**kwargs):
            if text is not None and text.startswith('\u2022 '):
                style = copy(style)
                style.leftIndent = 10
                style.firstLineIndent = -10
                style.spaceAfter = 6.5
            super().__init__(text,style,*args,**kwargs)

    try:
        base.Table,base.Paragraph,base.parse_markdown = S017Table,S017Paragraph,parse_markdown
        base.build(source,destination,link_base,'S017',fonts)
    finally:
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
