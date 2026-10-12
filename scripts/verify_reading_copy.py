#!/usr/bin/env python3
"""Check source text, order, links, bookmarks and font embedding in a reading PDF.

Requires pypdf and the adjacent render_reading_copy.py. This does not replace
visual review. No network or private data are used.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urljoin

from pypdf import PdfReader
from render_reading_copy import parse_markdown, plain


def normal(text):
    return re.sub(r'\s+', '', unicodedata.normalize('NFC', text))


def flattened_outline(outline):
    for item in outline:
        if isinstance(item, list):
            yield from flattened_outline(item)
        else:
            yield item


def verify(source, pdf, study, link_base):
    raw = source.read_text(encoding='utf-8')
    blocks = parse_markdown(raw)
    chunks = []
    for index, block in enumerate(blocks):
        if block.kind == 'table':
            for row, cells in enumerate(block.rows):
                for column, cell in enumerate(cells):
                    chunks.append({'block':index, 'kind':'table_cell', 'row':row, 'column':column, 'text':plain(cell)})
        else:
            chunks.append({'block':index, 'kind':block.kind, 'text':plain(block.text)})
    # Independent source view: remove only the known presentation markup.
    lines = []
    for line in raw.splitlines():
        if re.fullmatch(r'\|[\s:|\-]+\|', line):
            continue
        line = re.sub(r'^#{1,3} ', '', line)
        line = re.sub(r'^> ', '', line)
        line = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', line)
        line = line.replace('**', '').replace('*', '').replace('`', '')
        if line.startswith('|'):
            line = line.replace('|', ' ')
        lines.append(line)
    expected = normal(''.join(c['text'] for c in chunks))
    assert normal('\n'.join(lines)) == expected, 'Parsed blocks differ from independent plain source'
    reader = PdfReader(pdf)
    text_parts = []
    title = plain(blocks[0].text)
    for page_no, page in enumerate(reader.pages, 1):
        text = page.extract_text()
        furniture = '' if page_no == 1 else f'{study} | {title}\n'
        furniture += f'AI-assisted complete-study draft | No human peer review\n{page_no}\n'
        assert text.startswith(furniture), (page_no, 'Unexpected furniture')
        text = text[len(furniture):]
        if page_no == 1:
            label = f'PDF reading copy · Versioned manuscript source · {study}\n'
            assert text.count(label) == 1
            text = text.replace(label, '')
        text_parts.append(text)
    actual = normal('\n'.join(text_parts))
    # Strict equality also rejects any omitted or duplicated source words.
    assert actual == expected, f'Text mismatch: expected {len(expected)}, got {len(actual)} characters'
    offset = 0
    checks = []
    for chunk in chunks:
        value = normal(chunk['text'])
        assert actual[offset:offset + len(value)] == value, chunk
        checks.append({k:v for k,v in chunk.items() if k != 'text'} | {'normalized_sha256':sha256(value.encode()).hexdigest(), 'start':offset, 'end':offset + len(value)})
        offset += len(value)
    links = [urljoin(link_base, x) for x in re.findall(r'\[[^]]+\]\(([^)]+)\)', raw)] + [link_base]
    found = []
    for page in reader.pages:
        for ref in page.get('/Annots', []):
            ann = ref.get_object()
            if ann.get('/A', {}).get('/S') == '/URI':
                found.append(str(ann['/A']['/URI']))
    assert set(found) == set(links), {'missing':set(links)-set(found), 'extra':set(found)-set(links)}
    outline = list(flattened_outline(reader.outline))
    headings = [plain(b.text) for i,b in enumerate(blocks) if b.kind == 'heading' and not (i == 1 and b.level == 2)]
    assert [str(x['/Title']) for x in outline] == headings, 'Bookmark headings differ'
    fonts = {}
    for page in reader.pages:
        for font in page['/Resources']['/Font'].values():
            f = font.get_object()
            name = str(f['/BaseFont'])
            desc = f.get('/FontDescriptor')
            embedded = bool(desc and any(k in desc.get_object() for k in ['/FontFile', '/FontFile2', '/FontFile3']))
            fonts[name] = embedded
    # ReportLab declares an unused base Helvetica resource. All actual manuscript
    # fonts are TrueType subsets and must be embedded.
    manuscript_fonts = {n:e for n,e in fonts.items() if n != '/Helvetica'}
    assert manuscript_fonts and all(manuscript_fonts.values()), fonts
    return {'checked_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
            'source':str(source), 'source_sha256':sha256(source.read_bytes()).hexdigest(),
            'pdf':str(pdf), 'pdf_sha256':sha256(pdf.read_bytes()).hexdigest(),
            'source_url':link_base, 'pages':len(reader.pages), 'strict_source_text_match':True,
            'normalization':'Remove whitespace and apply Unicode NFC only; source punctuation is preserved.',
            'blocks_checked':len(blocks), 'units_checked':len(chunks), 'unit_types':dict(Counter(c['kind'] for c in chunks)),
            'normalized_source_characters':len(expected), 'source_link_occurrences':len(links),
            'unique_clickable_urls':len(set(found)), 'link_annotations':len(found), 'bookmarks':len(headings),
            'fonts':fonts, 'unit_order_checks':checks, 'visual_review':'Separate visual review required.'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('pdf', type=Path)
    p.add_argument('--study-id', required=True)
    p.add_argument('--link-base', required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    result = verify(a.source, a.pdf, a.study_id, a.link_base)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'unit_order_checks'}, indent=2))
