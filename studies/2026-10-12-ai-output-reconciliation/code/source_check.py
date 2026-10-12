"""Check source metadata and local retained evidence; does not run the source model."""
from argparse import ArgumentParser
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import csv, hashlib, json, re, zipfile
ROOT=Path(__file__).resolve().parents[3]
STUDY=Path(__file__).resolve().parents[1]
def norm(s):return re.sub(r'\s+',' ',s).strip()
def main():
    parser=ArgumentParser();parser.add_argument('--local',action='store_true');args=parser.parse_args()
    sources=json.loads((STUDY/'sources/manifest.json').read_text());byid={s['id']:s for s in sources}
    assert len(byid)==len(sources)==9
    quotes=list(csv.DictReader((STUDY/'evidence/shortquotes.csv').open()));words=defaultdict(int)
    n=0
    for s in sources:
        for k in ['title','authors','version','read_scope','requested_url','rights','retrieval_start_utc','retrieval_end_utc']:assert s[k]
        for k in ['snapshot','text_snapshot']:
            if k not in s:continue
            d=s[k];assert len(d['sha256'])==64 and d['bytes']>0
            if args.local:
                b=(ROOT/d['path']).read_bytes();assert len(b)==d['bytes'] and hashlib.sha256(b).hexdigest()==d['sha256'],d['path'];n+=1
    for q in quotes:
        i=q['source_id'];assert i in byid
        count=len(q['quote'].split());assert count==int(q['word_count']);words[i]+=count
        if args.local:
            s=byid[i]
            text=(ROOT/s['text_snapshot']['path']).read_text() if i!='C1' else zipfile.ZipFile(ROOT/s['snapshot']['path']).read('replication/results.py').decode()
            assert norm(q['quote']) in norm(text),(i,q['quote'])
    # B2 and P2 are versions of one work. Combine their quote allowances.
    words['appendix_all_versions']=words.get('B2',0)+words.get('P2',0)
    assert all(x<=25 for x in words.values())
    members=json.loads((STUDY/'sources/archive-members.json').read_text())
    if args.local:
        z=zipfile.ZipFile(ROOT/byid['C1']['snapshot']['path'])
        for d in members:
            b=z.read(d['name']);assert len(b)==d['bytes'] and hashlib.sha256(b).hexdigest()==d['sha256'],d['name']
    bell_members=json.loads((STUDY/'sources/bell-archive-members.json').read_text())
    if args.local:
        z=zipfile.ZipFile(ROOT/byid['Z1C']['snapshot']['path'])
        for d in bell_members:
            b=z.read(d['name']);assert len(b)==d['bytes'] and hashlib.sha256(b).hexdigest()==d['sha256'],d['name']
    result={'checked_utc':datetime.now(timezone.utc).isoformat(),'pass':True,'mode':'local bytes and quotes' if args.local else 'public metadata only',
            'sources':len(sources),'local_raw_or_text_files':n,'archive_members':len(members)+len(bell_members) if args.local else 0,
            'quotes':len(quotes),'quote_words':dict(words),'scope':'No source calculation code is imported or executed.'}
    suffix='local' if args.local else 'public'
    (STUDY/f'logs/source-check-{suffix}.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
