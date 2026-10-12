#!/usr/bin/env python3
"""Check S016 text, plain notation, hyperlinks, page bounds and local fonts.

Reuses the strict general text verifier. Visual review is still required.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import argparse
import json
from pathlib import Path
import re
from urllib.parse import urljoin

import pdfplumber
from pypdf import PdfReader

from render_reading_copy import TOKEN
from render_s016_reading_copy import URL
from verify_reading_copy import verify


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('pdf', type=Path)
    p.add_argument('--link-base', required=True)
    p.add_argument('--font-dir', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    result = verify(a.source, a.pdf, 'S016', a.link_base)
    raw = a.source.read_text(encoding='utf-8')
    links = [urljoin(a.link_base, x) for x in re.findall(r'\[[^]]+\]\(([^)]+)\)', raw)]
    bare = [m[0].rstrip('.,;:!?') for part in TOKEN.split(raw)
            if not TOKEN.fullmatch(part) for m in URL.finditer(part)]
    expected = Counter(links + bare + [a.link_base])
    found, annotations = Counter(), []
    reader = PdfReader(a.pdf)
    for index, page in enumerate(reader.pages, 1):
        for reference in page.get('/Annots', []):
            annotation = reference.get_object()
            if annotation.get('/A', {}).get('/S') != '/URI':
                continue
            uri = str(annotation['/A']['/URI'])
            x0, y0, x1, y1 = map(float, annotation['/Rect'])
            assert 0 <= x0 < x1 <= 612 and 0 <= y0 < y1 <= 792
            annotations.append({'page': index, 'uri': uri, 'rectangle': [x0,y0,x1,y1]})
            found[uri] += 1
    assert set(found) == set(expected)
    assert all(found[url] >= count for url, count in expected.items())
    bounds = []
    with pdfplumber.open(a.pdf) as pdf:
        for index, page in enumerate(pdf.pages, 1):
            assert all(56.15 <= c['x0'] < c['x1'] <= 555.85 and
                       0 <= c['top'] < c['bottom'] <= 792 for c in page.chars)
            bounds.append({'page': index, 'characters': len(page.chars),
                           'minimum_x': min(c['x0'] for c in page.chars),
                           'maximum_x': max(c['x1'] for c in page.chars),
                           'minimum_top': min(c['top'] for c in page.chars),
                           'maximum_bottom': max(c['bottom'] for c in page.chars)})
    appendix = raw[raw.index('## Appendix A.'):raw.index('## References')]
    fonts = []
    for suffix in ['', ' Bold', ' Italic', ' Bold Italic']:
        font = a.font_dir / ('Times New Roman' + suffix + '.ttf')
        fonts.append({'filename': font.name, 'bytes': font.stat().st_size,
                      'sha256': sha256(font.read_bytes()).hexdigest()})
    result.update({'checked_at_utc': datetime.now(timezone.utc).isoformat(),
                   'bare_reference_urls': bare,
                   'expected_link_occurrences_including_bare_urls': sum(expected.values()),
                   'link_occurrence_check': 'Each target has at least one annotation per source occurrence; wrapped link labels can have two annotations.',
                   'expected_occurrences_by_url': dict(expected),
                   'actual_annotations_by_url': dict(found),
                   'annotation_rectangles': annotations,
                   'all_characters_inside_page_and_horizontal_margins': True,
                   'page_bounds': bounds,
                   'appendix_source_sha256': sha256(appendix.encode()).hexdigest(),
                   'appendix_note': 'All plain notation, including underscores, carets and Unicode minus signs, is part of the strict text and order check. No math conversion is used.',
                   'local_font_files': fonts})
    a.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k:result[k] for k in ['pages','units_checked','strict_source_text_match',
          'pdf_sha256','expected_link_occurrences_including_bare_urls',
          'link_annotations','all_characters_inside_page_and_horizontal_margins']}, indent=2))
