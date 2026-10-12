"""S011 prospective benefit-unit extension. Original analysis files are read-only."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, platform
import numpy as np
import pandas as pd
from check_feasibility import REL, AGE, DEP, FIELDS

ROOT=Path(__file__).resolve().parents[1]
STUDY=ROOT.parents[1]
ARMS={'family':'family_count','adult':'adult_count','size':'sqrt_size'}
METRICS=['gross_pass','after_pass','classification_gap','shortfall','person_failure']
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def derive_members(d):
    r=d[REL].to_numpy(); a=d[AGE].to_numpy(); dep=d[DEP].to_numpy()
    if not np.isfinite(d.to_numpy(float)).all(): raise ValueError('Missing roster field')
    if set(np.unique(dep))-{0,1,5}: raise ValueError('Unknown dependence code')
    inc=dep==1
    if ((r==0)&inc).any() or ((a==0)&inc).any(): raise ValueError('Incomplete included person')
    if not inc[:,0].all(): raise ValueError('Missing reference person')
    if not np.array_equal(inc[:,1],d.X7020.to_numpy()==2): raise ValueError('Spouse membership mismatch')
    n=inc.sum(axis=1);adult=((a>=18)&inc).sum(axis=1)
    if not np.array_equal(n,d.X7001): raise ValueError('Roster and PEU size mismatch')
    if (adult==0).any(): raise ValueError('Zero-adult family requires investigation')
    if (n<1).any() or (n>12).any(): raise ValueError('Size outside public support')
    return n,adult

def calibrated_transfer(v,w,budget_per_family=2000.):
    den=np.dot(w,v)
    if den<=0 or np.sum(w)<=0: raise ValueError('Empty payment base')
    c=budget_per_family*np.sum(w)/den
    u=c*v
    target=budget_per_family*np.sum(w)
    error=abs(np.dot(w,u)-target)/target
    if error>1e-12: raise AssertionError('Unequal payment budget')
    return u,float(c),float(error)

def outcome_vectors(n,debt,transfer,floor):
    gross=n+transfer; after=gross-debt
    g=gross>=floor-1e-8;a=after>=floor-1e-8
    if (a&~g).any(): raise AssertionError('After pass not subset of gross pass')
    return {'gross_pass':g.astype(float),'after_pass':a.astype(float),
            'classification_gap':(g&~a).astype(float),
            'shortfall':np.maximum(floor-after,0),'person_failure':(~a).astype(float)}

def statistics(d,w):
    n=np.maximum(d.INCOME.to_numpy()-d.WAGEINC.to_numpy(),0)/12
    debt=d.TPAY.to_numpy();size=d.PEU_SIZE.to_numpy();adult=d.ADULTS.to_numpy()
    out={};meta={};max_error=0.
    for sample in ['exact','capped']:
        keep=size<12 if sample=='exact' else np.ones(len(d),bool)
        ws=w[keep];s=size[keep];ad=adult[keep];nn=n[keep];dd=debt[keep]
        if ws.sum()<=0: raise ValueError('Empty retained sample')
        masks={'all':np.ones(len(s),bool),'size_1':s==1,'size_2':s==2,'size_3plus':s>=3,
               'with_children':s>ad,'without_children':s==ad}
        def add(key,val,**m):
            out[key]=float(val);meta[key]={'sample':sample,**m}
        for arm in ARMS:
            v={'family':np.ones(len(s)),'adult':ad,'size':np.sqrt(s)}[arm]
            u,c,error=calibrated_transfer(v,ws);max_error=max(max_error,error)
            add(f'{sample}/allocation/{arm}/rate',c,table='allocation',arm=arm,metric='rate')
            add(f'{sample}/allocation/{arm}/annual_total',12*np.dot(ws,u),table='allocation',arm=arm,metric='annual_total')
            for floor_kind in ['sqrt','fixed']:
                floor=1000*np.sqrt(s) if floor_kind=='sqrt' else np.full(len(s),1000.)
                vectors=outcome_vectors(nn,dd,u,floor)
                groups=masks if sample=='exact' and floor_kind=='sqrt' else {'all':masks['all']}
                for group,mask in groups.items():
                    if ws[mask].sum()<=0: raise ValueError('Empty subgroup replicate')
                    for metric,vect in vectors.items():
                        if group!='all' and metric=='person_failure': continue
                        unit_w=ws*s if metric=='person_failure' else ws
                        value=np.dot(vect[mask],unit_w[mask])/unit_w[mask].sum()
                        add(f'{sample}/{floor_kind}/{arm}/{group}/{metric}',value,
                            table='outcomes',floor=floor_kind,arm=arm,group=group,metric=metric)
        for floor_kind in ['sqrt','fixed']:
            for left,right in [('adult','family'),('size','family'),('size','adult')]:
                for metric in METRICS:
                    value=out[f'{sample}/{floor_kind}/{left}/all/{metric}']-out[f'{sample}/{floor_kind}/{right}/all/{metric}']
                    add(f'{sample}/{floor_kind}/{left}_minus_{right}/{metric}',value,
                        table='contrasts',floor=floor_kind,left=left,right=right,metric=metric)
    return out,meta,max_error

def combine(imp,rep):
    return np.mean(imp,axis=0),np.sqrt(np.var(rep,axis=0,ddof=1)+1.2*np.var(imp,axis=0,ddof=1))

def prepare(selected,roster):
    s=pd.read_csv(selected);r=pd.read_csv(roster)
    n,a=derive_members(r)
    r=r[['YY1','Y1','X101']].copy();r['PEU_SIZE']=n;r['ADULTS']=a
    d=s.merge(r,on=['YY1','Y1'],how='outer',validate='one_to_one',indicator=True)
    if not d._merge.eq('both').all(): raise ValueError('Incomplete roster join')
    if not d.Y1.is_unique or not d.groupby('YY1').Y1.count().eq(5).all(): raise ValueError('Invalid implicates')
    if set(d.Y1%10)!={1,2,3,4,5}: raise ValueError('Invalid implicate labels')
    return d.drop(columns='_merge')

def main():
    p=argparse.ArgumentParser();p.add_argument('--full',type=Path);p.add_argument('--weights',type=Path,required=True)
    p.add_argument('--output',type=Path,default=ROOT/'results');a=p.parse_args()
    roster=ROOT/'data/roster.csv';selected=STUDY/'data/scf2025-selected.csv'
    if a.full:
        if roster.exists(): raise ValueError('Roster exists; omit --full to reuse it')
        r=pd.read_stata(a.full,columns=[x.lower() for x in FIELDS],convert_categoricals=False)
        r.columns=r.columns.str.upper();r=r[FIELDS]
        derive_members(r);roster.parent.mkdir(parents=True,exist_ok=True)
        r.to_csv(roster,index=False,float_format='%.17g')
    d=prepare(selected,roster);a.output.mkdir(parents=True,exist_ok=True)
    imps=[];counts=[];maxerror=0.
    for imp in range(1,6):
        sub=d[d.Y1%10==imp].sort_values('YY1').reset_index(drop=True);w=sub.WGT.to_numpy()*5
        values,meta,err=statistics(sub,w);maxerror=max(maxerror,err);imps.append(values)
        if imp==1:first=sub;keys=list(values);metadata=meta
        for sample in ['exact','capped']:
            keep=sub.PEU_SIZE.to_numpy()<12 if sample=='exact' else np.ones(len(sub),bool)
            s=sub.PEU_SIZE.to_numpy();ad=sub.ADULTS.to_numpy()
            groups={'all':keep,'size_1':keep&(s==1),'size_2':keep&(s==2),'size_3plus':keep&(s>=3),
                    'with_children':keep&(s>ad),'without_children':keep&(s==ad)}
            for group,mask in groups.items():
                counts.append(dict(implicate=imp,sample=sample,group=group,public_families=int(mask.sum()),
                    weighted_families=float(w[mask].sum()),weighted_members=float(np.dot(w[mask],s[mask]))))
    rw=pd.read_stata(a.weights);rw.columns=rw.columns.str.upper()
    joined=first[['YY1','Y1']].merge(rw,on='YY1',how='left',validate='one_to_one',suffixes=('_DATA','_WEIGHT'))
    if joined.Y1_WEIGHT.isna().any() or not joined.Y1_DATA.eq(joined.Y1_WEIGHT).all(): raise ValueError('Incomplete weight join')
    reps=[]
    for b in range(1,1000):
        w=joined[f'WT1B{b}'].fillna(0).to_numpy()*joined[f'MM{b}'].fillna(0).to_numpy()
        if not np.isfinite(w).all() or (w<0).any(): raise ValueError('Invalid replicate weights')
        vals,_,err=statistics(first,w);maxerror=max(maxerror,err);reps.append(vals)
    imp=pd.DataFrame(imps,columns=keys,index=range(1,6));imp.index.name='implicate'
    rep=pd.DataFrame(reps,columns=keys,index=range(1,1000));rep.index.name='replicate'
    point,se=combine(imp.to_numpy(),rep.to_numpy());rows=[]
    for k,q,s in zip(keys,point,se):
        rows.append(dict(key=k,**metadata[k],estimate=q,standard_error=s,lower_95=q-1.96*s,upper_95=q+1.96*s))
    result=pd.DataFrame(rows)
    for table,part in result.groupby('table',sort=False):
        part.dropna(axis=1,how='all').to_csv(a.output/(table+'.csv'),index=False,float_format='%.12g')
    imp.to_csv(a.output/'implicate-estimates.csv',float_format='%.17g');rep.to_csv(a.output/'replicate-estimates.csv',float_format='%.17g')
    pd.DataFrame(counts).to_csv(a.output/'counts.csv',index=False,float_format='%.12g')
    # Compare the unchanged original central case to the all-family fixed bridge.
    orig=pd.read_csv(STUDY/'results/grid.csv')
    central=orig[(orig.shock=='wage_only')&(orig.floor==1000)&(orig.debt_factor==1)&(orig.transfer==2000)]
    bridge={}
    for metric in METRICS[:4]:
        row=result[result.key==f'capped/fixed/family/all/{metric}'].iloc[0]
        old=central[central.metric==metric].iloc[0]
        assert np.isclose(row.estimate,old.estimate,rtol=1e-10,atol=1e-10)
        assert np.isclose(row.standard_error,old.standard_error,rtol=1e-10,atol=1e-10)
        bridge[metric]=dict(estimate=float(row.estimate),standard_error=float(row.standard_error),matched_original=True)
    diag=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),python=platform.python_version(),numpy=np.__version__,pandas=pd.__version__,
        selected_sha256=sha(selected),roster_sha256=sha(roster),weights_sha256=sha(a.weights),analysis_sha256=sha(__file__),
        protocol_sha256=sha(ROOT/'protocol.md'),public_families=int(d.YY1.nunique()),records=len(d),replicates=999,estimands=len(keys),
        max_relative_budget_error=maxerror,bridge=bridge,complete_joins=True,
        exact_count_exclusions_per_implicate=[int(((d.Y1%10==i)&(d.PEU_SIZE==12)).sum()) for i in range(1,6)],
        interpretation='Gross payment budgets matched; no tax, behavior, needs measurement or individual access to money estimated.')
    (a.output/'run.json').write_text(json.dumps(diag,indent=2)+'\n');print(json.dumps(diag,indent=2))
if __name__=='__main__':main()

