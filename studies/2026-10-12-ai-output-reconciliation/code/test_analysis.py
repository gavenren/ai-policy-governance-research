#!/usr/bin/env python3
"""Numerical checks of accounting identities, controls, and measured comparisons."""
import copy,csv,hashlib,json,math,unittest
from pathlib import Path
import analyze as a

class AccountingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p=json.loads((a.RAW/'parameters.json').read_text());cls.rows=a.load_rows()
        cls.cases,cls.training,cls.prices,cls.power,cls.comparisons=a.main()
        cls.lookup={(r['power_rule'],r['training_price_rule'],r['year']):r for r in cls.cases}
    def close(self,x,y):self.assertTrue(math.isclose(x,y,rel_tol=2e-12,abs_tol=1e-10),(x,y))
    def test_four_cases_and_three_years_only(self):
        self.assertEqual(len(self.cases),12);self.assertEqual(len(self.lookup),12)
    def test_all_source_gdp_cells(self):
        self.assertEqual(len(self.comparisons),96);self.assertTrue(all(r['passed'] for r in self.comparisons))
    def test_independent_quality_adjusted_controls(self):
        source=json.loads((a.RAW/'source-control.json').read_text())['baseline_qa']
        for t in self.training:
            y=t['year']
            if t['power_rule']=='released' and y>2023:
                inf=(t['nominal_spending_growth_ratio']/self.p['INFERENCE_DEFLATOR_RATIO']-1)*100
                train=t['operations_volume_growth_pct']
                for name,v in [('inference',inf),('training',train),('production',(inf+train)/2)]:self.close(v,source[f'qa_{name}_{y}'])
    def test_price_times_volume_both_conventions(self):
        for r in self.training:
            self.close(r['nominal_training_usd'],r['rental_price_times_volume_usd'])
            self.close(r['nominal_training_usd'],r['operations_price_times_volume_usd'])
    def test_null_spending_per_operation(self):
        for growth in [.25,1.0,3.5]:
            self.close(a.bridge_price(.4,growth,growth),.4)
            self.close(growth/.4,growth/a.bridge_price(.4,growth,growth))
    def test_currency_rescaling(self):
        original=[r for r in self.rows if r['power_rule']=='released'];scaled=copy.deepcopy(original);factor=.01
        for r in scaled:
            for key in r:
                if key.endswith('_usd') or key=='electricity_price_usd_per_kWh':r[key]*=factor
        for convention in ['released','operations_bridge']:
            before,_=a.reconstruct(original,self.p,convention);after,_=a.reconstruct(scaled,self.p,convention)
            for b,c in zip(before,after):
                self.close(b['fisher_chain_index'],c['fisher_chain_index'])
                self.close(b['nominal_ai_gdp_usd']*factor,c['nominal_ai_gdp_usd'])
                self.close(b['real_ai_gdp_2023_usd']*factor,c['real_ai_gdp_2023_usd'])
    def test_operations_unit_rescaling(self):
        original=[r for r in self.rows if r['power_rule']=='released'];scaled=copy.deepcopy(original)
        for r in scaled:r['physical_bit_ops']*=1e-21
        before=a.training_ledger(original,self.p);after=a.training_ledger(scaled,self.p)
        for b,c in zip(before,after):
            self.close(b['operations_volume_index_2023_100'],c['operations_volume_index_2023_100'])
            if b['year']>2023:self.close(b['bridge_training_price_ratio'],c['bridge_training_price_ratio'])
    def test_fixed_gpu_prices_do_not_imply_fixed_average_spending_per_operation(self):
        # A diagnostic two-GPU example, not another empirical accounting case.
        rates=[10,20];ops=[1,4];old=[.8,.2];new=[.2,.8]
        dot=lambda x,y:sum(v*w for v,w in zip(x,y))
        vg=dot(rates,new)/dot(rates,old);xg=dot(ops,new)/dot(ops,old)
        self.assertNotEqual(vg,xg);self.assertLess(a.bridge_price(.4,vg,xg),.4)
        self.assertEqual(rates,[10,20])
    def test_annual_totals_match(self):
        for r in self.rows:
            if r['power_rule']=='annual_preserving':self.close(r['selected_power_Wh'],r['listed_power_Wh'])
    def test_monthly_profile_and_uniform_annual_scale(self):
        with (a.RAW/'monthly-power.csv').open() as f:rows=list(csv.DictReader(f))
        lookup={(r['power_rule'],r['month']):float(r['power_Wh']) for r in rows}
        for y in [2023,2024,2025]:
            ratios=[lookup['annual_preserving',f'{y}-{m:02d}']/lookup['released',f'{y}-{m:02d}'] for m in range(1,13)]
            self.assertTrue(all(math.isclose(x,ratios[0],rel_tol=2e-14) for x in ratios))
        self.assertTrue(json.loads((a.RAW/'source-control.json').read_text())['source_checks']['row_allocation_and_composition_preserved'])
    def test_all_generated_costs_separate_from_charged_costs(self):
        for r in self.rows:
            self.close(r['charged_listed_power_cost_usd'],r['listed_power_Wh']/1000*r['electricity_price_usd_per_kWh'])
        self.assertGreater(self.power[-1]['generated_power_cost_usd'],self.power[-1]['listed_power_cost_usd'])
    def test_signed_component_boundary(self):
        for r in self.cases:
            self.close(r['nominal_ai_gdp_usd'],r['training_usd']+r['services_usd']-r['dc_labor_usd']-r['power_usd']-r['services_labor_usd'])
    def test_price_only_nominal_null_and_direction(self):
        for power in ['released','annual_preserving']:
            for y in [2023,2024,2025]:
                old=self.lookup[power,'released',y];new=self.lookup[power,'operations_bridge',y]
                self.close(old['nominal_ai_gdp_usd'],new['nominal_ai_gdp_usd'])
                if y>2023:
                    self.assertLess(new['training_price_ratio'],old['training_price_ratio'])
                    self.assertGreater(new['fisher_factor'],old['fisher_factor'])
    def test_positive_factors_and_fisher_geometric_mean(self):
        for r in self.cases:
            self.assertGreater(r['nominal_ai_gdp_usd'],0)
            if r['year']>2023:
                for k in ['laspeyres_numerator_usd','laspeyres_denominator_usd','paasche_numerator_usd','paasche_denominator_usd','laspeyres_factor','paasche_factor']:self.assertGreater(r[k],0)
                self.close(r['fisher_factor']**2,r['laspeyres_factor']*r['paasche_factor'])
    def test_reject_invalid_nominal(self):
        with self.assertRaises(ValueError):a.fisher_step([1,0,2,0,0],[1,0,2,0,0],[1]*5)
    def test_reject_invalid_paasche_denominator(self):
        with self.assertRaises(ValueError):a.fisher_step([1,1,0,0,1.5],[1,1,0,0,1.5],[.1,.1,1,1,1])
    def test_reject_invalid_laspeyres_numerator(self):
        with self.assertRaises(ValueError):a.fisher_step([1,1,0,0,1.5],[1,1,0,0,1.5],[10,10,1,1,1])
    def test_reject_nonfinite_price(self):
        with self.assertRaises(ValueError):a.fisher_step([2,2,0,0,0],[2,2,0,0,0],[float('nan'),1,1,1,1])
    def test_level_growth_separation(self):
        for power in ['released','annual_preserving']:
            for price in ['released','operations_bridge']:
                for y in [2024,2025]:
                    old=self.lookup[power,price,y-1];new=self.lookup[power,price,y]
                    self.close(new['real_growth_pct'],(new['real_ai_gdp_2023_usd']/old['real_ai_gdp_2023_usd']-1)*100)
    def test_power_change_does_not_change_bridge(self):
        t={(r['power_rule'],r['year']):r for r in self.training}
        for y in [2024,2025]:self.close(t['released',y]['bridge_training_price_ratio'],t['annual_preserving',y]['bridge_training_price_ratio'])
    def test_first_two_years_preserved_with_roundoff(self):
        for r in self.rows:
            if r['year']<2025:self.close(r['selected_power_Wh'],r['listed_power_Wh'])

if __name__=='__main__':unittest.main(verbosity=2)
