"""Validate saved evidence, public outputs and original-file preservation."""
from pathlib import Path
import argparse,csv,hashlib,json,re
import numpy as np
import pandas as pd
from analyze import derive_members,combine

ROOT=Path(__file__).resolve().parents[1]
STUDY=ROOT.parents[1]
REPO=ROOT.parents[3]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--local-evidence',action='store_true');a=p.parse_args()
 manifest=json.loads((ROOT/'sources/manifest.json').read_text())
 run=json.loads((ROOT/'results/run.json').read_text())
 assert sha(ROOT/'protocol.md')==run['protocol_sha256']
 assert sha(ROOT/'data/roster.csv')==run['roster_sha256']
 assert sha(STUDY/'data/scf2025-selected.csv')==run['selected_sha256']
 assert sha(ROOT/'code/analyze.py')==run['analysis_sha256']
 derive_members(pd.read_csv(ROOT/'data/roster.csv'))
 preserved=json.loads((ROOT/'logs/original-file-hashes.json').read_text())['files']
 checked=0
 for name,h in preserved.items():
  if name in ('paper.md','README.md'):continue
  assert sha(STUDY/name)==h,name;checked+=1
 for row in manifest['records']:
  e=row['public_evidence'];assert sha(ROOT/e['path'])==e['sha256']
 quotes=list(csv.DictReader((ROOT/'sources/extracts.csv').open()))
 for row in quotes:
  assert len(row['quote'].split())==int(row['word_count'])
 for sid in {x['source_id'] for x in quotes}:
  assert sum(int(x['word_count']) for x in quotes if x['source_id']==sid)<=25
 imp=pd.read_csv(ROOT/'results/implicate-estimates.csv',index_col='implicate')
 rep=pd.read_csv(ROOT/'results/replicate-estimates.csv',index_col='replicate')
 assert imp.shape==(5,192) and rep.shape==(999,192) and list(imp.columns)==list(rep.columns)
 point,se=combine(imp.to_numpy(),rep.to_numpy())
 allrows=pd.concat([pd.read_csv(ROOT/'results'/f'{t}.csv') for t in ['outcomes','contrasts','allocation']]).set_index('key').loc[imp.columns]
 np.testing.assert_allclose(allrows.estimate,point,rtol=1e-10,atol=1e-10)
 np.testing.assert_allclose(allrows.standard_error,se,rtol=1e-10,atol=1e-10)
 for frame in [imp,rep]:
  for sample in ['exact','capped']:
   base=frame[f'{sample}/allocation/family/annual_total']
   for arm in ['adult','size']:
    np.testing.assert_allclose(frame[f'{sample}/allocation/{arm}/annual_total'],base,rtol=1e-12)
  for key in frame.columns:
   if key.endswith('/all/gross_pass'):
    stem=key.removesuffix('gross_pass')
    np.testing.assert_allclose(frame[key]-frame[stem+'after_pass'],frame[stem+'classification_gap'],atol=1e-12)
 local_files=0
 if a.local_evidence:
  texts={}
  for row in manifest['records']:
   for item in [row.get('original'),row.get('representation'),row.get('extraction')]:
    if item:
     f=REPO/item['local_path'];assert sha(f)==item['sha256'],str(f);local_files+=1
   q=row.get('extraction',row['original'])
   if str(q['local_path']).endswith('.txt'):texts[row['source_id']]=' '.join((REPO/q['local_path']).read_text().split())
  for row in quotes:assert ' '.join(row['quote'].split()) in texts[row['source_id']],row['source_id']
  searches=json.loads((ROOT/'logs/searches.json').read_text())
  for row in searches['records']:assert sha(REPO/row['private_tool_response'])==row['sha256']
 print(json.dumps(dict(original_files_preserved=checked,estimands=192,replicates=999,source_records=len(manifest['records']),short_quotes=len(quotes),local_files_checked=local_files,passed=True)))
if __name__=='__main__':main()

