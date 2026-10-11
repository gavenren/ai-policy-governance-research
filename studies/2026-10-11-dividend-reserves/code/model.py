"""Exact deterministic liquidity model. Python standard library only."""
import csv,datetime,hashlib,itertools,json,pathlib,platform
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parents[1]

def read_design():
 return json.loads((HERE/'data/design.json').read_text())

def streams(n,k):
 """All binary shock streams with at most k shocks; no probabilities."""
 return [x for x in itertools.product((0,1),repeat=n) if sum(x)<=k]

def paths(c,family):
 ts=streams(c['horizon'],c['max_tax_shocks']); ds=streams(c['horizon'],c['max_fund_shocks'])
 for tax in ts:
  for div in ds:
   if family=='no_overlap' and any(a and b for a,b in zip(tax,div)):continue
   if family=='common_only' and tax!=div:continue
   yield tax,div

def revenues(c,path):
 tax,div=path
 return [(c['tax_shock'] if a else c['tax_normal'],c['fund_income_shock'] if b else c['fund_income_normal']) for a,b in zip(tax,div)]

def trajectory(c,path,sale,reserve,receipt,haircut,income_loss_start=1):
 """Transfers occur after this period's revenues and scheduled sale receipt."""
 q=F(sale); r=F(reserve); h=F(haircut); A=c['initial_asset_value']
 if not 0<=q<=A:raise ValueError('sale outside initial endowment')
 if receipt<1 or not 0<=h<=1:raise ValueError('invalid sale terms')
 out=[]
 for t,(tax,div) in enumerate(revenues(c,path),1):
  r+=tax+(1-q/A if t>=income_loss_start else 1)*div-c['obligation']
  if t==receipt:r+=(1-h)*q
  out.append(r)
 return out

def need(c,path,sale,receipt,haircut):
 balances=trajectory(c,path,sale,0,receipt,haircut)
 amount=max([F(0)]+[-x for x in balances])
 critical=next((i+1 for i,x in enumerate(balances) if -x==amount),0)
 return amount,critical

def constraints(c,path_list,receipt,haircut,income_loss_start=1):
 """Each line is gap(q)=intercept+slope*q; keep largest intercept per slope."""
 keep={F(0):F(0)}; A=c['initial_asset_value']; h=F(haircut)
 for path in path_list:
  tc=dc=lost_dc=0
  for t,(tax,div) in enumerate(revenues(c,path),1):
   tc+=tax; dc+=div
   if t>=income_loss_start:lost_dc+=div
   b=F(lost_dc,A)-(1-h if t>=receipt else 0)
   a=F(t*c['obligation']-tc-dc)
   keep[b]=max(keep.get(b,a),a)
 return [(a,b) for b,a in sorted(keep.items())]

def reserve(lines,q):return max(a+b*F(q) for a,b in lines)

def optimize(lines,max_sale,loss_weight=0):
 """All pair intersections + endpoints. Smallest sale breaks objective ties."""
 candidates={F(0),F(max_sale)}
 for (a,b),(aa,bb) in itertools.combinations(lines,2):
  if b==bb:continue
  q=(aa-a)/(b-bb)
  if 0<=q<=max_sale:candidates.add(q)
 weight=F(loss_weight)
 q=min(candidates,key=lambda x:(reserve(lines,x)+weight*x,x))
 return q,reserve(lines,q)

def f(x):return format(float(x),'.9f')
def write_csv(path,rows):
 with path.open('w',newline='') as fp:
  w=csv.DictWriter(fp,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 c=read_design(); out=HERE/'results';out.mkdir(exist_ok=True)
 summaries=[]; cases=[]; fronts=[]; objectives=[]; witnesses=[]; timings=[]
 for family in c['families']:
  pp=list(paths(c,family))
  for receipt in c['receipt_periods']:
   for hs in c['haircuts']:
    lines=constraints(c,pp,receipt,hs);q,r=optimize(lines,c['initial_asset_value'])
    summaries.append(dict(family=family,paths=len(pp),receipt_period=receipt,haircut=hs,sale_opt_exact=str(q),reserve_opt_exact=str(r),sale_opt=f(q),reserve_opt=f(r),reserve_no_sale=f(reserve(lines,0)),reserve_sale25=f(reserve(lines,25)),reserve_sale100=f(reserve(lines,100))))
    for qq in c['sale_grid']:
     fronts.append(dict(family=family,receipt_period=receipt,haircut=hs,sale=qq,reserve=f(reserve(lines,qq))))
    if receipt==c['base_receipt_period'] and hs==c['base_haircut']:
     for weight in c['loss_weights']:
      qo,ro=optimize(lines,c['initial_asset_value'],weight)
      objectives.append(dict(family=family,loss_weight=weight,sale_exact=str(qo),reserve_exact=str(ro),objective=f(ro+F(weight)*qo)))
     for i,p in enumerate(pp):
      n,t=need(c,p,q,receipt,hs);n0,t0=need(c,p,0,receipt,hs)
      balances=trajectory(c,p,q,r,receipt,hs)
      assert min(balances)>=0
      cases.append(dict(family=family,path_id=i,tax_shocks=''.join(map(str,p[0])),fund_shocks=''.join(map(str,p[1])),no_sale_reserve=f(n0),no_sale_critical_period=t0,chosen_sale_exact=str(q),chosen_path_reserve=f(n),chosen_critical_period=t,min_cash_at_robust_reserve=f(min(balances)),terminal_cash=f(balances[-1])))
      if n==r and not any(w['family']==family for w in witnesses):
       for tt,bal in enumerate(balances,1):witnesses.append(dict(family=family,period=tt,tax_shock=p[0][tt-1],fund_shock=p[1][tt-1],sale_exact=str(q),initial_reserve_exact=str(r),cash_exact=str(bal),cash=f(bal)))
  for receipt in (2,4):
   for loss_start in (1,receipt):
    lines=constraints(c,pp,receipt,c['base_haircut'],loss_start)
    q,r=optimize(lines,c['initial_asset_value'])
    timings.append(dict(family=family,receipt_period=receipt,income_loss_start=loss_start,sale_exact=str(q),reserve_exact=str(r),reserve_sale100=f(reserve(lines,100))))
  print(family,len(pp),'paths')
 write_csv(out/'summary.csv',summaries);write_csv(out/'path_cases.csv',cases);write_csv(out/'frontiers.csv',fronts);write_csv(out/'objectives.csv',objectives);write_csv(out/'witnesses.csv',witnesses)
 write_csv(out/'timing.csv',timings)
 outputs=['timing.csv','summary.csv','path_cases.csv','frontiers.csv','objectives.csv','witnesses.csv']
 meta=dict(utc=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),python=platform.python_version(),platform=platform.system(),method='complete deterministic enumeration; exact rational calculations; no random sampling',seed=None,input_sha256=sha(HERE/'data/design.json'),code_sha256=sha(pathlib.Path(__file__)),outputs={s:sha(out/s) for s in outputs},path_case_rows=len(cases),summary_rows=len(summaries),exit_status=0)
 (out/'run.json').write_text(json.dumps(meta,indent=2)+'\n')
 print(json.dumps(meta,indent=2))
if __name__=='__main__':main()
