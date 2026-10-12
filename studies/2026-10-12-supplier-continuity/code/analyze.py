"""Offline candidate enumeration. Structural coverage is not operational continuity."""
import csv, hashlib, itertools, json, platform
from pathlib import Path
from datetime import date, datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
READINESS=('task_qualified','reserved_capacity','tested_switching','service_data_access','permission_for_hypothetical_use','other_infrastructure_independence')
def read_rows():
    with (ROOT/'data/deployments.csv').open(newline='') as f: return list(csv.DictReader(f))
def within_announced_horizon(row,horizon):
    end=row['exact_support_retirement_date']
    return end=='unknown' or date.fromisoformat(end)>date.fromisoformat(horizon)
def coverage(pair, universe, eligible_ids=None):
    pool=[x for x in pair if eligible_ids is None or x['deployment_id'] in eligible_ids]
    model_tests={m:any(r['model_label']!=m for r in pool) for m in sorted({r['model_label'] for r in universe})}
    platform_tests={p:any(r['platform_label']!=p for r in pool) for p in sorted({r['platform_label'] for r in universe})}
    return {'model_pass':all(model_tests.values()),'platform_pass':all(platform_tests.values()),
            'joint_pass':all(model_tests.values()) and all(platform_tests.values()),
            'model_tests':model_tests,'platform_tests':platform_tests}
def analyze(rows):
    horizons={'incumbent_candidate_benchmark':{x['deployment_id'] for x in rows},
              'new_buyer_lifecycle_gate':{x['deployment_id'] for x in rows if x['documented_stage']!='Legacy'},
              'announced_support_2026_10_21':{x['deployment_id'] for x in rows if within_announced_horizon(x,'2026-10-21')},
              'new_buyer_and_support_2026_10_21':{x['deployment_id'] for x in rows if x['documented_stage']!='Legacy' and within_announced_horizon(x,'2026-10-21')},
              'claude_only_task_sensitivity':{x['deployment_id'] for x in rows if x['model_label']=='Claude Sonnet 4.5'},
              'shared_dependency_loss_sensitivity':set()}
    results=[]
    details={}
    for name,eligible in horizons.items():
        for pair in itertools.combinations(rows,2):
            key=''.join(x['deployment_id'] for x in pair)
            test=coverage(pair,rows,eligible)
            results.append({'case':name,'pair':key,
                'remaining_candidates':','.join(x['deployment_id'] for x in pair if x['deployment_id'] in eligible),
                'two_platform_labels':len({x['platform_label'] for x in pair})>=2,
                'two_model_labels':len({x['model_label'] for x in pair})>=2,
                'model_pass':test['model_pass'],'platform_pass':test['platform_pass'],'joint_pass':test['joint_pass'],
                'operational_continuity':'unverified'})
            details[name+':'+key]={'eligible_ids':sorted(eligible),**test}
    summary={'deployment_count':len(rows),'pair_count':len(list(itertools.combinations(rows,2))),
        'readiness_unknown_cells':sum(r[k]=='unknown' for r in rows for k in READINESS),
        'exact_retirement_unknown_rows':sum(r['exact_support_retirement_date']=='unknown' for r in rows),
        'cases':{n:{k:[r['pair'] for r in results if r['case']==n and r[k]] for k in ('model_pass','platform_pass','joint_pass')} for n in horizons}}
    return results,details,summary
def main():
    rows=read_rows();results,details,summary=analyze(rows)
    out=ROOT/'results';out.mkdir(exist_ok=True)
    with (out/'pairs.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(results[0]));writer.writeheader();writer.writerows(results)
    (out/'scenario-detail.json').write_text(json.dumps(details,indent=2,sort_keys=True)+'\n')
    (out/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    paths=['data/deployments.csv','code/analyze.py','results/pairs.csv','results/scenario-detail.json','results/summary.json']
    run={'run_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'python':platform.python_version(),
         'command':'python3 code/analyze.py (from study directory)','exit_status':0,
         'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    (out/'run.json').write_text(json.dumps(run,indent=2)+'\n')
    print(json.dumps(summary))
if __name__=='__main__': main()

