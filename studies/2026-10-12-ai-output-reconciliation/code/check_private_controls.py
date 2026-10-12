#!/usr/bin/env python3
"""Read an existing private extraction for the source's geometric-power control."""
from pathlib import Path
import argparse,hashlib,importlib,json,sys,contextlib,io,math
from datetime import datetime,timezone
STUDY=Path(__file__).resolve().parents[1];REPO=STUDY.parents[1]
p=argparse.ArgumentParser();p.add_argument('--run-id',default='run-01');args=p.parse_args()
source=REPO/'.local-sources/ai-output-reconciliation'/args.run_id/'replication'
meta=json.loads((STUDY/'logs'/f'execution-{args.run_id}.json').read_text())
for name in ['calculations.py','config.py']:
 assert hashlib.sha256((source/name).read_bytes()).hexdigest()==meta['unchanged_members_before'][name]
sys.dont_write_bytecode=True;sys.path.insert(0,str(source));calc=importlib.import_module('calculations')
# Same first two totals, with the third exactly on their geometric path.
first=28.7e12;ratio=72.3/28.7;annual=[first,first*ratio,first*ratio**2]
out=io.StringIO()
with contextlib.redirect_stdout(out):monthly=calc.annual_to_monthly_with_growth(annual)
rows=[]
for i,y in enumerate([2023,2024,2025]):
 total=float(monthly.loc[str(y)].sum());scale=annual[i]/total
 assert math.isclose(total,annual[i],rel_tol=2e-14)
 assert math.isclose(scale,1,rel_tol=2e-14)
 rows.append({'year':y,'geometric_annual_Wh':annual[i],'generated_Wh':total,'annual_preserving_scale':scale})
assert 'Warning' not in out.getvalue()
result={'checked_utc':datetime.now(timezone.utc).isoformat(),'control':'geometrically consistent annual totals','status':'passed',
        'scope':'diagnostic positive control, not a fifth empirical accounting case','source_run_id':args.run_id,
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_stdout':out.getvalue(),'rows':rows}
(STUDY/'logs/numerical-private-control.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
