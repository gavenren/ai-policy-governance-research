"""Static import-levy model. Standard library only; synthetic inputs."""
import csv, datetime, hashlib, itertools, json, math, pathlib, platform
from dataclasses import dataclass, replace, asdict
ROOT=pathlib.Path(__file__).resolve().parents[1]
EPS=1e-9
@dataclass(frozen=True)
class State:
    name:str='base'; A:float=14.; c:float=4.; b:float=1.; d:float=.25
    theta:float=.25; efficiency:float=1.; fixed_cost:float=0.; recipients:float=.8
    def __post_init__(self):
        if not all(math.isfinite(v) for k,v in asdict(self).items() if k!='name'): raise ValueError('Non-finite parameter')
        if not (self.A>self.c>=0 and self.b>0 and self.d>=0): raise ValueError('Invalid production/supply')
        if not (0<=self.theta<1 and 0<self.efficiency<=1 and self.fixed_cost>=0 and 0<self.recipients<1): raise ValueError('Invalid fiscal/population parameter')
    @property
    def slope(self): return self.b+self.d
    @property
    def q0(self): return (self.A-self.c)/self.slope
    @property
    def passthrough(self): return self.b/self.slope
    @property
    def choke(self): return self.A-self.c

def allocation(s,t):
    if not math.isfinite(t) or t<0 or t>s.choke+EPS: raise ValueError('Tax outside [0, choke]')
    q=max(0.,(s.A-s.c-t)/s.slope);p=s.c+s.d*q
    value=s.A*q-s.b*q*q/2
    profit=s.b*q*q/2
    gross=s.efficiency*t*q
    variable_cost=(1-s.efficiency)*t*q
    fixed=s.fixed_cost if t>0 else 0.
    revenue=s.theta*profit+gross-fixed
    owner=(1-s.theta)*profit
    domestic=owner+revenue
    # A transfer cancels within the domestic budget. No income is created twice.
    return dict(tax=t,imports=q,foreign_price=p,user_price=p+t,output=value,domestic_profit=profit,
      gross_levy_payments=t*q,usable_levy_receipts=gross,collection_resource_cost=variable_cost,fixed_cost_paid=fixed,
      public_income=revenue,recipient_consumption=revenue/s.recipients,
      owners_total_consumption=owner,domestic_consumption=domestic,
      foreign_receipts=p*q,foreign_producer_surplus=s.d*q*q/2,global_surplus=domestic+s.d*q*q/2,resource_residual=value-p*q-variable_cost-fixed-domestic)

def changes(s,t):
    row=allocation(s,t);zero=allocation(s,0.)
    row.update(net_funding=row['public_income']-zero['public_income'],
       domestic_change=row['domestic_consumption']-zero['domestic_consumption'],
       global_change=row['global_surplus']-zero['global_surplus'],
       displaced_domestic_revenue=s.theta*(zero['domestic_profit']-row['domestic_profit']))
    return row

def coefficients(s,public_share):
    return ((s.efficiency-public_share*s.passthrough)*s.q0,
      (s.efficiency-public_share*s.passthrough/2)/s.slope)

def interval(a,b,k,target,cap):
    """Solve a*t-b*t^2-k >= target for 0<t<=cap, given a,b>0.

    This helper is called only in the welfare-compatible branch e>lambda.
    """
    if a<=0 or b<=0: return None
    disc=a*a-4*b*(k+target)
    if disc < -EPS: return None
    disc=max(0.,disc);root=math.sqrt(disc)
    lo=(2*(k+target)/(a+root)) if a+root else 0.
    hi=(a+root)/(2*b)
    lo=max(0.,lo);hi=min(cap,hi)
    return (lo,hi) if hi>0 and lo<=hi+EPS else None

def safe_interval(s,target=0.,cap=None):
    """Return positive-tax interval meeting funding target and no domestic loss.
    None excludes positive taxes; tax zero is dealt with separately.
    """
    if target<0: raise ValueError('Target must be nonnegative')
    # If efficiency <= pass-through, all positive taxes reduce domestic consumption.
    if s.efficiency<=s.passthrough: return None
    cap=min(s.choke, cap if cap is not None else s.choke)
    wr=interval(*coefficients(s,1.),s.fixed_cost,0.,cap)
    rr=interval(*coefficients(s,s.theta),s.fixed_cost,target,cap)
    if wr is None or rr is None: return None
    lo=max(wr[0],rr[0]);hi=min(wr[1],rr[1])
    return (lo,hi) if lo<=hi+EPS else None

