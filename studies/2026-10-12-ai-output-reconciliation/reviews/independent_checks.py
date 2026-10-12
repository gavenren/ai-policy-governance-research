"""Separate review calculation. Does not import author or original source code.

Uses 50-digit Decimal arithmetic and explicit cumulative prices/quantities.
Raw annual aggregates remain source-derived inputs; this is not an independent
reconstruction of individual GPU records or an empirical validation of them.
Run from any directory. Writes only this review's JSON result.
"""
from pathlib import Path
from decimal import Decimal as D, getcontext
from datetime import datetime, timezone
import csv, hashlib, json, sys

getcontext().prec = 50
STUDY = Path(__file__).resolve().parents[1]
RAW, OUT = STUDY/'data/raw', STUDY/'results'
START = datetime.now(timezone.utc).isoformat()
TOL = D('2e-12')
checks = []

def rows(path):
    with path.open() as f:
        return list(csv.DictReader(f))

def check(label, actual, expected, absolute=D('1e-10')):
    actual, expected = D(str(actual)), D(str(expected))
    error = abs(actual-expected)
    assert error <= max(absolute, TOL*max(abs(actual),abs(expected))), (label,str(actual),str(expected))
    checks.append({'check':label,'actual':str(actual),'independent':str(expected),'absolute_error':str(error)})

raw = {(r['power_rule'],int(r['year'])):{k:(v if k=='power_rule' else D(v)) for k,v in r.items()} for r in rows(RAW/'annual-inputs.csv')}
years = [2023,2024,2025]
a = (D(1)/8).sqrt()  # 0.5 ** (12/8), independent from saved float constant
b = D('2.2')/35
names = ['training','services','dc_labor','power','services_labor']
signs = [1,1,-1,-1,-1]
cases, prices = {}, {}
for power in ['released','annual_preserving']:
    for convention in ['released','operations_bridge']:
        previous_q = previous_p = previous_v = None
        chains = [D(100)]*3
        for year in years:
            r = raw[power,year]
            spending = r['compute_spending_usd']
            # Use level prices from 2023 and derive quantities from each value.
            # Price * quantity cross-products supply Laspeyres and Paasche.
            training_price = a**(year-2023)
            if convention == 'operations_bridge':
                base = raw[power,2023]
                training_price *= (spending/base['compute_spending_usd'])/(r['physical_bit_ops']/base['physical_bit_ops'])
            p = [training_price,b**(year-2023),D(1),r['electricity_price_usd_per_kWh']/raw[power,2023]['electricity_price_usd_per_kWh'],D(1)]
            v = [spending/2,spending*D('.75'),r['data_center_labor_usd'],r['listed_power_Wh']/1000*r['electricity_price_usd_per_kWh'],spending*D('.05')]
            q = [value/price for value,price in zip(v,p)]
            nominal = sum(s*value for s,value in zip(signs,v))
            assert nominal > 0
            c = {n+'_usd':v[i] for i,n in enumerate(names)}
            c['nominal_ai_gdp_usd'] = nominal
            if year == 2023:
                base_nominal = nominal
            else:
                old_nominal = sum(s*value for s,value in zip(signs,previous_v))
                current_at_old = sum(s*price*qty for s,price,qty in zip(signs,previous_p,q))
                old_at_current = sum(s*price*qty for s,price,qty in zip(signs,p,previous_q))
                assert current_at_old > 0 and old_at_current > 0
                factors = [current_at_old/old_nominal,nominal/old_at_current]
                factors.append((factors[0]*factors[1]).sqrt())
                chains = [x*y for x,y in zip(chains,factors)]
                c.update(nominal_growth_pct=(nominal/old_nominal-1)*100,
                         training_price_ratio=p[0]/previous_p[0],
                         laspeyres_numerator_usd=current_at_old,laspeyres_denominator_usd=old_nominal,
                         paasche_numerator_usd=nominal,paasche_denominator_usd=old_at_current,
                         real_growth_pct=(factors[2]-1)*100)
                for n,f in zip(['laspeyres','paasche','fisher'],factors): c[n+'_factor'] = f
                for n,price,old in zip(names,p,previous_p): prices[power,convention,year,n] = price/old
            for n,f in zip(['laspeyres','paasche','fisher'],chains): c[n+'_chain_index'] = f
            c['real_ai_gdp_2023_usd'] = base_nominal*chains[2]/100
            cases[power,convention,year] = c
            previous_q,previous_p,previous_v = q,p,v

for r in rows(OUT/'cases.csv'):
    key = (r['power_rule'],r['training_price_rule'],int(r['year']))
    for field,value in r.items():
        if field not in ['power_rule','training_price_rule','year'] and value:
            check(f'cases/{key}/{field}',value,cases[key][field])
