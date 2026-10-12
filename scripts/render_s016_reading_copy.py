#!/usr/bin/env python3
"""Render the published S016 prose manuscript with its plain-text appendix.

This wrapper reuses render_reading_copy.py without changing that builder. Its
only layout changes are suitable widths for S016's five-column table and
clickable bare HTTP(S) URLs. Text and notation are not changed. Fonts are
supplied locally and are not distributed. No network access is used.
"""
from __future__ import annotations

import argparse
from html import escape
from pathlib import Path
import re

import render_reading_copy as base


URL = re.compile(r'https?://[^\s<>]+')


def build(source, destination, link_base, fonts):
    original_inline, original_table = base.inline, base.Table

    def linked_inline(text, url_base):
        parts = []
        for part in base.TOKEN.split(text):
            if base.TOKEN.fullmatch(part):
                parts.append(original_inline(part, url_base))
                continue
            cursor = 0
            for match in URL.finditer(part):
                # Sentence punctuation remains outside the clickable target.
                url = match[0].rstrip('.,;:!?')
                parts.append(escape(part[cursor:match.start()]))
                parts.append('<link color="#185B77" href="' + escape(url, quote=True)
                             + '">' + escape(url) + '</link>')
                parts.append(escape(match[0][len(url):]))
                cursor = match.end()
            parts.append(escape(part[cursor:]))
        return ''.join(parts)

    class S016Table(original_table):
        def __init__(self, data, colWidths=None, **kwargs):
            if len(data[0]) == 5:
                width = sum(colWidths)
                colWidths = [width * ratio for ratio in [.23, .18, .19, .18, .22]]
            super().__init__(data, colWidths=colWidths, **kwargs)

    try:
        base.inline, base.Table = linked_inline, S016Table
        base.build(source, destination, link_base, 'S016', fonts)
    finally:
        base.inline, base.Table = original_inline, original_table


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--link-base', required=True)
    for name in ['regular', 'bold', 'italic', 'bold-italic']:
        parser.add_argument('--font-' + name, type=Path, required=True)
    args = parser.parse_args()
    build(args.source, args.destination, args.link_base,
          {'Regular': args.font_regular, 'Bold': args.font_bold,
           'Italic': args.font_italic, 'BoldItalic': args.font_bold_italic})
