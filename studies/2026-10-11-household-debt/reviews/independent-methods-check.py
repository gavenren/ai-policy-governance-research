"""Independent central checks; no import of the study analysis functions."""
from pathlib import Path
import argparse, hashlib, json, math
from datetime import datetime, timezone
import numpy as np
import pandas as pd
BASE=Path(__file__).resolve().parents[1]

def values(d):
    residual=np.maximum(d['INCOME'].to_numpy()-d['WAGEINC'].to_numpy(),0)/12
    payment=d['TPAY'].to_numpy()
    # With U=2000 and F=1000, every gross case passes by construction.
    gap=(payment>residual+1000+1e-8).astype(float)
    shortfall=np.maximum(payment-residual-1000,0)
    extra=12*(np.maximum(1000+payment-residual,0)-np.maximum(1000-residual,0))
    return gap,shortfall,extra

def main():
    a=argparse.ArgumentParser();a.add_argument('--weights',type=Path,required=True);a.add_argument('--source-csv',type=Path);args=a.parse_args()
    selected=BASE/'data/scf2025-selected.csv';d=pd.read_csv(args.source_csv or selected)
    selected_d=pd.read_csv(selected)
    check_columns=list(selected_d.columns)
    source_error=float(np.max(np.abs(d[check_columns].to_numpy()-selected_d.to_numpy())))
    assert np.allclose(d[check_columns],selected_d,rtol=1e-14,atol=1e-9)
    imp=[];pop=[];clipped=[]
    for i in range(1,6):
        part=d[d.Y1%10==i].sort_values('YY1');w=part.WGT.to_numpy()*5
        x=values(part);imp.append([float(np.dot(x[0],w)/w.sum()),float(np.dot(x[1],w)/w.sum()),float(np.dot(x[2],w))]);pop.append(float(w.sum()))
        negative=(part.INCOME<part.WAGEINC).to_numpy()
        clipped.append({'implicate':i,'unweighted_families':int(negative.sum()),'weighted_share':float(np.dot(negative,w)/w.sum())})
    first=d[d.Y1%10==1].sort_values('YY1');r=pd.read_stata(args.weights);r.columns=r.columns.str.upper();r=r.set_index('YY1').loc[first.YY1]
    assert np.array_equal(r.Y1.to_numpy(),first.Y1.to_numpy())
    v=values(first);rep=[];missing=0
    for j in range(1,1000):
        wt=r['WT1B'+str(j)];mult=r['MM'+str(j)]
        assert wt.isna().equals(mult.isna())
        missing+=int(wt.isna().sum())
        w=np.nan_to_num(wt.to_numpy())*np.nan_to_num(mult.to_numpy())
        rep.append([float(np.dot(v[0],w)/w.sum()),float(np.dot(v[1],w)/w.sum()),float(np.dot(v[2],w))])
    imp=np.array(imp);rep=np.array(rep);point=imp.mean(axis=0)
    # Explicit sum-of-squares calculation follows the official MEANIT formula.
    sampling=np.sum((rep-rep.mean(axis=0))**2,axis=0)/998
    imputation=np.sum((imp-imp.mean(axis=0))**2,axis=0)/4
    se=np.sqrt(sampling+6/5*imputation)
    keys=['grid/wage_only/F1000/D1/U2000/classification_gap','grid/wage_only/F1000/D1/U2000/shortfall','topup/wage_only/F1000/D1/extra_annual']
    saved=pd.read_csv(BASE/'results/all-estimates.csv').set_index('key');checks=[]
    for k,mean,error,samp,mi in zip(keys,point,se,sampling,imputation):
        assert math.isclose(mean,saved.loc[k,'estimate'],rel_tol=1e-10,abs_tol=1e-9)
        assert math.isclose(error,saved.loc[k,'standard_error'],rel_tol=1e-10,abs_tol=1e-9)
        checks.append({'key':k,'estimate':mean,'standard_error':error,'sampling_variance':samp,'imputation_variance':mi,'matches_saved':True})
    result={'executed_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'method':'Separate direct central formulas, five implicate estimates, 999 original replicate-weight calculations, explicit sample sums of squares. No import of author analysis.','source_used':args.source_csv.name if args.source_csv else selected.name,'source_sha256':hashlib.sha256((args.source_csv or selected).read_bytes()).hexdigest(),'selected_sha256':hashlib.sha256(selected.read_bytes()).hexdigest(),'weights_sha256':hashlib.sha256(args.weights.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_to_selected_max_numeric_roundtrip_error':source_error,'families':int(d.YY1.nunique()),'records':len(d),'implicate_population':pop,'matching_missing_weight_and_multiplicity_cells':missing,'wage_only_clipping_by_implicate':clipped,'central_gross_pass_is_one_by_construction':True,'checks':checks}
    (BASE/'reviews/independent-methods-check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