for r in rows(OUT/'component-prices.csv'):
    key=(r['power_rule'],r['training_price_rule'],int(r['year']),r['component'])
    check(f'prices/{key}',r['price_ratio'],prices[key])
    assert int(r['sign']) == signs[names.index(r['component'])]

for r in rows(OUT/'training-reconciliation.csv'):
    power,year = r['power_rule'],int(r['year'])
    x,base = raw[power,year],raw[power,2023]
    gV = x['compute_spending_usd']/base['compute_spending_usd']
    gX = x['physical_bit_ops']/base['physical_bit_ops']
    ai = a**(year-2023)
    expected = {'nominal_training_usd':x['compute_spending_usd']/2,'physical_training_bit_ops':x['physical_bit_ops']/2,
                'rental_volume_index_2023_100':100*gV/ai,'operations_volume_index_2023_100':100*gX/ai,
                'operations_to_rental_level_ratio':gX/gV,'rental_price_index_2023_1':ai,
                'operations_price_index_2023_1':ai*gV/gX,
                'rental_price_times_volume_usd':x['compute_spending_usd']/2,'operations_price_times_volume_usd':x['compute_spending_usd']/2}
    if year > 2023:
        prev=raw[power,year-1];v=x['compute_spending_usd']/prev['compute_spending_usd'];q=x['physical_bit_ops']/prev['physical_bit_ops']
        expected.update(nominal_spending_growth_ratio=v,physical_operations_growth_ratio=q,released_training_price_ratio=a,
                        bridge_training_price_ratio=a*v/q,rental_volume_growth_pct=100*(v/a-1),operations_volume_growth_pct=100*(q/a-1),operations_to_rental_growth_ratio=q/v)
    for field,value in r.items():
        if field not in ['power_rule','year'] and value: check(f'training/{power}/{year}/{field}',value,expected[field])

contrasts = {'training_given_released_power':(('released','released'),('released','operations_bridge')),
             'training_given_annual_preserving_power':(('annual_preserving','released'),('annual_preserving','operations_bridge')),
             'power_given_released_price':(('released','released'),('annual_preserving','released')),
             'power_given_bridge_price':(('released','operations_bridge'),('annual_preserving','operations_bridge'))}
for r in rows(OUT/'factorial-effects.csv'):
    year=int(r['year']);lo,hi=contrasts[r['contrast']];lo,hi=cases[*lo,year],cases[*hi,year]
    expected={}
    for prefix,field in [('real','real_ai_gdp_2023_usd'),('nominal','nominal_ai_gdp_usd')]:
        expected[prefix+'_level_difference_usd']=hi[field]-lo[field]
        expected[prefix+'_level_difference_pct']=100*(hi[field]/lo[field]-1)
    if year>2023: expected['real_growth_difference_pp']=hi['real_growth_pct']-lo['real_growth_pct']
    for field,value in r.items():
        if field not in ['contrast','year'] and value: check(f'effects/{r["contrast"]}/{year}/{field}',value,expected[field],D('.1') if field.endswith('_usd') else D('1e-10'))

# The first two annual totals fix the entire released geometric path.
listed=[D('28.7')*10**12,D('72.3')*10**12,D(138)*10**12]
annual_ratio=listed[1]/listed[0];monthly_ratio=annual_ratio**(D(1)/12)
first=listed[0]*(monthly_ratio-1)/(annual_ratio-1)
generated=[listed[0],listed[1],listed[1]**2/listed[0]]
for r in rows(RAW/'monthly-power.csv'):
    year,month=map(int,r['month'].split('-'));i=(year-2023)*12+month-1
    expected=first*monthly_ratio**i
    if r['power_rule']=='annual_preserving': expected*=listed[year-2023]/generated[year-2023]
    check(f'monthly/{r["power_rule"]}/{r["month"]}',r['power_Wh'],expected)
for r in rows(OUT/'power-ledger.csv'):
    year=int(r['year']);i=year-2023;price=raw['released',year]['electricity_price_usd_per_kWh']
    expected={'listed_power_TWh':listed[i]/10**12,'generated_power_TWh':generated[i]/10**12,
              'generated_excess_TWh':(generated[i]-listed[i])/10**12,'generated_excess_pct':100*(generated[i]/listed[i]-1),
              'annual_preserving_scale':listed[i]/generated[i],'listed_power_cost_usd':listed[i]*price/1000,
              'generated_power_cost_usd':generated[i]*price/1000,'cost_difference_usd':(generated[i]-listed[i])*price/1000}
    for field,value in r.items():
        if field!='year':check(f'power/{year}/{field}',value,expected[field],D('1e-4') if field.endswith('_usd') else D('1e-10'))
    for field in ['compute_spending_usd','physical_bit_ops','data_center_labor_usd']:
        check(f'annual-scaled/{year}/{field}',raw['annual_preserving',year][field],raw['released',year][field]*listed[i]/generated[i])

