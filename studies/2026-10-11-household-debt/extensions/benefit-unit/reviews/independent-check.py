"""Independent S011 benefit-unit review calculation; does not import author code.

Run from the repository root with pinned public SCF full data and weights.
The program compares every saved implicate/replicate statistic and its combined
estimate/SE. All writes stay in the extension review folder.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, sys, math
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
STUDY=ROOT.parents[1]
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def evaluate(fin,size,adults,weight):
    result={}; worst=0.
    cash=np.clip(fin[:,0]-fin[:,1],0,None)/12
    debt=fin[:,2]
    for sample,keep in [('exact',size!=12),('capped',np.ones(len(size),dtype=bool))]:
        w=weight[keep];s=size[keep];a=adults[keep];N=cash[keep];D=debt[keep]
        mass=w.sum();target=mass*2000
        masks={'all':np.ones(len(s),bool),'size_1':s==1,'size_2':s==2,'size_3plus':s>=3,'with_children':a<s,'without_children':a==s}
        for arm,basis in [('family',np.ones(len(s))),('adult',a.astype(float)),('size',s.astype(float)**.5)]:
            rate=2000. if arm=="family" else 2000.*math.fsum(w)/math.fsum(w*basis)
            U=basis*rate
            error=abs(sum(w*U)/target-1)
            worst=max(worst,error)
            result[f'{sample}/allocation/{arm}/rate']=rate
            result[f'{sample}/allocation/{arm}/annual_total']=sum(w*U)*12
            for label,threshold in [('sqrt',1000*s**.5),('fixed',np.repeat(1000.,len(s)))]:
                G=(N+U>=threshold).astype(float)
                A=(N+U-D>=threshold).astype(float)
                assert (A<=G).all()
                shortfall=np.clip(threshold-(N+U-D),0,None)
                for group,mask in masks.items():
                    if group!='all' and (sample!='exact' or label!='sqrt'):continue
                    numerator_weights=w[mask]
                    den=sum(numerator_weights)
                    values={'gross_pass':G,'after_pass':A,'classification_gap':G-A,'shortfall':shortfall}
                    for metric,values in values.items():
                        result[f'{sample}/{label}/{arm}/{group}/{metric}']=sum(numerator_weights*values[mask])/den
                    if group=='all':
                        result[f'{sample}/{label}/{arm}/all/person_failure']=sum(w*s*(1-A))/sum(w*s)
        for label in ['sqrt','fixed']:
            for left,right in [('adult','family'),('size','family'),('size','adult')]:
                for metric in ['gross_pass','after_pass','classification_gap','shortfall','person_failure']:
                    result[f'{sample}/{label}/{left}_minus_{right}/{metric}']=result[f'{sample}/{label}/{left}/all/{metric}']-result[f'{sample}/{label}/{right}/all/{metric}']
    return result,worst

def main():
    p=argparse.ArgumentParser();p.add_argument('--full',type=Path,required=True);p.add_argument('--weights',type=Path,required=True);a=p.parse_args()
    checkpoint=json.loads((ROOT/'reviews/reviewed-hashes.json').read_text())
    assert sha(STUDY/'paper.md')==checkpoint['paper_sha256']
    for path,h in checkpoint['files'].items(): assert sha(ROOT/path)==h,path
    # Fields transcribed independently from the retained official codebook.
    age=['x8022','x104','x110','x116','x122','x128','x134','x204','x210','x216','x222','x228']
    dep=['x8098','x107','x113','x119','x125','x131','x137','x207','x213','x219','x225','x231']
    roster=pd.read_csv(ROOT/'data/roster.csv')
    full=pd.read_stata(a.full,columns=[c.lower() for c in roster.columns],convert_categoricals=False)
    full.columns=full.columns.str.upper()
    ordered=roster.sort_values('Y1'); raw=full.sort_values('Y1')[ordered.columns]
    np.testing.assert_allclose(ordered.to_numpy(),raw.to_numpy(),rtol=1e-14,atol=1e-9)
    included=full[[c.upper() for c in dep]].to_numpy()==1
    ages=full[[c.upper() for c in age]].to_numpy()
    size=included.sum(axis=1);adults=(included&(ages>=18)).sum(axis=1)
    assert np.array_equal(size,full.X7001)
    assert included[:,0].all() and np.array_equal(included[:,1],full.X7020==2)
    assert (adults>0).all() and not ((ages==0)&included).any()
    full['size']=size;full['adults']=adults
    summary=pd.read_csv(STUDY/'data/scf2025-selected.csv')
    data=summary.merge(full[['YY1','Y1','size','adults']],on=['YY1','Y1'],how='outer',validate='one_to_one',indicator=True)
    assert data._merge.eq('both').all() and data.Y1.is_unique
    assert data.groupby('YY1').size().eq(5).all()
    saved_i=pd.read_csv(ROOT/'results/implicate-estimates.csv',index_col=0)
    saved_r=pd.read_csv(ROOT/'results/replicate-estimates.csv',index_col=0)
    keys=list(saved_i.columns);assert keys==list(saved_r.columns)
    results_i=[];results_r=[];errors=[];exclusions=[]
    for imp in range(1,6):
        sub=data[data.Y1%10==imp].sort_values('YY1')
        fin=sub[['INCOME','WAGEINC','TPAY']].to_numpy();s=sub['size'].to_numpy();ad=sub.adults.to_numpy();w=sub.WGT.to_numpy()*5
        values,e=evaluate(fin,s,ad,w);errors.append(e);results_i.append([values[k] for k in keys])
        exclusions.append({'implicate':imp,'count':int((s==12).sum()),'weighted_share':sum(w[s==12])/sum(w),'covered_families':int((s<12).sum()),'covered_members':sum(w[s<12]*s[s<12])})
        if imp==1:first=sub
    rw=pd.read_stata(a.weights,convert_categoricals=False);rw.columns=rw.columns.str.upper()
    rw=rw.set_index('YY1').loc[first.YY1]
    assert np.array_equal(rw.Y1.to_numpy(),first.Y1.to_numpy())
    fin=first[['INCOME','WAGEINC','TPAY']].to_numpy();s=first['size'].to_numpy();ad=first.adults.to_numpy()
    for rep in range(1,1000):
        w=rw[f'MM{rep}'].fillna(0).to_numpy()*rw[f'WT1B{rep}'].fillna(0).to_numpy()
        assert (w>=0).all() and np.isfinite(w).all()
        values,e=evaluate(fin,s,ad,w);errors.append(e);results_r.append([values[k] for k in keys])
    I=np.array(results_i);R=np.array(results_r)
    np.testing.assert_allclose(I,saved_i.to_numpy(),rtol=2e-11,atol=1e-10)
    np.testing.assert_allclose(R,saved_r.to_numpy(),rtol=2e-11,atol=1e-10)
    mean=I.sum(axis=0)/5
    variance=sum((R-R.mean(axis=0))**2)/998+1.2*sum((I-I.mean(axis=0))**2)/4
    se=variance**.5
    reported=pd.concat([pd.read_csv(ROOT/'results'/f'{t}.csv') for t in ['allocation','outcomes','contrasts']]).set_index('key').loc[keys]
    np.testing.assert_allclose(mean,reported.estimate,rtol=2e-11,atol=1e-9)
    np.testing.assert_allclose(se,reported.standard_error,rtol=2e-11,atol=1e-8)
    # Algebraic and negative checks separate from the survey calculation.
    w=np.array([1.,2.,1.]);v=np.array([1.,2.,3.]);c=2000*sum(w)/sum(w*v)
    assert c==1000 and sum(w*c*v)==8000
    # If each replicate held a full-sample rate, unequal composition would break matching.
    c_fixed=4000/3;changed_w=np.array([2.,1.]);unit=np.array([1.,2.])
    assert abs(sum(changed_w*c_fixed*unit)-2000*sum(changed_w))>600
    # Paired variance has covariance and can be zero even when both arm variances are positive.
    x=np.array([1.,2.,4.]);y=x+2
    assert np.var(y-x,ddof=1)==0 and np.var(x,ddof=1)+np.var(y,ddof=1)>0
    # The public 13-17 and 18-25 bins preserve an age-18 split but not an age-14 split.
    assert all((x>=18)==(17>=18) for x in range(13,18))
    assert all((x>=18)==(25>=18) for x in range(18,26))
    assert (13>=14)!=(17>=14)
    output={'checked_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
            'reviewer':'Separate AI agent; no author analysis imports','python':sys.version.split()[0],'numpy':np.__version__,'pandas':pd.__version__,
            'paper_sha256':checkpoint['paper_sha256'],'author_checkpoint_sha256':sha(ROOT/'logs/author-checkpoint.json'),
            'code_sha256':sha(__file__),'full_data_sha256':sha(a.full),'weights_sha256':sha(a.weights),
            'source_rows':len(full),'full_to_public_roster_match':True,'complete_joins':True,
            'implicates':len(I),'replicates':len(R),'estimands_per_run':len(keys),'statistic_comparisons':int(I.size+R.size),
            'max_absolute_difference_scaled_by_max_1':float(max(np.max(abs(I-saved_i.to_numpy())/np.maximum(1,abs(saved_i.to_numpy()))),np.max(abs(R-saved_r.to_numpy())/np.maximum(1,abs(saved_r.to_numpy()))))),
            'all_combined_estimates_and_paired_standard_errors_match':True,'budget_checks':len(errors)*2*3,'max_relative_budget_error':max(errors),
            'exclusions':exclusions,'negative_checks':['fixed-rate replicate changes budget','separate-arm variance loses covariance','age-14 boundary not recoverable'],
            'source_and_author_files_changed':False}
    (ROOT/'reviews/independent-check.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
