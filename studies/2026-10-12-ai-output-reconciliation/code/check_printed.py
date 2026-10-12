#!/usr/bin/env python3
"""Compare independent baseline values with manually transcribed printed cells.

Direct displayed-precision formatting is used, without intermediate rounding.
Failures are retained, not adjusted to fit. Source tables share some cells; the
locator column identifies each checked version, without treating them as new data.
"""
import csv,json
from pathlib import Path
from analyze import STUDY,RAW,OUT,load_rows,save_csv,save_json

def check():
    params=json.loads((RAW/'parameters.json').read_text())
    with (OUT/'cases.csv').open() as f:
        cases={int(r['year']):r for r in csv.DictReader(f) if r['power_rule']=='released' and r['training_price_rule']=='released'}
    annual={r['year']:r for r in load_rows() if r['power_rule']=='released'}
    with (RAW/'printed-targets.csv').open() as f:targets=list(csv.DictReader(f))
    checks=[]
    for t in targets:
        year=int(t['year']) if t['year'] else None;metric=t['metric'];y=annual.get(year)
        if metric=='compute_spending_B':value=y['compute_spending_usd']/1e9
        elif metric=='spending_growth_pct':value=(y['compute_spending_usd']/annual[year-1]['compute_spending_usd']-1)*100
        elif metric=='h100_equivalent':value=y['physical_bit_ops']/params['H100_OPs_per_year']
        elif metric=='compute_growth_pct':value=(y['physical_bit_ops']/annual[year-1]['physical_bit_ops']-1)*100
        elif metric.startswith('qa_'):
            previous=annual[year-1]
            inference=(y['compute_spending_usd']/previous['compute_spending_usd']/params['INFERENCE_DEFLATOR_RATIO']-1)*100
            training=(y['physical_bit_ops']/previous['physical_bit_ops']/params['TRAINING_DEFLATOR_RATIO']-1)*100
            value={'qa_inference':inference,'qa_training':training,'qa_production':(inference+training)/2}[metric]
        elif metric=='listed_power_TWh':value=y['listed_power_Wh']/1e12
        elif metric=='power_price':value=y['electricity_price_usd_per_kWh']
        elif metric=='training_deflator':value=params['TRAINING_DEFLATOR_RATIO']
        elif metric=='inference_deflator':value=params['INFERENCE_DEFLATOR_RATIO']
        elif metric in ('dc_labor_deflator','services_labor_deflator'):value=1.0
        else:
            value=float(cases[year][metric.removesuffix('_B')])/(1e9 if metric.endswith('_B') else 1)
        displayed=format(value,t['format']);target=float(t['printed_value'])
        checks.append({**t,'full_precision_value':value,'direct_display':displayed,'difference_from_printed':value-target,'passed':displayed==format(target,t['format'])})
    save_csv(OUT/'printed-cell-checks.csv',checks)
    summary={'checked_unique_cells':len(checks),'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),
      'failure_details':[{k:c[k] for k in ['metric','year','source_locators','printed_value','direct_display','full_precision_value','difference_from_printed']} for c in checks if not c['passed']],
      'rule':'Direct formatting from full precision, with no intermediate rounding. Multiple matching source versions share a row and locator list.',
      'rounding_conjecture':'The two 2024 failures are consistent with first rounding the source result to one decimal and then to an integer. The paper tables do not state that rule, so it is not used to turn failures into passes.'}
    save_json(OUT/'printed-check-summary.json',summary);print(json.dumps(summary,indent=2));return checks
if __name__=='__main__':check()
