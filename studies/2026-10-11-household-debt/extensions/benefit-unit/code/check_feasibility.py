"""Schema and membership check only. Does not calculate transfer outcomes."""
from pathlib import Path
import argparse, hashlib, json, platform
from datetime import datetime, timezone
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
REL=['X8020','X102','X108','X114','X120','X126','X132','X202','X208','X214','X220','X226']
AGE=['X8022','X104','X110','X116','X122','X128','X134','X204','X210','X216','X222','X228']
DEP=['X8098','X107','X113','X119','X125','X131','X137','X207','X213','X219','X225','X231']
FIELDS=['YY1','Y1','X7001','X7020','X101','X42001']+REL+AGE+DEP
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--full',type=Path,required=True)
 p.add_argument('--selected',type=Path,required=True)
 p.add_argument('--output',type=Path,required=True)
 a=p.parse_args()
 d=pd.read_stata(a.full,columns=[x.lower() for x in FIELDS],convert_categoricals=False)
 d.columns=d.columns.str.upper()
 s=pd.read_csv(a.selected,usecols=['YY1','Y1','WGT'])
 m=s.merge(d,on=['YY1','Y1'],validate='one_to_one',how='outer',indicator=True)
 rel=m[REL].to_numpy()
 ages=m[AGE].to_numpy()
 dep=m[DEP].to_numpy()
 included=dep==1
 alt=included.copy();alt[:,0]=True;alt[:,1]=m.X7020.to_numpy()==2
 counts=included.sum(axis=1)
 adults=((ages>=18)&included).sum(axis=1)
 rows=[]
 for i in range(1,6):
  mask=m.Y1%10==i;sub=m[mask];w=sub.WGT.to_numpy()*5
  rows.append(dict(implicate=i,records=int(mask.sum()),
   roster_count_mismatch=int((counts[mask]!=sub.X7001.to_numpy()).sum()),
   explicit_core_count_mismatch=int((alt[mask].sum(axis=1)!=sub.X7001.to_numpy()).sum()),
   number_size_topcoded=int((sub.X7001==12).sum()),
   number_household_topcoded=int((sub.X101==12).sum()),
   no_included_adult=int((adults[mask]==0).sum()),
   missing_included_age=int(((ages[mask]==0)&included[mask]).sum()),
   member_age_values=sorted(np.unique(ages[mask][included[mask]]).tolist()),
   family_size_counts={str(int(k)):int(v) for k,v in sub.X7001.value_counts().sort_index().items()},
   adults_counts={str(int(k)):int(v) for k,v in pd.Series(adults[mask]).value_counts().sort_index().items()},
   mean_size=float(np.average(sub.X7001,weights=w)),
   mean_adults=float(np.average(adults[mask],weights=w)),
   weight_sum=float(w.sum())))
 result=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),python=platform.python_version(),numpy=np.__version__,pandas=pd.__version__,
  full_sha256=sha(a.full),selected_sha256=sha(a.selected),code_sha256=sha(__file__),
  public_rows=len(d),families=int(d.YY1.nunique()),join_counts={str(k):int(v) for k,v in m._merge.value_counts().items()},
  full_vs_summary_weight_max_abs=float(abs(m.X42001-m.WGT*5).max()),
  included_without_relationship=int(((rel==0)&included).sum()),unknown_dependency_codes=sorted(set(np.unique(dep))-{0,1,5}),
  core_membership_disagreements=int((included!=alt).sum()),
  implicates=rows,scope='Feasibility only: public schema, join and member counts. No transfer, floor, debt outcome or policy ranking calculated.')
 a.output.parent.mkdir(parents=True,exist_ok=True)
 a.output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()

