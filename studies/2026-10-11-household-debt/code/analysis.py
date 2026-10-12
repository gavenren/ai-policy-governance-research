"""Fixed-contract SCF stress test. No forecast, behavioral, or tax model."""
from pathlib import Path
import argparse, hashlib, json, platform
from datetime import datetime, timezone
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
FIELDS=['YY1','Y1','WGT','INCOME','WAGEINC','BUSSEFARMINC','KGINC','PENACCTWD','TPAY','RENT','LIQ','DEBT','AGE','MARRIED','KIDS','HHOUSES','NETWORTH','NORMINC']
SHOCKS=['no_loss','wage_only','wider_flow']
METRICS=['gross_pass','after_pass','classification_gap','shortfall','gap_shortfall','negative_after','bridge_3','bridge_12']

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def resources(d,shock):
    raw=d.INCOME.to_numpy(float).copy()
    if shock!='no_loss': raw-=d.WAGEINC.to_numpy(float)
    if shock=='wider_flow':
        for c in ['BUSSEFARMINC','KGINC','PENACCTWD']: raw-=np.maximum(d[c].to_numpy(float),0)
    return np.maximum(raw,0)/12,raw<0

def outcomes(n,debt,liquid,transfer,floor):
    gross=n+transfer; after=gross-debt
    short=np.maximum(floor-after,0)
    g=gross>=floor-1e-8; a=after>=floor-1e-8
    return np.column_stack([g,a,g&~a,short,short*g,after< -1e-8,(short>1e-8)&(liquid>=3*short),(short>1e-8)&(liquid>=12*short)]).astype(float)

def topups(n,debt,floor):
    t0=np.maximum(floor-n,0);t1=np.maximum(floor+debt-n,0)
    return t0,t1,t1-t0

def weighted_quantile(v,w,q):
    order=np.argsort(v,kind='stable');v=np.asarray(v)[order];w=np.asarray(w)[order]
    return float(v[np.searchsorted(np.cumsum(w),q*w.sum(),side='left')])

def combine(imp,rep):
    return float(np.mean(imp)),float(np.sqrt(np.var(rep,ddof=1)+1.2*np.var(imp,ddof=1)))

