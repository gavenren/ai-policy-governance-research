#!/usr/bin/env python3
"""Check every S018 text unit, list item, table cell, link and bookmark."""
import argparse
from collections import Counter
from datetime import datetime,timezone
from hashlib import sha256
import json
from pathlib import Path
import re
from urllib.parse import urljoin

import pdfplumber
from pypdf import PdfReader

from render_reading_copy import plain
from render_s018_reading_copy import parse_markdown, footer_text
from verify_reading_copy import normal,flattened_outline


def verify(source,pdf,link_base):
    raw=source.read_text(encoding='utf-8');blocks=parse_markdown(raw)
    chunks=[]
    for index,b in enumerate(blocks):
        if b.kind=='table':
            for row,cells in enumerate(b.rows):
                for column,cell in enumerate(cells):
                    chunks.append({'block':index,'kind':'table_cell','row':row,'column':column,'text':plain(cell)})
        else:
            kind='list_item' if b.text.startswith('\u2022 ') else b.kind
            chunks.append({'block':index,'kind':kind,'text':plain(b.text)})
    lines=[]
    for line in raw.splitlines():
        if re.fullmatch(r'\|[\s:|\-]+\|',line):continue
        line=re.sub(r'^#{1,3} ','',line)
        line=re.sub(r'^> ','',line)
        line=re.sub(r'^- ','\u2022 ',line)
        line=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',line)
        line=line.replace('**','').replace('*','').replace('`','')
        if line.startswith('|'):line=line.replace('|',' ')
        lines.append(line)
    expected=normal(''.join(c['text'] for c in chunks))
    assert expected==normal('\n'.join(lines)), 'Independent source view differs'
    reader=PdfReader(pdf);parts=[];title=plain(blocks[0].text)
    for n,page in enumerate(reader.pages,1):
        text=page.extract_text()
        furniture='' if n==1 else f'S018 | {title}\n'
        furniture+=footer_text(raw)+f'\n{n}\n'
        assert text.startswith(furniture),(n,'Furniture differs')
        text=text[len(furniture):]
        if n==1:
            notice='PDF reading copy · Versioned manuscript source · S018\n'
            assert text.count(notice)==1
            text=text.replace(notice,'')
        parts.append(text)
    actual=normal('\n'.join(parts));assert actual==expected,'Source text or order differs'
    offset=0;checks=[]
    for chunk in chunks:
        value=normal(chunk['text']);assert actual[offset:offset+len(value)]==value
        checks.append({k:v for k,v in chunk.items() if k!='text'}|{'normalized_sha256':sha256(value.encode()).hexdigest(),'start':offset,'end':offset+len(value)})
        offset+=len(value)
    expected_urls=Counter([urljoin(link_base,u) for u in re.findall(r'\[[^]]+\]\(([^)]+)\)',raw)]+[link_base])
    found=Counter();annotations=[];fonts={}
    for n,page in enumerate(reader.pages,1):
        for ref in page.get('/Annots',[]):
            a=ref.get_object()
            if a.get('/A',{}).get('/S')=='/URI':
                uri=str(a['/A']['/URI']);rect=list(map(float,a['/Rect']))
                assert 0<=rect[0]<rect[2]<=612 and 0<=rect[1]<rect[3]<=792
                found[uri]+=1;annotations.append({'page':n,'uri':uri,'rectangle':rect})
        for ref in page['/Resources']['/Font'].values():
            f=ref.get_object();name=str(f['/BaseFont']);d=f.get('/FontDescriptor')
            fonts[name]=bool(d and any(k in d.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']))
    assert set(found)==set(expected_urls)
    assert all(found[url]>=count for url,count in expected_urls.items())
    assert all(e for f,e in fonts.items() if f!='/Helvetica')
    headings=[plain(b.text) for i,b in enumerate(blocks) if b.kind=='heading' and not(i==1 and b.level==2)]
    assert [str(x['/Title']) for x in flattened_outline(reader.outline)]==headings
    bounds=[]
    with pdfplumber.open(pdf) as doc:
        for n,page in enumerate(doc.pages,1):
            assert all(56.15<=c['x0']<c['x1']<=555.85 and 0<=c['top']<c['bottom']<=792 for c in page.chars),n
            bounds.append({'page':n,'characters':len(page.chars),'minimum_x':min(c['x0'] for c in page.chars),'maximum_x':max(c['x1'] for c in page.chars)})
    return {'checked_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
            'source':str(source),'source_sha256':sha256(source.read_bytes()).hexdigest(),
            'pdf':str(pdf),'pdf_sha256':sha256(pdf.read_bytes()).hexdigest(),'source_url':link_base,
            'pages':len(reader.pages),'strict_ordered_text_match':True,
            'normalization':'Remove whitespace and apply Unicode NFC. Markdown list markers are rendered as bullets; all source words and other punctuation are preserved.',
            'blocks_checked':len(blocks),'units_checked':len(chunks),'unit_types':dict(Counter(c['kind'] for c in chunks)),
            'normalized_source_characters':len(expected),'source_link_occurrences':sum(expected_urls.values()),
            'unique_clickable_urls':len(found),'link_annotations':sum(found.values()),'bookmarks':len(headings),
            'fonts':fonts,'all_characters_within_page_and_horizontal_margins':True,'page_bounds':bounds,
            'expected_link_occurrences':dict(expected_urls),'found_link_annotations':dict(found),
            'annotation_rectangles':annotations,'unit_order_checks':checks,'visual_review':'Separate visual review required.'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',type=Path);p.add_argument('pdf',type=Path)
    p.add_argument('--link-base',required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();record=verify(a.source,a.pdf,a.link_base)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['source_sha256','pdf_sha256','pages','units_checked','unit_types','strict_ordered_text_match','source_link_occurrences','unique_clickable_urls','link_annotations','bookmarks']},indent=2))
