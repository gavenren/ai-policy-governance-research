"""A specified repeated transfer agreement, not a solver for all repeated-game equilibria."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, itertools, json, math, platform
BASE=Path(__file__).resolve().parents[1]
TOL=1e-9

def solve(matrix, rhs):
    a=[list(map(float,row))+[float(v)] for row,v in zip(matrix,rhs)]
    n=len(rhs)
    for j in range(n):
        k=max(range(j,n),key=lambda i: abs(a[i][j]))
        if abs(a[k][j])<1e-14: raise ValueError('singular matrix')
        a[j],a[k]=a[k],a[j]
        v=a[j][j];a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]

def validate(c):
    n=len(c['gain'])
    vectors=['gain','cost','own_income','provider_resources','domestic_minimum']
    if n<1 or any(len(c[k])!=n for k in vectors):raise ValueError('inconsistent vectors')
    nums=[c[k] for k in ['discount','population','bond_cap','carry_cost']]+[v for k in vectors for v in c[k]]
    if not all(math.isfinite(v) for v in nums):raise ValueError('non-finite input')
    if not 0<=c['discount']<1 or c['population']<=0 or c['bond_cap']<0 or c['carry_cost']<0:raise ValueError('invalid scalar')
    if any(v<0 for k in vectors for v in c[k]):raise ValueError('negative resource or cost')
    p=c.get('transition')
    if p is None:
        q=c['persistence']
        if n!=2 or not math.isfinite(q) or not 0<=q<=1:raise ValueError('invalid persistence')
        p=[[q,1-q],[1-q,q]]
    if len(p)!=n or any(len(row)!=n or any(not math.isfinite(x) or x<0 for x in row) or abs(sum(row)-1)>1e-10 for row in p):raise ValueError('invalid transition')
    return p

def assess(c, floor, bond=0):
    p=validate(c);d=c['discount'];r=c['carry_cost'];n=len(p)
    if not math.isfinite(floor) or floor<0 or not math.isfinite(bond) or not 0<=bond<=c['bond_cap']+TOL:raise ValueError('invalid policy')
    t=[cost+max(0,c['population']*floor-y) for cost,y in zip(c['cost'],c['own_income'])]
    g=[k-pay-r*bond for k,pay in zip(c['gain'],t)]
    v=solve([[(1 if i==j else 0)-d*p[i][j] for j in range(n)] for i in range(n)],g)
    continuation=[d*sum(prob*x for prob,x in zip(row,v)) for row in p]
    margins=[bond+cv-pay for cv,pay in zip(continuation,t)]
    domestic=[a+k-pay-r*bond-m for a,k,pay,m in zip(c['provider_resources'],c['gain'],t,c['domestic_minimum'])]
    household=[y+pay-cost for y,pay,cost in zip(c['own_income'],t,c['cost'])]
    recipient_net=[pay-cost for pay,cost in zip(t,c['cost'])]
    return dict(transfers=t,provider_net=g,provider_value=v,continuation=continuation,enforcement_margin=margins,domestic_margin=domestic,household_resources=household,recipient_net=recipient_net,feasible=min(v+ margins+domestic)>=-TOL)

def bond_interval(c,floor):
    """Exact affine bounds apart from floating arithmetic. Return a feasible interval or None."""
    a=assess(c,floor);d=c['discount'];r=c['carry_cost'];effect=1-d*r/(1-d)
    lo=0.;hi=c['bond_cap']
    for v in a['provider_value']:
        if r>0:hi=min(hi,v*(1-d)/r)
        elif v < -TOL:return None
    for margin in a['domestic_margin']:
        if r>0:hi=min(hi,margin/r)
        elif margin < -TOL:return None
    for margin in a['enforcement_margin']:
        if effect>1e-12:lo=max(lo,-margin/effect)
        elif effect < -1e-12:hi=min(hi,margin/(-effect))
        elif margin < -TOL:return None
    if lo>hi+TOL or hi < -TOL:return None
    return max(0,lo),max(0,hi)

def maximum_floor(c):
    if bond_interval(c,0) is None:return None
    # This is an upper bound from the domestic budget with a zero carrying cost.
    hi=max(0,min((y+a+k-m-cost)/c['population'] for y,a,k,m,cost in zip(c['own_income'],c['provider_resources'],c['gain'],c['domestic_minimum'],c['cost'])))+1
    lo=0
    for _ in range(75):
        mid=(lo+hi)/2
        if bond_interval(c,mid) is not None:lo=mid
        else:hi=mid
    return lo

def row(c,name):
    target=c['target_floor'];iv=bond_interval(c,target);a=assess(c,target,iv[0] if iv else 0)
    return dict(name=name,discount=c['discount'],persistence=c['persistence'],adverse_gain=c['gain'][1],domestic_minimum=c['domestic_minimum'][0],provider_resources=c['provider_resources'][0],bond_cap=c['bond_cap'],carry_cost=c['carry_cost'],target_floor=target,maximum_floor=maximum_floor(c),target_feasible=iv is not None,least_bond=iv[0] if iv else None,largest_bond=iv[1] if iv else None,mean_net_before_bond=sum(k-t for k,t in zip(c['gain'],a['transfers']))/2,min_provider_value=min(a['provider_value']),min_enforcement_margin=min(a['enforcement_margin']),min_domestic_margin=min(a['domestic_margin']),bond_marginal_enforcement=1-c['discount']*c['carry_cost']/(1-c['discount']))

def write_csv(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    design_path=BASE/'data/design.json';design=json.loads(design_path.read_text());base=design['base'];named=[];details=[]
    for change in design['named']:
        c={**base,**change};named.append(row(c,c['name']))
        for bond in sorted(set([0,c['bond_cap']]+([bond_interval(c,c['target_floor'])[0]] if bond_interval(c,c['target_floor']) else []))):
            result=assess(c,c['target_floor'],bond)
            for i in range(2):details.append(dict(name=c['name'],state=i,bond=bond,**{key:val[i] for key,val in result.items() if isinstance(val,list)}))
    grid=[];keys=list(design['grid'])
    for i,values in enumerate(itertools.product(*(design['grid'][k] for k in keys))):
        changes=dict(zip(keys,values));c={**base,**changes};c['gain']=[12,changes['adverse_gain']];c['domestic_minimum']=[changes['domestic_minimum']]*2
        grid.append(row(c,'grid_'+str(i)))
    persistence=[]
    for q in [i/100 for i in range(0,101)]:
        c={**base,'persistence':q};persistence.append(row(c,'p_'+str(q)))
    out=BASE/'results';out.mkdir(exist_ok=True)
    for fname,rows in [('named.csv',named),('state_details.csv',details),('grid.csv',grid),('persistence.csv',persistence)]:write_csv(out/fname,rows)
    summary=dict(grid_cases=len(grid),target_feasible=sum(r['target_feasible'] for r in grid),positive_average_but_target_infeasible=sum(r['mean_net_before_bond']>0 and not r['target_feasible'] for r in grid),no_agreement_even_at_zero_floor=sum(r['maximum_floor'] is None for r in grid),named=named)
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    hashes={str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [design_path,Path(__file__)]+sorted(out.glob('*.csv'))}
    (out/'run.json').write_text(json.dumps(dict(executed_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),python=platform.python_version(),command='python3 studies/2026-10-11-international-dividend/code/model.py',exit_status=0,input_and_output_sha256=hashes,randomness='none',method='linear system; affine deposit intervals; 75-step floor bisection'),indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='named'}));print(json.dumps(named,indent=2))

if __name__=='__main__':main()
