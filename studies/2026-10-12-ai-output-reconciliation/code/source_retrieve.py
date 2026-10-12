"""Retrieve public source bytes for a version check. Never run source code."""
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, subprocess

STUDY=Path(__file__).resolve().parents[1]
def main():
    p=ArgumentParser();p.add_argument('--output',type=Path,required=True)
    p.add_argument('--ids',nargs='+',default=['B1','B2','P2','C1']);a=p.parse_args()
    sources=json.loads((STUDY/'sources/manifest.json').read_text())
    sources=[s for s in sources if s['id'] in a.ids]
    assert {s['id'] for s in sources}==set(a.ids),'Unknown source ID'
    a.output.mkdir(parents=True,exist_ok=True)
    def path(s):return a.output/(s['id']+('.zip' if s['retained_media_type']=='application/zip' else '.pdf'))
    assert not (a.output/'capture.json').exists(),'Choose a fresh output folder'
    assert not any(path(s).exists() for s in sources),'Do not overwrite earlier captures'
    def get(s):
        dest=path(s);start=datetime.now(timezone.utc).isoformat()
        r=subprocess.run(['curl','-L','-f','-sS','--max-time','45','-o',str(dest),
                          '-w','%{http_code}\n%{url_effective}',s['requested_url']],capture_output=True,text=True)
        end=datetime.now(timezone.utc).isoformat()
        d={'id':s['id'],'requested_url':s['requested_url'],'start_utc':start,'end_utc':end,
           'method':'curl HTTPS GET; normal TLS','http_and_final_url':r.stdout,'exit_code':r.returncode,
           'stderr':r.stderr,'path':str(dest),'expected_sha256':s['snapshot']['sha256']}
        if r.returncode==0:
            b=dest.read_bytes();d.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
            d['matches_frozen_source']=d['sha256']==s['snapshot']['sha256']
        return d
    results=list(ThreadPoolExecutor(max_workers=4).map(get,sources))
    (a.output/'capture.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))
    if not all(x.get('matches_frozen_source',False) for x in results):raise SystemExit(1)
if __name__=='__main__':main()
