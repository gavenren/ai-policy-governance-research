import json, math, random, unittest
from pathlib import Path
from model import assess,bond_interval,maximum_floor,solve
B=json.loads((Path(__file__).resolve().parents[1]/'data/design.json').read_text())['base']

class AgreementTests(unittest.TestCase):
    def test_one_state_known_bound(self):
        c={**B,'gain':[10],'cost':[0],'own_income':[0],'provider_resources':[20],'domestic_minimum':[0],'transition':[[1]]}
        self.assertAlmostEqual(maximum_floor(c),8,places=7)
        self.assertTrue(assess(c,8)['feasible']);self.assertFalse(assess(c,8.01)['feasible'])
    def test_independent_state_hand_calculation(self):
        a=assess(B,6)
        self.assertEqual(a['transfers'],[3,7]);self.assertAlmostEqual(a['provider_value'][0],25);self.assertAlmostEqual(a['provider_value'][1],15)
        self.assertAlmostEqual(a['enforcement_margin'][1],9);self.assertAlmostEqual(maximum_floor(B),7.8,places=7)
    def test_persistence_closed_form(self):
        c={**B,'persistence':.95};a=assess(c,6)
        self.assertAlmostEqual(a['provider_value'][1],15/7)
        self.assertAlmostEqual(a['enforcement_margin'][1],-27/7)
        self.assertAlmostEqual(maximum_floor(c),183/35,places=7)
    def test_total_wealth_does_not_create_enforcement(self):
        c={**B,'persistence':.95};rich={**c,'provider_resources':[200,200]}
        self.assertEqual(assess(c,6)['enforcement_margin'],assess(rich,6)['enforcement_margin'])
        self.assertAlmostEqual(maximum_floor(c),maximum_floor(rich),places=7)
    def test_financed_deposit_accounting(self):
        c={**B,'persistence':.95,'bond_cap':12,'carry_cost':.05};lo,hi=bond_interval(c,6)
        self.assertAlmostEqual(lo,135/28);self.assertAlmostEqual(hi,60/7)
        a=assess(c,6,lo);self.assertTrue(a['feasible'])
        # Stock principal is absent from compliant-period budget; only its carry cost appears.
        self.assertAlmostEqual(a['provider_net'][0],12-3-.05*lo)
        self.assertAlmostEqual(a['enforcement_margin'][1],0)
    def test_expensive_deposit_reduces_margin(self):
        c={**B,'persistence':.95,'bond_cap':12,'carry_cost':.3}
        a=assess(c,6);b=assess(c,6,10)
        self.assertAlmostEqual(b['enforcement_margin'][1]-a['enforcement_margin'][1],-2)
        self.assertIsNone(bond_interval(c,6))
    def test_zero_bond_effect_threshold(self):
        c={**B,'bond_cap':12,'carry_cost':.25}
        self.assertAlmostEqual(assess(c,6,4)['enforcement_margin'][1],assess(c,6,0)['enforcement_margin'][1])
    def test_higher_transfer_worsens_constraints(self):
        for f in [0,2,4,6,8]:
            a=assess(B,f);b=assess(B,f+.5)
            for key in ['provider_value','enforcement_margin','domestic_margin']:
                self.assertTrue(all(y<=x+1e-10 for x,y in zip(a[key],b[key])))
    def test_linear_solver_against_iterated_value(self):
        rng=random.Random(901)
        for _ in range(100):
            d=rng.uniform(.1,.95);q=rng.random();k=[rng.uniform(2,20),rng.uniform(2,20)]
            c={**B,'discount':d,'persistence':q,'gain':k};a=assess(c,6);v=[0.,0.]
            for j in range(1500):v=[a['provider_net'][0]+d*(q*v[0]+(1-q)*v[1]),a['provider_net'][1]+d*((1-q)*v[0]+q*v[1])]
            for x,y in zip(a['provider_value'],v):self.assertAlmostEqual(x,y,places=8)
    def test_interval_against_direct_constraints(self):
        for d in [.5,.8,.95]:
            for q in [.1,.5,.95]:
                for r in [0,.05,.3]:
                    c={**B,'discount':d,'persistence':q,'carry_cost':r,'bond_cap':12};iv=bond_interval(c,6)
                    for i in range(1201):
                        b=i/100;direct=assess(c,6,b)['feasible'];inside=iv is not None and iv[0]-1e-9<=b<=iv[1]+1e-9
                        self.assertEqual(direct,inside)
    def test_binding_domestic_rule_and_no_surplus(self):
        self.assertIsNone(maximum_floor({**B,'domestic_minimum':[26,26]}))
        c={**B,'gain':[0,0],'cost':[0,0]};self.assertAlmostEqual(maximum_floor(c),0,places=7)
    def test_invalid_inputs(self):
        for change in [{'discount':1},{'discount':float('nan')},{'persistence':1.1},{'carry_cost':-.1},{'gain':[1]},{'transition':[[1,1],[0,1]]}]:
            with self.assertRaises(ValueError):assess({**B,**change},6)
        with self.assertRaises(ValueError):assess(B,float('nan'))

if __name__=='__main__':unittest.main()
