"""Check retained public evidence; optional original-source byte verification."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser();p.add_argument('--local',type=Path);a=p.parse_args()
    m=json.loads((ROOT/'sources/manifest.json').read_text())
    ids=[];local=0
    for r in m['records']:
        ids.append(r['source_id'])
        for field in ('title','canonical_url','publication_or_update_date','claim_locator','rights','coverage'):
            assert r[field],(r['source_id'],field)
        e=r['public_evidence'];b=(ROOT/e['path']).read_bytes()
        assert len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256'],r['source_id']
        if a.local:
            for kind in ('original','extraction'):
                e=r[kind]
                if e:
                    b=(a.local/e['local_file']).read_bytes()
                    assert len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256'],(r['source_id'],kind)
                    local+=1
    assert len(ids)==len(set(ids))==14
    for p in ROOT.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if '://' in target or target.startswith('#'):continue
            dest=target.split('#')[0]
            assert (p.parent/dest).exists(),(str(p.relative_to(ROOT)),target)
    print(json.dumps({'source_records':len(ids),'public_evidence_hashes_verified':len(ids),
                      'local_representations_verified':local,'relative_links':'pass',
                      'limit':'Byte and link checks do not verify interpretation or research originality.'},indent=2))

if __name__=='__main__':main()