def safe_maximum(s,cap=None):
    limits=safe_interval(s,cap=cap)
    if limits is None: return dict(tax=0.,net_funding=0.,domestic_change=0.)
    a,b=coefficients(s,s.theta)
    t=min(limits[1],max(limits[0],a/(2*b)))
    row=changes(s,t)
    if row['net_funding']<0: return dict(tax=0.,net_funding=0.,domestic_change=0.)
    return dict(tax=t,net_funding=row['net_funding'],domestic_change=row['domestic_change'])

def robust_interval(states,target):
    intervals=[safe_interval(s,target) for s in states]
    if any(x is None for x in intervals): return None
    lo=max(x[0] for x in intervals);hi=min(x[1] for x in intervals)
    return (lo,hi) if lo<=hi+EPS else None

def robust_maximum(states,iterations=80):
    if robust_interval(states,0.) is None: return dict(tax=0.,net_funding=0.)
    lo=0.;hi=min(safe_maximum(s)['net_funding'] for s in states)
    for _ in range(iterations):
        mid=(lo+hi)/2
        if robust_interval(states,mid) is not None: lo=mid
        else: hi=mid
    limits=robust_interval(states,lo)
    t=sum(limits)/2
    return dict(tax=t,net_funding=min(changes(s,t)['net_funding'] for s in states))

def write_csv(path,rows):
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

def main():
    design=json.loads((ROOT/'data/design.json').read_text());base=State(**design['base'])
    out=ROOT/'results';out.mkdir(exist_ok=True)
    named=[]
    for spec in design['named']:
        spec=dict(spec);t=spec.pop('tax');s=replace(base,**spec)
        named.append(dict(name=s.name,**changes(s,t),pass_through=s.passthrough,**{'safe_max_funding':safe_maximum(s)['net_funding']}))
    write_csv(out/'scenarios.csv',named)
    grid=design['grid'];keys=list(grid);rows=[];boundaries=[]
    state_keys=[k for k in keys if k!='tax']
    for idx,values in enumerate(itertools.product(*(grid[k] for k in state_keys))):
        pars=dict(zip(state_keys,values));s=replace(base,name='state_'+str(idx),**pars)
        bounds=safe_maximum(s);boundaries.append(dict(state=s.name,**pars,pass_through=s.passthrough,**bounds))
        for t in grid['tax']:
            row=changes(s,t)
            rows.append(dict(state=s.name,**pars,**row))
    write_csv(out/'grid.csv',rows);write_csv(out/'state_boundaries.csv',boundaries)
    robust=[];intervals=[]
    for name,specs in design['robust_sets'].items():
        states=[replace(base,**spec) for spec in specs]
        result=robust_maximum(states,design['robust_search_iterations'])
        robust.append(dict(set=name,states=len(states),**result))
        for target in design['funding_targets']:
            bounds=robust_interval(states,target)
            intervals.append(dict(set=name,target=target,positive_tax_feasible=bounds is not None,
                zero_tax_feasible=target==0.,lower=bounds[0] if bounds else '',upper=bounds[1] if bounds else ''))
    write_csv(out/'robust.csv',robust);write_csv(out/'feasible_intervals.csv',intervals)
    caps=[dict(tax_cap=cap,**safe_maximum(base,cap)) for cap in design['withdrawal_tax_caps']]
    write_csv(out/'withdrawal_caps.csv',caps)
    positive=[r for r in rows if r['tax']>0]
    summary={'states':len(boundaries),'policy_state_rows':len(rows),'positive_tax_rows':len(positive),
      'gross_positive_net_negative':sum(r['gross_levy_payments']>EPS and r['net_funding']<-EPS for r in positive),
      'net_positive_domestic_negative':sum(r['net_funding']>EPS and r['domestic_change']<-EPS for r in positive),
      'net_positive_domestic_nonnegative':sum(r['net_funding']>EPS and r['domestic_change']>=-EPS for r in positive),
      'states_with_positive_safe_funding':sum(r['net_funding']>EPS for r in boundaries),
      'base_safe_maximum':safe_maximum(base),
      'max_accounting_residual':max(abs(r['resource_residual']) for r in rows)}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    paths=[ROOT/'data/design.json',ROOT/'code/model.py',ROOT/'code/test_model.py']
    outputs=sorted(out.glob('*.csv'))+[out/'summary.json']
    metadata={'run_utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
      'python':platform.python_version(),'platform':platform.system(),'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
      'outputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in outputs},'exit_status':0,'network_used':False}
    (out/'run.json').write_text(json.dumps(metadata,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
