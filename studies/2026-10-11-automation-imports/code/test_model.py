"""Checks use resource accounting, numerical search, and root boundaries."""
import math, random, unittest
from dataclasses import replace
from model import State,allocation,changes,coefficients,safe_interval,safe_maximum,robust_interval,robust_maximum
class ModelTests(unittest.TestCase):
    def test_resource_accounting_and_direct_production(self):
        rng=random.Random(6006)
        for _ in range(300):
            s=State(A=rng.uniform(8,20),d=rng.uniform(0,2),theta=rng.uniform(0,.99),efficiency=rng.uniform(.3,1),fixed_cost=rng.uniform(0,1))
            t=rng.uniform(0,s.choke);r=allocation(s,t)
            direct=s.A*r['imports']-s.b*r['imports']**2/2-r['user_price']*r['imports']
            self.assertAlmostEqual(direct,r['domestic_profit'],places=10)
            self.assertAlmostEqual(r['resource_residual'],0.,places=10)
            self.assertAlmostEqual(r['recipient_consumption']*s.recipients+r['owners_total_consumption'],r['domestic_consumption'],places=10)
    def test_polynomials_match_independent_allocation(self):
        for d in [0,.1,.25,1]:
            for e in [.3,.75,1]:
                s=State(d=d,efficiency=e,fixed_cost=.3)
                for t in [.01,1,3,7,10]:
                    r=changes(s,t)
                    for key,share in [('net_funding',s.theta),('domestic_change',1.)]:
                        a,b=coefficients(s,share)
                        self.assertAlmostEqual(r[key],a*t-b*t*t-s.fixed_cost,places=10)
    def test_global_loss_identity(self):
        for s in [State(),State(d=0),State(efficiency=.75),State(fixed_cost=.5)]:
            for t in [.01,1,4,10]:
                r=changes(s,t)
                loss=-t*t/(2*s.slope)-(1-s.efficiency)*t*r['imports']-s.fixed_cost
                self.assertAlmostEqual(r['global_change'],loss,places=10)
                self.assertLess(r['global_change'],0.)
    def test_small_country_and_collection_failure(self):
        for s in [State(d=0),State(efficiency=.75)]:
            self.assertIsNone(safe_interval(s,0))
            self.assertEqual(safe_maximum(s)['net_funding'],0.)
            for t in [.01,1,5,10]: self.assertLess(changes(s,t)['domestic_change'],0.)
    def test_safe_optimum_against_dense_direct_search(self):
        for s in [State(),State(theta=.8),State(d=1),State(fixed_cost=.5),State(fixed_cost=2),State(A=10)]:
            best=0.
            for i in range(20001):
                r=changes(s,s.choke*i/20000)
                if r['domestic_change']>=-1e-10:best=max(best,r['net_funding'])
            ans=safe_maximum(s)
            self.assertGreaterEqual(ans['net_funding']+1e-8,best)
            self.assertLess(ans['net_funding']-best,.006)
            self.assertGreaterEqual(changes(s,ans['tax'])['domestic_change'],-1e-8)
    def test_roots_and_activation_cost(self):
        s=State(fixed_cost=.5);iv=safe_interval(s,8.)
        self.assertIsNotNone(iv);lo,hi=iv
        self.assertGreater(lo,0.)
        for t in [lo,(lo+hi)/2,hi]:
            self.assertGreaterEqual(changes(s,t)['net_funding'],8.-1e-8)
            self.assertGreaterEqual(changes(s,t)['domestic_change'],-1e-8)
        self.assertLess(changes(s,hi+1e-4)['domestic_change'],0)
        self.assertEqual(changes(s,0)['fixed_cost_paid'],0)
    def test_common_policy_and_target_failure(self):
        states=[State(),State(d=.1)];r=robust_maximum(states)
        for s in states:
            row=changes(s,r['tax'])
            self.assertGreaterEqual(row['net_funding'],r['net_funding']-1e-8)
            self.assertGreaterEqual(row['domestic_change'],-1e-8)
        self.assertIsNone(robust_interval(states,r['net_funding']+.001))
        self.assertIsNone(robust_interval(states+[State(d=0)],.01))
    def test_caps_and_invalid_inputs(self):
        self.assertLessEqual(safe_maximum(State(),cap=1)['tax'],1)
        with self.assertRaises(ValueError):State(b=0)
        with self.assertRaises(ValueError):State(theta=1)
        with self.assertRaises(ValueError):allocation(State(),-1)
        with self.assertRaises(ValueError):allocation(State(),11)
        with self.assertRaises(ValueError):allocation(State(),math.nan)
if __name__=='__main__':unittest.main()
