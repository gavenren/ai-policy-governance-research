"""Two-date acquisition and guarantee accounting; exact rational arithmetic."""
import pathlib,json,csv,hashlib,datetime,platform,itertools
from fractions import Fraction as F
ROOT=pathlib.Path(__file__).resolve().parents[1]
def design():return json.loads((ROOT/'data/design.json').read_text())
def unpack(c):
 m=list(map(F,c['prices']));p=list(map(F,c['probabilities']));y=list(map(F,c['payoffs']));t=list(map(F,c['taxes']))
 assert len(m)==len(p)==len(y)==len(t) and all(x>0 for x in m) and sum(p)==1
 assert all(x>=0 for x in y+t+p)
 return m,p,y,t,1/sum(m),sum(a*b for a,b in zip(m,y))
def balances(c,alpha,capital):
 m,p,y,t,r,price=unpack(c);a=F(alpha);C=F(capital)
 assert 0<=a<=1 and C>=0
 debt=max(a*price-C,F(0));safe=max(C-a*price,F(0))
 return [a*x+r*safe-r*debt+tax for x,tax in zip(y,t)]
def capital_need(c,alpha):
 m,p,y,t,r,price=unpack(c);a=F(alpha)
 return max([F(0)]+[(F(c['floor'])-tax-a*(x-r*price))/r for x,tax in zip(y,t)])
def guaranteed_without_capital(c,alpha):return min(balances(c,alpha,0))
def best_hedge(c):
 m,p,y,t,r,price=unpack(c);k=[x-r*price for x in y];cand={F(0),F(1)}
 for i,j in itertools.combinations(range(len(y)),2):
  if k[i]!=k[j]:
   a=(t[j]-t[i])/(k[i]-k[j])
   if 0<=a<=1:cand.add(a)
 a=min(cand,key=lambda z:(-guaranteed_without_capital(c,z),z))
 return a,guaranteed_without_capital(c,a)
def fmt(x):return format(float(x),'.9f')
def save(name,rows):
 with (ROOT/'results'/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 d=design();policies=[];states=[];summary=[]
 for c in d['scenarios']:
  m,p,y,t,r,price=unpack(c);a,g=best_hedge(c);C=capital_need(c,a)
  summary.append(dict(scenario=c['name'],fair_price=str(price),safe_return=str(r),physical_expected_payoff=str(sum(x*z for x,z in zip(p,y))),outside_tax_value=str(sum(x*z for x,z in zip(m,t))),best_hedge_share=str(a),max_floor_without_initial_capital=str(g),capital_for_target_at_best_hedge=str(C),target=c['floor']))
  for alpha in sorted(set(map(F,d['ownership_grid']))|{a}):
   need=capital_need(c,alpha);zero=balances(c,alpha,0);funded=balances(c,alpha,need)
   assert min(funded)>=c['floor']
   pv=sum(x*z for x,z in zip(m,funded));assert pv==need+sum(x*z for x,z in zip(m,t))
   policies.append(dict(scenario=c['name'],share=str(alpha),minimum_initial_capital=str(need),no_capital_worst=str(min(zero)),no_capital_expected=str(sum(x*z for x,z in zip(p,zero))),funded_worst=str(min(funded)),debt_at_issue=str(max(alpha*price-need,F(0))),safe_deposit=str(max(need-alpha*price,F(0))),seller_receipt=str(alpha*price)))
   for i,(z,b) in enumerate(zip(zero,funded)):
    states.append(dict(scenario=c['name'],share=str(alpha),state=i,state_price=str(m[i]),probability=str(p[i]),asset_payoff=str(y[i]),outside_taxes=str(t[i]),balance_without_capital=str(z),balance_with_minimum_capital=str(b)))
 save('summary.csv',summary);save('policies.csv',policies);save('states.csv',states)
 c=d['scenarios'][0];m,p,y,t,r,P=unpack(c);default=[]
 for face in d['default_faces']:
  debt=[min(F(face),x) for x in y];equity=[x-z for x,z in zip(y,debt)]
  debt_price=sum(x*z for x,z in zip(m,debt));eqprice=sum(x*z for x,z in zip(m,equity));assert debt_price+eqprice==P
  default.append(dict(face=face,fair_debt_proceeds=str(debt_price),purchase_funding_gap=str(P-debt_price),equity_value=str(eqprice),physical_expected_equity=str(sum(x*z for x,z in zip(p,equity)))))
 save('default.csv',default)
 sensitivity=[]
 for high in map(F,d['physical_probability_grid']):
  c=dict(c,probabilities=[str(1-high),str(high)])
  sensitivity.append(dict(high_state_probability=str(high),expected_surplus=str(sum(x*z for x,z in zip(map(F,c['probabilities']),balances(c,1,0)))),required_capital=str(capital_need(c,1))))
 save('probabilities.csv',sensitivity)
 outputs=['summary.csv','policies.csv','states.csv','default.csv','probabilities.csv']
 meta=dict(utc=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),python=platform.python_version(),method='complete specified finite-state enumeration; exact Fraction arithmetic',seed=None,policy_rows=len(policies),state_rows=len(states),input_sha256=sha(ROOT/'data/design.json'),code_sha256=sha(pathlib.Path(__file__)),outputs={s:sha(ROOT/'results'/s) for s in outputs},exit_status=0)
 (ROOT/'results/run.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta,indent=2))
if __name__=='__main__':main()
