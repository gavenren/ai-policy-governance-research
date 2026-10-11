import unittest
from fractions import Fraction as F
import model
class Tests(unittest.TestCase):
 def setUp(self):self.c={x['name']:x for x in model.design()['scenarios']}
 def test_risk_premium_does_not_fund_floor(self):
  c=self.c['risk_premium'];self.assertEqual(model.balances(c,1,0),[-40,60]);self.assertEqual(model.capital_need(c,1),55)
 def test_fiscal_hedge(self):self.assertEqual(model.best_hedge(self.c['fiscal_hedge']),(F(1,2),F(15)))
 def test_common_loss(self):self.assertEqual(model.best_hedge(self.c['common_loss']),(F(0),F(0)))
 def test_three_state_interior(self):self.assertEqual(model.best_hedge(self.c['three_states']),(F(1,3),F(16)))
 def test_independent_accounting_and_minimality(self):
  for c in self.c.values():
   for a in [F(i,20) for i in range(21)]:
    C=model.capital_need(c,a);m,p,y,t,r,P=model.unpack(c)
    B=max(a*P-C,0);S=max(C-a*P,0)
    self.assertEqual(C+B,a*P+S)
    vals=[a*y[i]+r*S-r*B+t[i] for i in range(len(y))]
    self.assertGreaterEqual(min(vals),c['floor'])
    if C>0:self.assertLess(min(x-r*F(1,100000) for x in vals),c['floor'])
    self.assertEqual(sum(m[i]*vals[i] for i in range(len(y))),C+sum(m[i]*t[i] for i in range(len(y))))
 def test_independent_dense_share_search(self):
  for c in self.c.values():
   a,g=model.best_hedge(c)
   for i in range(1001):self.assertGreaterEqual(g,model.guaranteed_without_capital(c,F(i,1000)))
 def test_probability_does_not_change_guarantee(self):
  c=self.c['risk_premium'];other=dict(c,probabilities=['9/10','1/10'])
  self.assertEqual(model.capital_need(c,1),model.capital_need(other,1))
 def test_default_requires_repricing(self):
  m,p,y,t,r,P=model.unpack(self.c['risk_premium']);proceeds=sum(q*min(x,40) for q,x in zip(m,y))
  self.assertEqual(proceeds,16);self.assertEqual(P-proceeds,24)
  self.assertEqual(sum(q*min(x,100) for q,x in zip(m,y)),P)
 def test_safe_asset_and_limits(self):
  c=self.c['safe_asset'];self.assertEqual(model.capital_need(c,1),F(100,7))
  with self.assertRaises(AssertionError):model.balances(c,F(11,10),0)
if __name__=='__main__':unittest.main()