source_names={'Training Compute':'training_usd','AI Services Revenue':'services_usd','DC Labor':'dc_labor_usd','Power Costs':'power_usd','AI Services Labor':'services_labor_usd','Nominal GDP':'nominal_ai_gdp_usd','Fisher Index':'fisher_chain_index','Real GDP':'real_ai_gdp_2023_usd'}
source_count=0
for key,values in json.loads((RAW/'source-case-outputs.json').read_text()).items():
    power,convention=key.split('__')
    for r in values:
        for field,dest in source_names.items():
            check(f'source/{key}/{r["Year"]}/{field}',r[field],cases[power,convention,r['Year']][dest]);source_count+=1

printed=[]
for target in rows(RAW/'printed-targets.csv'):
    m=target['metric'];year=int(target['year']) if target['year'] else None
    x=raw.get(('released',year));prev=raw.get(('released',year-1)) if year else None
    if m=='compute_spending_B': value=x['compute_spending_usd']/10**9
    elif m=='spending_growth_pct': value=100*(x['compute_spending_usd']/prev['compute_spending_usd']-1)
    elif m=='h100_equivalent':value=x['physical_bit_ops']/D(499277952000000000000000)
    elif m=='compute_growth_pct':value=100*(x['physical_bit_ops']/prev['physical_bit_ops']-1)
    elif m.startswith('qa_'):
        iq=100*(x['compute_spending_usd']/prev['compute_spending_usd']/b-1);tq=100*(x['physical_bit_ops']/prev['physical_bit_ops']/a-1)
        value={'qa_inference':iq,'qa_training':tq,'qa_production':(iq+tq)/2}[m]
    elif m=='listed_power_TWh':value=x['listed_power_Wh']/10**12
    elif m=='power_price':value=x['electricity_price_usd_per_kWh']
    elif m=='training_deflator':value=a
    elif m=='inference_deflator':value=b
    elif m.endswith('labor_deflator'):value=D(1)
    else:value=cases['released','released',year][m.removesuffix('_B')]/(10**9 if m.endswith('_B') else 1)
    # Decimal formatting keeps ties-to-even and does not use intermediate rounding.
    shown=format(value,target['format']);wanted=format(D(target['printed_value']),target['format'])
    match=D(shown)==D(wanted)
    printed.append({'metric':m,'year':year,'independent_display':shown,'printed_display':wanted,'pass':match})
assert len(printed)==54 and sum(x['pass'] for x in printed)==52
assert {(x['metric'],x['year']) for x in printed if not x['pass']}=={('fisher_chain_index',2024),('real_growth_pct',2024)}

# Check each numerical cell in the manuscript's three result tables.
paper=(STUDY/'paper.md').read_text()
table_checks=[]
for year in years:
    i=year-2023
    cells=[str(year),f'{listed[i]/10**12:.2f}',f'{generated[i]/10**12:.2f}',f'{listed[i]/generated[i]:.4f}']
    table_checks.append({'table':'power','cells':cells})
for year in [2024,2025]:
    r=raw['released',year];p=raw['released',year-1]
    vg=r['compute_spending_usd']/p['compute_spending_usd'];xg=r['physical_bit_ops']/p['physical_bit_ops']
    table_checks.append({'table':'training','cells':[str(year),f'{100*(vg/a-1):.1f}',f'{100*(xg/a-1):.1f}',f'{a*vg/xg:.6f}']})
for power in ['released','annual_preserving']:
    for convention in ['released','operations_bridge']:
        cells=[f'{cases[power,convention,2024]["real_growth_pct"]:,.1f}',f'{cases[power,convention,2025]["real_growth_pct"]:,.1f}',f'{cases[power,convention,2025]["fisher_chain_index"]:,.1f}']
        table_checks.append({'table':'four_cases','cells':cells})
for r in table_checks:
    assert all(cell in paper for cell in r['cells']),r

result={'started_utc':START,'completed_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,
        'method':'50-digit Decimal, explicit cumulative prices and quantities, signed cross-valuations; no author or original code imported',
        'scope_limit':'Source-derived aggregate inputs are accepted for this check. Detailed GPU rows and the full source model are not executed.',
        'relative_tolerance':str(TOL),'pass':True,'numeric_comparisons':len(checks),'case_rows':12,'source_cells':source_count,
        'monthly_rows':72,'component_price_rows':40,'training_rows':6,'factorial_rows':12,'power_rows':3,
        'printed_cells':printed,'manuscript_table_checks':table_checks,'checks':checks,
        'own_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(Path(__file__).parent/'independent-check-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['completed_utc','pass','numeric_comparisons','case_rows','source_cells','own_sha256']},indent=2))
