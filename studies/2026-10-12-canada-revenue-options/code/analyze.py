"""Conditional Canadian revenue accounts. No tax-yield or growth forecast."""
from decimal import Decimal as D
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'data/inputs.json'
raw = json.loads(INPUT.read_text(), parse_float=D, parse_int=D)
B, A = raw['baseline'], raw['scenario_assumptions']
TARGET = B['new_revenue_target']
D0 = B['cit_replaced'] + B['retained_pit_replaced'] + B['nonresident_tax_replaced']
V0 = B['gst_replaced']
OTHER = B['remaining_revenue'] - D0 - V0
OUT = ROOT / 'results'
OUT.mkdir(exist_ok=True)


def account(package, multiple, label='standard', capital_share=None,
            consumption_share=None, collection=None, rebate_multiple=D(1), retained_relief_multiple=D(1)):
    y = B['gdp'] * multiple
    kb = A['capital_income_base_share'] if capital_share is None else capital_share
    cb = A['tax_exclusive_consumption_base_share'] if consumption_share is None else consumption_share
    ke = A['capital_collection_share'] if collection is None else collection
    ce = A['consumption_collection_share'] if collection is None else collection
    capital = y * kb * package['capital_rate'] * ke
    gst_before_relief = y * cb * package['gst_rate'] * ce
    retained_relief = A['retained_gst_credit_rebate_allowance'] * retained_relief_multiple
    gst = gst_before_relief - retained_relief
    rebate = package['new_rebate'] * rebate_multiple
    admin = A['new_tax_administration']
    new = capital + gst - D0 - V0 - rebate - admin
    gap = TARGET - new
    revenue = OTHER + capital + gst
    expense = B['post_shock_expense'] + rebate + admin
    deficit = expense - revenue
    assert deficit == B['existing_deficit'] + gap
    assert capital <= y * kb and gst >= 0
    return dict(package=package['name'], case=label, gdp_multiple=multiple,
                gdp=y, capital_base_share=kb, consumption_base_share=cb,
                capital_rate=package['capital_rate'], gst_rate=package['gst_rate'],
                capital_collection=ke, consumption_collection=ce,
                capital_receipts_total=capital, gst_before_retained_relief=gst_before_relief,
                retained_gst_relief=retained_relief, gst_receipts_total=gst,
                replaced_capital_receipts=D0, replaced_gst_receipts=V0,
                extra_rebate=rebate, extra_tax_admin=admin, net_new_resources=new,
                target=TARGET, remaining_gap=gap, total_federal_revenue=revenue,
                total_federal_expense=expense, federal_deficit=deficit)


def write_csv(name, rows):
    with (OUT/name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    assert OTHER == D('77.8')
    assert B['post_shock_expense'] - B['remaining_revenue'] - B['existing_deficit'] == TARGET
    packages = raw['packages']
    cases = [account(p, m) for p in packages for m in A['gdp_multiples']]
    stresses = []
    for p in packages:
        stresses += [account(p,D(2),label='central'),
                     account(p,D(2),label='capital_base_25pct',capital_share=D('.25')),
                     account(p,D(2),label='collection_70pct',collection=D('.70')),
                     account(p,D(2),label='consumption_base_45pct',consumption_share=D('.45')),
                     account(p,D('1.5'),label='gdp_1_5_times'),
                     account(p,D(2),label='rebate_50pct_higher',rebate_multiple=D('1.5')),
                     account(p,D(2),label='retained_gst_relief_doubled',retained_relief_multiple=D(2))]
    boundaries=[]
    for p in packages:
        rate_per_gdp=(A['capital_income_base_share']*p['capital_rate']*A['capital_collection_share']
                      + A['tax_exclusive_consumption_base_share']*p['gst_rate']*A['consumption_collection_share'])
        y=(TARGET+D0+V0+p['new_rebate']+A['new_tax_administration']+A['retained_gst_credit_rebate_allowance'])/rate_per_gdp
        boundaries.append(dict(package=p['name'], required_gdp=y,
                               required_gdp_multiple=y/B['gdp'], receipts_per_gdp=rate_per_gdp))
    single=[]
    for m in A['gdp_multiples']:
        y=B['gdp']*m
        # Existing GST stays in the capital-only case; existing capital taxes stay in the GST-only case.
        kr=(TARGET+D0+A['new_tax_administration'])/(y*A['capital_income_base_share']*A['capital_collection_share'])
        vr=(TARGET+V0+D(200)+A['new_tax_administration']+A['retained_gst_credit_rebate_allowance'])/(y*A['tax_exclusive_consumption_base_share']*A['consumption_collection_share'])
        single.append(dict(gdp_multiple=m, capital_only_required_joint_rate=kr,
                           gst_only_required_total_rate=vr, gst_only_extra_rebate=D(200)))
    fund=[dict(net_real_withdrawal_rate=r, required_unlevered_assets=TARGET/r)
          for r in raw['comparison_assumptions']['fund_net_real_withdrawal_rates']]
    debt=D(0); rate=raw['comparison_assumptions']['debt_real_interest']; borrowing=[]
    for year in range(1,int(raw['comparison_assumptions']['debt_years'])+1):
        interest=debt*rate; debt+=TARGET+interest
        borrowing.append(dict(year=year, unfunded_primary_gap=TARGET,
                              interest_on_opening_new_debt=interest, closing_new_debt=debt))
    for name,rows in [('packages.csv',cases),('stress.csv',stresses),('break_even.csv',boundaries),
                      ('single_source.csv',single),('fund_assets.csv',fund),('borrowing.csv',borrowing)]:
        write_csv(name,rows)
    scale=raw['dated_scale_comparisons']
    summary=dict(target=TARGET,replaced_capital=D0,replaced_gst=V0,other_retained=OTHER,
                 twice_gdp_packages=[r for r in cases if r['gdp_multiple']==2],
                 break_even=boundaries,
                 wealth_tax_target_share=scale['pbo_wealth_tax_2026_27_from_2025_proposal']/TARGET,
                 target_share_of_household_wealth=TARGET/scale['household_net_worth_2026_q2_rounded'],
                 fund_assets=fund, year10_debt=borrowing[-1],
                 input_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),
                 checks={'source_account_reconciles':True,'all_case_accounts_reconcile':True},
                 counts={'packages':len(cases),'stress':len(stresses),'single_source':len(single)})
    (OUT/'summary.json').write_text(json.dumps(summary,default=str,indent=2)+'\n')
    print(json.dumps(summary,default=str,indent=2))


if __name__=='__main__':
    main()
