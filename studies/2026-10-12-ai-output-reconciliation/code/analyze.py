#!/usr/bin/env python3
"""Independent, standard-library reconstruction from aggregate accounting inputs.

No original module, implementation, or cluster-level data is used by this file.
A signed Fisher index is conditional on the source's AI-island boundary.
"""
import csv, hashlib, json, math
from pathlib import Path

STUDY=Path(__file__).resolve().parents[1]
RAW=STUDY/'data/raw'
OUT=STUDY/'results'
COMPONENTS=('training','services','dc_labor','power','services_labor')
SIGNS=(1,1,-1,-1,-1)

def load_rows():
    with (RAW/'annual-inputs.csv').open() as f:
        return [{k:(v if k=='power_rule' else int(v) if k=='year' else float(v)) for k,v in r.items()} for r in csv.DictReader(f)]
def save_csv(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def save_json(path,obj): path.write_text(json.dumps(obj,sort_keys=True,indent=2,allow_nan=False)+'\n')
def positive(value,name):
    if not math.isfinite(value) or value<=0: raise ValueError(name+' must be finite and positive; real index is undefined')
def bridge_price(algorithm,spending_growth,operations_growth):
    for v in (algorithm,spending_growth,operations_growth):positive(v,'bridge input')
    return algorithm*spending_growth/operations_growth

def fisher_step(previous,current,prices):
    """Signed Laspeyres and Paasche factors, with explicit validity checks."""
    for p in prices:positive(p,'component price ratio')
    old=sum(s*x for s,x in zip(SIGNS,previous));new=sum(s*x for s,x in zip(SIGNS,current))
    lnum=sum(s*x/p for s,x,p in zip(SIGNS,current,prices))
    pden=sum(s*x*p for s,x,p in zip(SIGNS,previous,prices))
    for value,name in [(old,'previous nominal value added'),(new,'current nominal value added'),(lnum,'Laspeyres numerator'),(pden,'Paasche denominator')]:positive(value,name)
    l=lnum/old;p=new/pden
    positive(l,'Laspeyres factor');positive(p,'Paasche factor')
    return {'laspeyres_numerator_usd':lnum,'laspeyres_denominator_usd':old,'paasche_numerator_usd':new,
            'paasche_denominator_usd':pden,'laspeyres_factor':l,'paasche_factor':p,'fisher_factor':math.sqrt(l*p)}

def components(row,i,params):
    v=row['compute_spending_usd'];inf=v*params['INFERENCE_SHARE'][i]
    return [v-inf,params['AI_SERVICES_MARKUP']*inf,row['data_center_labor_usd'],
            row['charged_listed_power_cost_usd'],params['AI_SERVICES_LABOR_SHARE']*inf]

def reconstruct(rows,params,price_rule):
    answer=[];price_rows=[];previous=None;chained_l=chained_p=chained_f=100.0
    a=params['TRAINING_DEFLATOR_RATIO'];b=params['INFERENCE_DEFLATOR_RATIO']
    for i,row in enumerate(rows):
        c=components(row,i,params);nominal=sum(s*v for s,v in zip(SIGNS,c));positive(nominal,'nominal value added')
        prices=[None]*5;factors={k:None for k in ['laspeyres_numerator_usd','laspeyres_denominator_usd','paasche_numerator_usd','paasche_denominator_usd','laspeyres_factor','paasche_factor','fisher_factor']}
        nomgrowth=realgrowth=None
        if i:
            prior=rows[i-1];vg=row['compute_spending_usd']/prior['compute_spending_usd'];xg=row['physical_bit_ops']/prior['physical_bit_ops']
            train=a if price_rule=='released' else bridge_price(a,vg,xg)
            prices=[train,b,1.0,row['electricity_price_usd_per_kWh']/prior['electricity_price_usd_per_kWh'],1.0]
            factors=fisher_step(previous,c,prices)
            chained_l*=factors['laspeyres_factor'];chained_p*=factors['paasche_factor'];chained_f*=factors['fisher_factor']
            nomgrowth=(nominal/answer[-1]['nominal_ai_gdp_usd']-1)*100
            realgrowth=(factors['fisher_factor']-1)*100
            for k,s,p in zip(COMPONENTS,SIGNS,prices):price_rows.append({'power_rule':row['power_rule'],'training_price_rule':price_rule,'year':row['year'],'component':k,'sign':s,'price_ratio':p})
        r={'power_rule':row['power_rule'],'training_price_rule':price_rule,'year':row['year'],
           **{k+'_usd':v for k,v in zip(COMPONENTS,c)},'nominal_ai_gdp_usd':nominal,'nominal_growth_pct':nomgrowth,
           'training_price_ratio':prices[0],**factors,'laspeyres_chain_index':chained_l,'paasche_chain_index':chained_p,
           'fisher_chain_index':chained_f,'real_ai_gdp_2023_usd':(answer[0]['nominal_ai_gdp_usd'] if i else nominal)*chained_f/100,
           'real_growth_pct':realgrowth}
        answer.append(r);previous=c
    return answer,price_rows

def training_ledger(rows,p):
    a=p['TRAINING_DEFLATOR_RATIO'];result=[]
    base_v=(1-p['INFERENCE_SHARE'][0])*rows[0]['compute_spending_usd']
    base_x=(1-p['INFERENCE_SHARE'][0])*rows[0]['physical_bit_ops']
    for i,r in enumerate(rows):
        v=(1-p['INFERENCE_SHARE'][i])*r['compute_spending_usd'];x=(1-p['INFERENCE_SHARE'][i])*r['physical_bit_ops']
        rental_index=100*(v/base_v)/a**i;ops_index=100*(x/base_x)/a**i
        source_price=a**i;ops_price=(v/base_v)/(ops_index/100)
        vg=xg=bridge=rental_growth=ops_growth=wedge=None
        if i:
            vg=r['compute_spending_usd']/rows[i-1]['compute_spending_usd'];xg=r['physical_bit_ops']/rows[i-1]['physical_bit_ops']
            bridge=bridge_price(a,vg,xg);rental_growth=(vg/a-1)*100;ops_growth=(xg/a-1)*100;wedge=xg/vg
        result.append({'power_rule':r['power_rule'],'year':r['year'],'nominal_training_usd':v,'physical_training_bit_ops':x,
           'nominal_spending_growth_ratio':vg,'physical_operations_growth_ratio':xg,'released_training_price_ratio':a if i else None,
           'bridge_training_price_ratio':bridge,'rental_volume_index_2023_100':rental_index,'operations_volume_index_2023_100':ops_index,
           'rental_volume_growth_pct':rental_growth,'operations_volume_growth_pct':ops_growth,'operations_to_rental_growth_ratio':wedge,
           'operations_to_rental_level_ratio':ops_index/rental_index,'rental_price_index_2023_1':source_price,'operations_price_index_2023_1':ops_price,
           'rental_price_times_volume_usd':source_price*base_v*rental_index/100,
           'operations_price_times_volume_usd':ops_price*base_v*ops_index/100})
    return result

def main():
    params=json.loads((RAW/'parameters.json').read_text());rows=load_rows();cases=[];prices=[];training=[];lookup={}
    for power in ['released','annual_preserving']:
        selected=[r for r in rows if r['power_rule']==power]
        training.extend(training_ledger(selected,params))
        for pr in ['released','operations_bridge']:
            result,p=reconstruct(selected,params,pr);cases.extend(result);prices.extend(p);lookup[(power,pr)]={r['year']:r for r in result}
    effects=[]
    for label,left,right in [('training_given_released_power',('released','released'),('released','operations_bridge')),
        ('training_given_annual_preserving_power',('annual_preserving','released'),('annual_preserving','operations_bridge')),
        ('power_given_released_price',('released','released'),('annual_preserving','released')),
        ('power_given_bridge_price',('released','operations_bridge'),('annual_preserving','operations_bridge'))]:
        for y in params['years']:
            l,r=lookup[left][y],lookup[right][y]
            effects.append({'contrast':label,'year':y,'real_level_difference_usd':r['real_ai_gdp_2023_usd']-l['real_ai_gdp_2023_usd'],
                'real_level_difference_pct':(r['real_ai_gdp_2023_usd']/l['real_ai_gdp_2023_usd']-1)*100,
                'real_growth_difference_pp':None if y==2023 else r['real_growth_pct']-l['real_growth_pct'],
                'nominal_level_difference_usd':r['nominal_ai_gdp_usd']-l['nominal_ai_gdp_usd'],
                'nominal_level_difference_pct':(r['nominal_ai_gdp_usd']/l['nominal_ai_gdp_usd']-1)*100})
    power=[]
    for r in rows[:3]:
        gen=r['released_generated_power_Wh'];listed=r['listed_power_Wh']
        power.append({'year':r['year'],'listed_power_TWh':listed/1e12,'generated_power_TWh':gen/1e12,'generated_excess_TWh':(gen-listed)/1e12,
           'generated_excess_pct':(gen/listed-1)*100,'annual_preserving_scale':listed/gen,
           'listed_power_cost_usd':r['charged_listed_power_cost_usd'],'generated_power_cost_usd':r['released_generated_power_cost_usd'],
           'cost_difference_usd':r['released_generated_power_cost_usd']-r['charged_listed_power_cost_usd']})
    sources=json.loads((RAW/'source-case-outputs.json').read_text());comparisons=[]
    mapping={'Training Compute':'training_usd','AI Services Revenue':'services_usd','DC Labor':'dc_labor_usd','Power Costs':'power_usd',
       'AI Services Labor':'services_labor_usd','Nominal GDP':'nominal_ai_gdp_usd','Fisher Index':'fisher_chain_index','Real GDP':'real_ai_gdp_2023_usd'}
    for r in cases:
        source=next(x for x in sources[r['power_rule']+'__'+r['training_price_rule']] if x['Year']==r['year'])
        for old,new in mapping.items():
            diff=r[new]-source[old]
            comparisons.append({'power_rule':r['power_rule'],'training_price_rule':r['training_price_rule'],'year':r['year'],'metric':new,
              'source_value':source[old],'independent_value':r[new],'difference':diff,'relative_difference':diff/source[old],
              'passed':math.isclose(r[new],source[old],rel_tol=1e-12,abs_tol=1e-9)})
    OUT.mkdir(exist_ok=True)
    for name,value in [('cases',cases),('component-prices',prices),('training-reconciliation',training),('factorial-effects',effects),('power-ledger',power),('source-comparison',comparisons)]:save_csv(OUT/(name+'.csv'),value)
    result={'case_rows':len(cases),'source_cell_checks':len(comparisons),'source_cell_checks_passed':sum(c['passed'] for c in comparisons),
          'maximum_relative_source_difference':max(abs(c['relative_difference']) for c in comparisons),
          'interpretation':'Conditional accounting cases. The bridge is an alternative operations convention, not a unique correction. Whole-US GDP is outside this reconstruction.'}
    save_json(OUT/'summary.json',result);print(json.dumps(result,indent=2))
    return cases,training,prices,power,comparisons

if __name__=='__main__':main()
