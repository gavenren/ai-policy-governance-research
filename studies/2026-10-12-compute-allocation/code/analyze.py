"""Exact, offline audit of a pinned compute-allocation formula."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import platform

ROOT = Path(__file__).resolve().parents[1]


def inputs(claims, weights, budget):
    d, w, b = tuple(map(F, claims)), tuple(map(F, weights)), F(budget)
    if not d or len(d) != len(w) or min(d) < 0 or min(w) <= 0 or b < 0:
        raise ValueError('Need nonnegative claims and budget, positive weights, matching nonempty vectors')
    return d, w, b


def raw(claims, weights, budget):
    d, w, b = inputs(claims, weights, budget)
    denominator = sum(x*y for x,y in zip(d,w))
    # This extension is the source's explicit residual-demand convention.
    return tuple(b*x*y/denominator for x,y in zip(d,w)) if denominator else (F(0),)*len(d)


def capped(claims, weights, budget):
    d, w, b = inputs(claims, weights, budget)
    remaining = min(b, sum(d))
    awards = [F(0)]*len(d)
    active = {i for i,x in enumerate(d) if x > 0}
    while active and remaining:
        scale = remaining / sum(w[i]*d[i] for i in active)
        full = {i for i in active if scale*w[i] >= 1}
        if not full:
            for i in active:
                awards[i] = scale*w[i]*d[i]
            remaining = F(0)
        else:
            for i in full:
                awards[i] = d[i]
                remaining -= d[i]
            active -= full
    return tuple(awards), b-sum(awards)


def floor_awards(demand, weights, capacity, floors, cap=False):
    d, w, c = inputs(demand, weights, capacity)
    u = tuple(map(F, floors))
    if len(u) != len(d) or min(u) < 0:
        raise ValueError('Need one nonnegative floor per claimant')
    b = c - sum(u)
    if b < 0:
        raise ValueError('Protected floor exceeds capacity')
    residual = tuple(max(F(0), x-y) for x,y in zip(d,u))
    z = capped(residual,w,b)[0] if cap else raw(residual,w,b)
    a = tuple(x+y for x,y in zip(u,z))
    return a, c-sum(a)


def string_vector(values):
    return '|'.join(map(str,values))


def encode(value):
    if isinstance(value,F): return str(value)
    if isinstance(value,(tuple,list)): return [encode(v) for v in value]
    if isinstance(value,dict): return {k:encode(v) for k,v in value.items()}
    return value


def named_results(cases):
    out = {}
    for case in cases['allocations']:
        d,w,b=case['claims'],case['weights'],case['budget']
        c,unused=capped(d,w,b)
        out[case['id']]={'raw':raw(d,w,b),'capped':c,'capped_unused':unused}
    for case in cases['floors']:
        args=case['demands'],case['weights'],case['capacity'],case['floors']
        out[case['id']]={name:floor_awards(*args,cap=cap) for name,cap in [('raw',False),('capped',True)]}
    d,w=(F(2),F(2)),(F(2,3),F(1,3))
    small,large=raw(d,w,1),raw(d,w,2)
    leftover=tuple(x-y for x,y in zip(d,small))
    out['composition']={'claims':d,'weights':w,'small':small,'large':large,'down':raw(large,w,1),'up':tuple(x+y for x,y in zip(small,raw(leftover,w,1))),'fixed_claim_sum':tuple(2*x for x in small),'remaining_claims':leftover,'cap_inactive_in_each_problem':all(capped(a,w,b)[0]==raw(a,w,b) for a,b in [(d,1),(d,2),(large,1),(leftover,1)])}
    d,w=(F(2),F(3),F(5)),(F(1,2),F(1,3),F(1,6))
    all_awards=raw(d,w,4)
    out['subset_consistency']={'all':all_awards,'remaining_indices':[0,2],'reapplied':raw((d[0],d[2]),(w[0],w[2]),all_awards[0]+all_awards[2])}
    return encode(out)


def run():
    cases=json.loads((ROOT/'data/raw/cases.json').read_text())
    output=ROOT/'results';output.mkdir(exist_ok=True)
    named=named_results(cases)
    (output/'named-cases.json').write_text(json.dumps(named,indent=2)+'\n')
    rows=[]
    for d in product([1,2,5],repeat=2):
        for initial_w in product([1,2,4],repeat=2):
            w=tuple(F(x,sum(initial_w)) for x in initial_w)
            for fraction in map(F,['0','1/4','1/2','3/4','1','5/4']):
                b=fraction*sum(d);a=raw(d,w,b);z,idle=capped(d,w,b)
                threshold=sum(x*y for x,y in zip(d,w))/max(w)
                bounds=all(x<=y for x,y in zip(a,d))
                assert bounds==(b<=threshold)
                assert sum(a)==b
                assert sum(z)==min(b,sum(d)) and idle==max(F(0),b-sum(d))
                assert all(0<=x<=y for x,y in zip(z,d))
                if bounds:assert a==z
                rows.append({'claims':string_vector(d),'weights':string_vector(w),'budget_fraction':str(fraction),'budget':str(b),'raw_awards':string_vector(a),'raw_within_claims':bounds,'raw_sum':str(sum(a)),'threshold':str(threshold),'capped_awards':string_vector(z),'unused_capacity':str(idle),'domain':'surplus' if b>sum(d) else 'shortage_or_equal'})
    with (output/'grid.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    summary={'rows':len(rows),'raw_within_claims':sum(r['raw_within_claims'] for r in rows),'raw_exceeds_a_claim':sum(not r['raw_within_claims'] for r in rows),'shortage_or_equal_exceedances':sum(not r['raw_within_claims'] and r['domain']=='shortage_or_equal' for r in rows),'surplus_rows':sum(r['domain']=='surplus' for r in rows),'all_capped_bounds_and_budget_checks_pass':True,'interpretation':'Selected finite grid; counts are not real-world prevalence.'}
    (output/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    tracked=['protocol.md','data/raw/cases.json','code/analyze.py','code/test_analysis.py','results/named-cases.json','results/grid.csv','results/summary.json']
    metadata={'run_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),'python':platform.python_version(),'arithmetic':'fractions.Fraction, exact rational numbers','network_used':False,'command':'python3 studies/2026-10-12-compute-allocation/code/analyze.py','sha256':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in tracked}}
    (output/'run-metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':run()
