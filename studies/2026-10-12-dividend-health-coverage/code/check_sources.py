"""Check evidence records only. This is not a legal or eligibility engine."""
from pathlib import Path
import argparse, collections, hashlib, json, re
from datetime import datetime, timezone

STUDY=Path(__file__).resolve().parents[1]
REPO=STUDY.parents[1]

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def normal(t):
    t=re.sub(r'^L\d+(?:@P[\d-]+)?:\s*','',t,flags=re.M)
    return ' '.join(t.split())

def check(local=False):
    manifest=json.loads((STUDY/'sources/manifest.json').read_text())
    sources=manifest['sources']
    ids=[s['id'] for s in sources]
    assert len(ids)==len(set(ids)), 'Repeated source ID'
    required=('title','version','read_scope','use_and_limit','rights','start_utc','end_utc','capture_type')
    for s in sources:
        for k in required: assert s.get(k), (s['id'],k)
    quotes=json.loads((STUDY/'evidence/short-quotes.json').read_text())
    totals=collections.Counter()
    for q in quotes:
        assert q['source_id'] in ids
        words=len(q['quote'].split())
        assert words==q['word_count'],q['id']
        totals[q['copyright_group']]+=words
    assert all(n<=25 for n in totals.values()), totals
    checked={}
    def file_check(r):
        path=r['path']
        assert re.fullmatch(r'[a-f0-9]{64}',r['sha256'])
        if local:
            p=REPO/path
            assert p.exists(),path
            assert p.stat().st_size==r['bytes'],path
            assert digest(p)==r['sha256'],path
            checked[path]=True
    def walk(x):
        if isinstance(x,dict):
            if all(k in x for k in ('path','bytes','sha256')):file_check(x)
            if all(k in x for k in ('text_path','text_bytes','text_sha256')):
                file_check({'path':x['text_path'],'bytes':x['text_bytes'],'sha256':x['text_sha256']})
            for v in x.values():walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    walk(sources)
    web=json.loads((STUDY/'logs/web-captures.json').read_text())
    walk(web)
    if local:
        for q in quotes:
            assert normal(q['quote']) in normal((REPO/q['private_text_path']).read_text()),q['id']
    return {'recorded_utc':datetime.now(timezone.utc).isoformat(),'mode':'local' if local else 'public','source_count':len(ids),'web_response_count':len(web),'quote_count':len(quotes),'private_files_checked':len(checked),'passed':True,'scope':'Evidence schema, quote budgets, and optionally exact private hashes and normalized quote matches; not legal truth or code outcomes.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--local',action='store_true');p.add_argument('--output')
    a=p.parse_args();r=check(a.local);t=json.dumps(r,indent=2)+'\n'
    if a.output:Path(a.output).write_text(t)
    print(t,end='')
