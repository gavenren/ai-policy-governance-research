"""Optional check of retained source bytes, distinct from offline calculations."""
import argparse,hashlib,json,re
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument('--repository',type=Path,default=Path('.'));a=p.parse_args()
study=Path(__file__).resolve().parents[1]
records=json.loads((study/'sources/manifest.json').read_text());checked=[]
for r in records:
 for path_key,hash_key in [('retained_original_path','sha256'),('extracted_path','extracted_sha256')]:
  if path_key in r:
   f=a.repository/r[path_key]
   assert hashlib.sha256(f.read_bytes()).hexdigest()==r[hash_key],r['id']
   checked.append(str(f))
normalize=lambda s:re.sub(r'\s+',' ',s)
c1=normalize((a.repository/'.local-sources/compute-allocation/C1.txt').read_text())
for quote in ['consistency and composition properties','second term is zero when residual weighted demand vanishes']:assert quote in c1
c2=normalize((a.repository/'.local-sources/compute-allocation/C2.txt').read_text())
assert 'they satisfy neither composition down nor composition up' in c2
metadata=json.loads((a.repository/'.local-sources/compute-allocation/C4.json').read_text())
assert str(metadata['id'])=='21305645' and metadata['metadata']['publication_date']=='2026-07-11'
print(json.dumps({'source_files_checked':len(checked),'source_records':len(records),'quoted_prose_checks':3,'latest_record_in_retained_capture':metadata['id']}))
