#!/usr/bin/env python3
"""Check retained unchanged-script stdout against the saved source-policy rows."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import csv,json,re
BASE=Path(__file__).resolve().parents[1]
with (BASE/'results/summary.csv').open() as f:
    rows={(r['cohort'],r['policy'],int(r['year'])):r for r in csv.DictReader(f)}
checks=[]
for cohort,policy,years,marker,fields in [
    ('ten','trigger',10,'Rev P10',[(2,'revenue_p50_billion','.2f'),(5,'outflow_p50_billion','.2f'),(6,'gap_p50_billion','+.2f')]),
    ('twenty','fixed',20,'Rev P50',[(0,'revenue_p50_billion','.2f'),(1,'outflow_p50_billion','.2f'),(2,'gap_p50_billion','+.2f'),(3,'gap_p10_billion','+.2f'),(4,'gap_p90_billion','+.2f'),(5,'auto_tax_p50_billion','.2f'),(6,'vat_p50_billion','.2f')])]:
    lines=(BASE/f'logs/source-{cohort}-stdout.txt').read_text().splitlines()
    start=next(i for i,line in enumerate(lines) if marker in line)+2
    for year,line in enumerate(lines[start:start+years],1):
        assert int(line.split()[0])==year
        money=re.findall(r'\$\s*([+-]?\d+\.\d+)T',line)
        row=rows[cohort,policy,year]
        for index,field,fmt in fields:
            printed=money[index];rendered=format(float(row[field])/1000,fmt)
            assert printed==rendered,(cohort,year,field,printed,rendered)
            checks.append({'cohort':cohort,'policy':policy,'year':year,'field':field,'source_stdout':printed,'reconstruction':rendered,'matches':True})
        printed=re.search(r'([0-9]+\.[0-9]+)%',line)[1]+'%'
        rendered=format(float(row['surplus_fraction']),'.1%')
        assert printed==rendered,(cohort,year,printed,rendered)
        checks.append({'cohort':cohort,'policy':policy,'year':year,'field':'surplus_fraction','source_stdout':printed,'reconstruction':rendered,'matches':True})
assert len(checks)==200
record={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'checks':200,'all_match':True,'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Retained baseline summary tables only. Existing LVT and other auxiliary stdout are preserved but not audited.','rows':checks}
(BASE/'logs/source-stdout-check.json').write_text(json.dumps(record,indent=2)+'\n')
print('All 200 source-stdout summary checks match.')
