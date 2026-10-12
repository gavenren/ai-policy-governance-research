"""Acquire pinned extension originals into a new directory without overwrite."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,subprocess,zipfile
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--destination',type=Path,required=True);p.add_argument('--ids',nargs='+',default=['E1'])
 a=p.parse_args()
 if a.destination.exists():raise SystemExit('Use a new destination')
 m={r['source_id']:r for r in json.loads((ROOT/'sources/manifest.json').read_text())['records']}
 if set(a.ids)-set(m):raise SystemExit('Unknown source ID')
 if any(m[sid]['original'] is None for sid in a.ids):raise SystemExit('This source has tool text only; no pinned original can be fetched by this script')
 a.destination.mkdir(parents=True);logs=[]
 for sid in a.ids:
  s=m[sid];dest=a.destination/Path(s['original']['local_path']).name
  start=datetime.now(timezone.utc).isoformat()
  r=subprocess.run(['curl','--fail','--location','--silent','--show-error','--max-time','120',s['canonical_url'],'--output',str(dest),'--write-out','%{http_code}\n%{url_effective}'],capture_output=True,text=True)
  digest=hashlib.sha256(dest.read_bytes()).hexdigest() if dest.exists() else None
  rec=dict(source_id=sid,started_utc=start,completed_utc=datetime.now(timezone.utc).isoformat(),requested_url=s['canonical_url'],response=r.stdout.splitlines(),error=r.stderr,returncode=r.returncode,sha256=digest,matches=digest==s['original']['sha256'])
  logs.append(rec);(a.destination/'capture.json').write_text(json.dumps(logs,indent=2)+'\n')
  if r.returncode or not rec['matches']:raise SystemExit('Unavailable or changed bytes; investigate the retained capture')
  if sid=='E1':
   with zipfile.ZipFile(dest) as z:
    if z.namelist()!=['p25i6.dta']:raise ValueError('Unexpected archive members')
    data=z.read('p25i6.dta')
    expected=s['retrieval']['extracted'][0]['sha256']
    if hashlib.sha256(data).hexdigest()!=expected:raise ValueError('Unexpected Stata bytes')
    (a.destination/'p25i6.dta').write_bytes(data)
  print(sid,'verified')
if __name__=='__main__':main()

