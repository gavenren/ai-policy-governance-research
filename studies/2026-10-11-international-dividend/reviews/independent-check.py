"""Independent exact two-state check. Does not import the study model."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, itertools, json
BASE = Path(__file__).resolve().parents[1]

def f(x):
    return F(str(x))

def direct(c, floor, deposit):
    d, q, r, n = (f(c[k]) for k in ['discount', 'persistence', 'carry_cost', 'population'])
    transfers = [f(cost) + max(F(0), n*floor-f(y)) for cost,y in zip(c['cost'], c['own_income'])]
    gain = [f(k)-t-r*deposit for k,t in zip(c['gain'], transfers)]
    mean = sum(gain)/2/(1-d)
    contrast = (gain[0]-gain[1])/2/(1-d*(2*q-1))
    value = [mean+contrast, mean-contrast]
    future = [d*(q*value[0]+(1-q)*value[1]), d*((1-q)*value[0]+q*value[1])]
    # Compliance and payment-default payoffs include the current gain.
    compliance = [k-t-r*deposit+v for k,t,v in zip(map(f,c['gain']), transfers, future)]
    default = [k-r*deposit-deposit for k in map(f,c['gain'])]
    margins = [x-y for x,y in zip(compliance,default)]
    domestic = [f(a)+f(k)-t-r*deposit-f(m) for a,k,t,m in zip(c['provider_resources'],c['gain'],transfers,c['domestic_minimum'])]
    assert compliance == value
    return value, margins, domestic

def candidates(c, floor):
    cap = f(c['bond_cap'])
    at_zero = sum(direct(c,floor,F(0)),[])
    at_one = sum(direct(c,floor,F(1)),[])
    points = {F(0),cap}
    for a,b in zip(at_zero,at_one):
        if b != a:
            root = -a/(b-a)
            if 0 <= root <= cap: points.add(root)
    points = sorted(points)
    points += [(a+b)/2 for a,b in zip(points,points[1:])]
    return [b for b in points if min(sum(direct(c,floor,b),[])) >= 0]

def main():
    design = json.loads((BASE/'data/design.json').read_text())
    base = design['base']
    saved = list(csv.DictReader((BASE/'results/grid.csv').open()))
    mismatches=[]; passed=0
    for i, values in enumerate(itertools.product(*design['grid'].values())):
        changes=dict(zip(design['grid'],values));c={**base,**changes}
        c['gain']=[12,changes['adverse_gain']]
        c['domestic_minimum']=[changes['domestic_minimum']]*2
        feasible=bool(candidates(c,f(c['target_floor'])))
        passed+=feasible
        if feasible != (saved[i]['target_feasible']=='True'):mismatches.append(i)
    persistent={**base,'persistence':.95}
    cheap={**persistent,'bond_cap':12,'carry_cost':.05}
    exact={}
    for name,c,limit in [('independent',base,F(39,5)),('persistent',persistent,F(183,35)),('cheap_deposit',cheap,F(43,7))]:
        assert candidates(c,limit)
        assert not candidates(c,limit+F(1,10**6))
        exact[name+'_maximum_floor']=str(limit)
    value,margins,domestic=direct(persistent,F(6),F(0))
    assert value[1]==F(15,7) and margins[1]==-F(27,7)
    feasible_points=candidates(cheap,F(6))
    assert min(feasible_points)==F(135,28) and max(feasible_points)==F(60,7)
    assert min(direct(cheap,F(6),F(12))[0]) < 0
    equal_discount_cost={**persistent,'bond_cap':12,'carry_cost':.25}
    assert direct(equal_discount_cost,F(6),F(0))[1] == direct(equal_discount_cost,F(6),F(12))[1]
    report={'executed_utc':datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),'method':'Exact two-state mean/contrast values and direct compliance-minus-default payoffs; finite roots and midpoints for affine constraints. No import of author model.','grid_rows_checked':len(saved),'feasible_target_cases':passed,'mismatches':mismatches,'exact_floor_boundaries':exact,'persistent_adverse_value':str(value[1]),'persistent_adverse_payment_margin':str(margins[1]),'floor_six_deposit_interval':[str(min(feasible_points)),str(max(feasible_points))],'deposit_12_participation_fails':True,'loan_discount_break_even_checked':True,'input_sha256':hashlib.sha256((BASE/'data/design.json').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    assert len(saved)==648 and passed==292 and not mismatches
    (BASE/'reviews/independent-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
