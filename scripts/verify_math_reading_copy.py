#!/usr/bin/env python3
"""Verify prose, formulas, glyph positions, rules, links and font embedding.

Vector equation forms are checked separately from prose. Their drawing calls
are removed only in the in-memory extraction view; the PDF is never edited.
"""
import argparse,hashlib,json,re,unicodedata
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urljoin
from pypdf import PdfReader,PageObject
from pypdf.generic import DecodedStreamObject,NameObject,ContentStream,DictionaryObject
from render_math_reading_copy import parse,INLINE_MATH,DISPLAY
from render_reading_copy import plain as plain_once

def plain(text):
    while True:
        next_text=plain_once(text)
        if next_text==text:return text
        text=next_text

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+','',unicodedata.normalize('NFC',s))
def outline(items):
    for x in items:
        if isinstance(x,list):yield from outline(x)
        else:yield str(x['/Title'])
def verify(source,pdf):
    record=json.loads((pdf.parent/'math-layout.json').read_text());raw=source.read_text();blocks=parse(raw)
    assert sha(source)==record['source_sha256'] and sha(pdf)==record['pdf_sha256']
    equations=record['equations'];r=PdfReader(pdf);forms={};uses=Counter();text=[];tags=Counter();foundlinks=[]
    font_records={}
    for number,page in enumerate(r.pages,1):
        resources=page['/Resources']
        for key,ref in resources.get('/XObject',{}).items():
            assert str(key).startswith('/FormXob.Math'),'Unexpected raster/image form'
            forms[str(key).split('.')[-1]]=ref.get_object()
        for ref in page.get('/Annots',[]):
            obj=ref.get_object()
            if obj.get('/A',{}).get('/S')=='/URI':foundlinks.append(str(obj['/A']['/URI']))
        stream=page.get_contents().get_data()
        for name in re.findall(rb'/FormXob\.(Math\d+) Do',stream):uses[name.decode()]+=1
        # Byte-level removal preserves original text encoding and ToUnicode maps.
        clean=re.sub(rb'/FormXob\.Math\d+ Do',b'',stream)
        new=DecodedStreamObject();new.set_data(clean);page[NameObject('/Contents')]=new
        extracted=page.extract_text()
        title=plain(blocks[0].text)
        furniture=('' if number==1 else record['study']+' | '+title+'\n')+'AI-assisted complete-study draft | No human peer review\n'+str(number)+'\n'
        assert extracted.startswith(furniture),(number,'page furniture')
        extracted=extracted[len(furniture):]
        if number==1:
            label='PDF reading copy · Versioned manuscript source · '+record['study']+'\n';assert extracted.count(label)==1;extracted=extracted.replace(label,'')
        for e in equations:
            if e['tag'] and e['placements'][0]['page']==number:
                value='('+e['tag']+')\n';assert extracted.count(value)==1,(number,value);extracted=extracted.replace(value,'');tags[e['tag']]+=1
        # Bullet marks are layout, while the reference text remains source text.
        extracted=extracted.replace('•','')
        text.append(extracted)
        for ref in resources['/Font'].values():
            font=ref.get_object();desc=font.get('/FontDescriptor');name=str(font['/BaseFont'])
            embedded=bool(desc and any(k in desc.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']))
            font_records[name]=embedded
    expected=[];units=[]
    for i,b in enumerate(blocks):
        if b.kind=='math':continue
        cells=[c for row in b.rows for c in row] if b.kind=='table' else [b.text]
        for c in cells:
            value=plain(INLINE_MATH.sub('',c));expected.append(value)
            units.append({'block':i,'kind':'table_cell' if b.kind=='table' else b.kind,'normalized_sha256':hashlib.sha256(norm(value).encode()).hexdigest()})
    actual=norm('\n'.join(text));want=norm(''.join(expected))
    assert actual==want,('Prose mismatch',len(actual),len(want),next(((i,actual[i-40:i+50],want[i-40:i+50]) for i in range(min(len(actual),len(want))) if actual[i]!=want[i]),None))
    # A second plain-source pass detects loss or duplication by the block parser.
    independent=DISPLAY.sub('',raw);independent=INLINE_MATH.sub('',independent)
    lines=[]
    for line in independent.splitlines():
        if re.fullmatch(r'\|[\s:|\-]+\|',line):continue
        line=re.sub(r'^#{1,3} |^- ','',line)
        if line.startswith('|'):line=line.replace('|',' ')
        lines.append(plain(line))
    assert norm('\n'.join(lines))==want,'Independent source coverage check failed'
    assert actual.count('$')==record['literal_dollar_count']
    mathchecks=[]
    for e in equations:
        assert uses[e['id']]==1
        form=forms[e['id']]
        fake=PageObject.create_blank_page(width=612,height=792);fake[NameObject('/Resources')]=form['/Resources'];fake[NameObject('/Contents')]=form
        glyphs=[]
        def visitor(t,cm,tm,font,size):
            if norm(t):glyphs.append({'text':norm(t),'x':float(tm[4]),'y':float(tm[5]),'size':float(size),'font':str(font['/BaseFont'])})
        value=fake.extract_text(visitor_text=visitor)
        assert norm(value)==norm(''.join(chr(g['codepoint']) for g in e['glyphs'])),(e['id'],'glyph sequence')
        assert len(glyphs)==len(e['glyphs']),(e['id'],'glyph count')
        for got,g in zip(glyphs,e['glyphs']):
            assert got['text']==chr(g['codepoint'])
            for a,b in [(got['x'],g['x']),(got['y'],g['y']+e['depth']),(got['size'],g['size'])]:assert abs(a-b)<1e-4,(e['id'],a,b)
        rules=[[float(v) for v in o] for o,op in ContentStream(form,r).operations if op==b're']
        assert len(rules)==len(e['rules'])
        for got,rule in zip(rules,e['rules']):
            expected_rule=[rule[0],rule[1]+e['depth'],rule[2],rule[3]]
            assert all(abs(a-b)<1e-4 for a,b in zip(got,expected_rule))
        pos=e['placements'][0];assert pos['x']>=56 and pos['x']+e['width']<=556 and pos['y']>=48 and pos['y']+e['height']<=742
        assert hashlib.sha256(e['raw_latex'].encode()).hexdigest()==e['source_latex_sha256']
        mathchecks.append({'id':e['id'],'glyphs_checked':len(glyphs),'rules_checked':len(rules),'tag':e['tag'],'source_latex_sha256':e['source_latex_sha256'],'page':pos['page']})
    assert set(forms)==set(e['id'] for e in equations)
    expectedlinks=[urljoin(record['source_url'],x) for x in re.findall(r'\[[^]]+\]\(([^)]+)\)',raw)]+[record['source_url']]
    assert set(foundlinks)==set(expectedlinks),(set(expectedlinks)-set(foundlinks),set(foundlinks)-set(expectedlinks))
    headings=[plain(b.text) for i,b in enumerate(blocks) if b.kind=='heading' and i!=1]
    assert list(outline(r.outline))==headings
    assert all(value for key,value in font_records.items() if key!='/Helvetica')
    result={'checked_utc':datetime.now(timezone.utc).isoformat(),'study':record['study'],'source_sha256':sha(source),'pdf_sha256':sha(pdf),
            'verifier_sha256':sha(__file__),'pages':len(r.pages),'strict_prose_and_table_text_match':True,'independent_source_coverage':True,
            'prose_units_checked':len(units),'prose_characters_without_whitespace':len(want),'literal_currency_dollars_preserved':record['literal_dollar_count'],
            'vector_coordinate_tolerance_points':0.0001,'vector_math_forms_checked':len(mathchecks),'math_glyphs_checked':sum(x['glyphs_checked'] for x in mathchecks),'math_rules_checked':sum(x['rules_checked'] for x in mathchecks),
            'equation_tags_checked':dict(tags),'unique_links':len(set(foundlinks)),'bookmarks':len(headings),'fonts':font_records,
            'source_units':units,'math_checks':mathchecks,'limit':'Text and vector checks do not replace page and equation visual review. PDF math copying may not preserve LaTeX structure.'}
    (pdf.parent/'text-math-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['source_units','math_checks','fonts']},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('pdf',type=Path);a=p.parse_args();verify(a.source,a.pdf)