def validate_data(d):
    if list(d.columns)!=FIELDS: raise ValueError('Unexpected selected-data schema')
    if not d.Y1.is_unique: raise ValueError('Duplicate observation ID')
    if not np.isfinite(d.to_numpy(float)).all(): raise ValueError('Non-finite input')
    if not (d.Y1//10==d.YY1).all(): raise ValueError('Family identifier mismatch')
    if not d.groupby('YY1').Y1.count().eq(5).all(): raise ValueError('Missing implicate')
    if set(d.Y1%10)!={1,2,3,4,5}: raise ValueError('Unexpected implicate')
    if not (d[['WGT','TPAY','RENT','LIQ','DEBT','INCOME']]>=0).all().all(): raise ValueError('Negative nonnegative field')
    if not (d.WGT>0).all(): raise ValueError('Zero main weight')


def build_statistics(d):
    """Return one vector per estimand plus a subgroup mask and total/mean flag."""
    nrows=len(d);ones=np.ones(nrows,dtype=bool); stats={};metadata={}
    def add(key,v,meta,mask=ones,total=False,uncertainty=False):
        stats[key]=(np.asarray(v,float),mask,total)
        metadata[key]={**meta,'uncertainty':uncertainty}
    debt=d.TPAY.to_numpy(float);liq=d.LIQ.to_numpy(float)
    for shock in SHOCKS:
        n,clipped=resources(d,shock)
        add(f'diagnostic/{shock}/clipped',clipped,dict(table='diagnostic',shock=shock,metric='clipped'),uncertainty=True)
        for floor in [500,1000,1500]:
            for factor in [0,0.5,1]:
                outflow=factor*debt
                for transfer in [0,1000,2000,3000,4000]:
                    v=outcomes(n,outflow,liq,transfer,floor)
                    central=floor==1000 and factor==1
                    prefix=f'grid/{shock}/F{floor}/D{factor}/U{transfer}'
                    for j,m in enumerate(METRICS):add(prefix+'/'+m,v[:,j],dict(table='grid',shock=shock,floor=floor,debt_factor=factor,transfer=transfer,metric=m),uncertainty=central)
                t0,t1,extra=topups(n,outflow,floor)
                for m,v,total in [('gross_annual',12*t0,True),('debt_adjusted_annual',12*t1,True),('extra_annual',12*extra,True),('gross_recipients',t0>1e-8,False),('debt_adjusted_recipients',t1>1e-8,False)]:
                    key=f'topup/{shock}/F{floor}/D{factor}/{m}'
                    add(key,v,dict(table='topup',shock=shock,floor=floor,debt_factor=factor,metric=m),total=total,uncertainty=floor==1000 and factor==1)
    n,_=resources(d,'wage_only')
    for transfer in [0,1000,2000,3000,4000]:
        v=outcomes(n,debt+d.RENT.to_numpy(float),liq,transfer,1000)
        for j,m in enumerate(METRICS):add(f'rent/U{transfer}/{m}',v[:,j],dict(table='rent',transfer=transfer,floor=1000,metric=m),uncertainty=transfer==2000)
    groups={'all':ones,'wage_positive':d.WAGEINC.to_numpy()>0,'wage_zero':d.WAGEINC.to_numpy()<=0,'payment_positive':debt>0,'payment_zero':debt==0,'age_under65':d.AGE.to_numpy()<65,'age_65plus':d.AGE.to_numpy()>=65,'owner':d.HHOUSES.to_numpy()==1,'nonowner':d.HHOUSES.to_numpy()==0}
    v=outcomes(n,debt,liq,2000,1000)
    for group,mask in groups.items():
        for j,m in enumerate(METRICS):add(f'group/{group}/{m}',v[:,j],dict(table='groups',group=group,metric=m),mask=mask,uncertainty=True)
    cap=weighted_quantile(debt,d.WGT,0.99)
    capped=outcomes(n,np.minimum(debt,cap),liq,2000,1000)
    for j,m in enumerate(METRICS):add(f'influence/capped/{m}',capped[:,j],dict(table='influence',metric=m,first_implicate_cap=cap,cap_rule='weighted 99th percentile separately within each implicate'),uncertainty=False)
    for c in ['INCOME','NETWORTH','TPAY','LIQ','DEBT']:
        add('descriptive/'+c,d[c],dict(table='descriptive',metric='mean_'+c),uncertainty=True)
    add('descriptive/population',np.ones(nrows),dict(table='descriptive',metric='families'),total=True,uncertainty=True)
    add('descriptive/has_debt',d.DEBT>0,dict(table='descriptive',metric='has_debt'),uncertainty=True)
    return stats,metadata

def estimate(v,w,mask,total):
    numer=np.asarray(v)[mask]@np.asarray(w)[mask]
    return numer if total else numer/np.asarray(w)[mask].sum(axis=0)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-csv',type=Path);ap.add_argument('--weights',type=Path);ap.add_argument('--saved-replicates',type=Path);ap.add_argument('--output',type=Path,default=ROOT/'results');a=ap.parse_args()
    datafile=ROOT/'data/scf2025-selected.csv'
    if a.source_csv:
        source=pd.read_csv(a.source_csv,usecols=FIELDS)[FIELDS];source.to_csv(datafile,index=False,float_format='%.17g')
    d=pd.read_csv(datafile);validate_data(d);a.output.mkdir(parents=True,exist_ok=True)
    imp_results={};metadata=None;first_stats=None;counts=[];caps=[]
    for imp in range(1,6):
        sub=d[d.Y1%10==imp].sort_values('YY1').reset_index(drop=True)
        stats,meta=build_statistics(sub);w=sub.WGT.to_numpy()*5
        imp_results[imp]={k:float(estimate(v,w,mask,total)) for k,(v,mask,total) in stats.items()}
        caps.append(weighted_quantile(sub.TPAY.to_numpy(),w,.99))
        for k,(v,mask,total) in stats.items():
            if meta[k]['table']=='groups' and meta[k]['metric']=='gross_pass':counts.append(dict(implicate=imp,group=meta[k]['group'],public_families=int(mask.sum()),weighted_families=float(w[mask].sum())))
        if imp==1:first=sub;first_stats=stats;metadata=meta
    se_keys=[k for k in metadata if metadata[k]['uncertainty']]
    weight_info={}
    if a.weights:
        rw=pd.read_stata(a.weights);rw.columns=rw.columns.str.upper()
        if not rw.YY1.is_unique:raise ValueError('Duplicate family in weights')
        merged=first[['YY1','Y1']].merge(rw,on='YY1',how='left',validate='one_to_one',suffixes=('_DATA','_WEIGHT'))
        if merged.Y1_WEIGHT.isna().any() or not (merged.Y1_DATA==merged.Y1_WEIGHT).all():raise ValueError('Incomplete weight join')
        # The official codebook maps missing multiplicity/weight to zero for unselected families.
        weights=np.column_stack([merged[f'WT1B{i}'].fillna(0).to_numpy()*merged[f'MM{i}'].fillna(0).to_numpy() for i in range(1,1000)])
        if not np.isfinite(weights).all() or (weights<0).any() or (weights.sum(axis=0)<=0).any():raise ValueError('Invalid replicate weights')
        reps=pd.DataFrame({k:estimate(first_stats[k][0],weights,first_stats[k][1],first_stats[k][2]) for k in se_keys})
        reps.index=np.arange(1,1000);reps.index.name='replicate';reps.to_csv(a.output/'replicate-estimates.csv',float_format='%.17g')
        weight_info=dict(path_name=a.weights.name,sha256=sha(a.weights),replicates=999,rows=len(rw),replicate_population_min=float(weights.sum(axis=0).min()),replicate_population_max=float(weights.sum(axis=0).max()))
    elif a.saved_replicates:
        reps=pd.read_csv(a.saved_replicates,index_col='replicate')
        if list(reps.columns)!=se_keys or list(reps.index)!=list(range(1,1000)):raise ValueError('Saved replicate schema mismatch')
        weight_info=dict(reconstructed_from_saved_estimates=True,sha256=sha(a.saved_replicates),limitation='Does not independently rerun replicate-weight application')
    else:raise ValueError('Provide --weights or --saved-replicates')
    rows=[]
    for key,meta in metadata.items():
        values=[imp_results[i][key] for i in range(1,6)];point=float(np.mean(values));se=None
        if key in reps:point,se=combine(values,reps[key].to_numpy())
        rows.append(dict(key=key,**meta,estimate=point,standard_error=se,imputation_sd=float(np.std(values,ddof=1))))
    result=pd.DataFrame(rows)
    result.to_csv(a.output/'all-estimates.csv',index=False,float_format='%.12g')
    for table,part in result.groupby('table',sort=False):part.dropna(axis=1,how='all').to_csv(a.output/(table+'.csv'),index=False,float_format='%.12g')
    pd.DataFrame(imp_results).rename_axis('key').to_csv(a.output/'implicate-estimates.csv',float_format='%.17g')
    pd.DataFrame(counts).to_csv(a.output/'group-counts.csv',index=False,float_format='%.12g')
    invariants={}
    for shock in SHOCKS:
        for f in [500,1000,1500]:
            for fac in [0,0.5,1]:
                pick=result[(result.table=='grid')&(result.shock==shock)&(result.floor==f)&(result.debt_factor==fac)]
                for metric in ['gross_pass','after_pass']:
                    vals=pick[pick.metric==metric].sort_values('transfer').estimate.to_numpy();assert (np.diff(vals)>=-1e-10).all()
                wide=pick.pivot(index='transfer',columns='metric',values='estimate');assert np.allclose(wide.gross_pass-wide.after_pass,wide.classification_gap)
    invariants.update(monotone_in_transfer=True,gap_decomposition=True,unique_Y1=True,five_implicates=True,complete_weight_join=True if a.weights else "not rerun; saved estimates used")
    diagnostics=dict(recorded_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),python=platform.python_version(),numpy=np.__version__,pandas=pd.__version__,rows=len(d),families=d.YY1.nunique(),selected_data_sha256=sha(datafile),analysis_sha256=sha(__file__),weights=weight_info,estimands=len(rows),uncertainty_estimands=len(se_keys),cap99_by_implicate=caps,missing_values=int(d.isna().sum().sum()),invariants=invariants)
    (a.output/'run.json').write_text(json.dumps(diagnostics,indent=2)+'\n')
    print(json.dumps(diagnostics,indent=2))
if __name__=='__main__':main()
