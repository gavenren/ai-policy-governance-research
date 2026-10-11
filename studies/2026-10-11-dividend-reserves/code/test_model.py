import math,unittest
from fractions import Fraction as F
import model

class ModelTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.c=model.read_design();cls.pp=list(model.paths(cls.c,'joint_allowed'))
  cls.lines=model.constraints(cls.c,cls.pp,2,F(1,5))
 def test_complete_enumeration_counts(self):
  n=8;k=3
  count=sum(math.comb(n,i) for i in range(k+1))
  self.assertEqual(len(self.pp),count**2)
  disjoint=sum(math.comb(n,a)*sum(math.comb(n-a,b) for b in range(min(k,n-a)+1)) for a in range(k+1))
  self.assertEqual(len(list(model.paths(self.c,'no_overlap'))),disjoint)
  self.assertEqual(len(list(model.paths(self.c,'common_only'))),count)
 def test_same_terminal_total_different_bridge(self):
  early=((1,1,1,0,0,0,0,0),)*2;late=((0,0,0,0,0,1,1,1),)*2
  self.assertEqual(model.need(self.c,early,0,2,F(1,5))[0],21)
  self.assertEqual(model.need(self.c,late,0,2,F(1,5))[0],11)
  self.assertEqual(model.trajectory(self.c,early,0,0,2,F(1,5))[-1],model.trajectory(self.c,late,0,0,2,F(1,5))[-1])
 def test_sale_stock_and_receipt_accounting(self):
  p=((0,)*8,)*2
  v=model.trajectory(self.c,p,100,0,2,F(1,5))
  self.assertEqual(v[:3],[F(-3),F(74),F(71)])
  with self.assertRaises(ValueError):model.trajectory(self.c,p,101,0,2,0)
  with self.assertRaises(ValueError):model.trajectory(self.c,p,-1,0,2,0)
 def test_known_interior_optimum(self):
  self.assertEqual(model.optimize(self.lines,100),(F(700,39),F(280,39)))
  self.assertEqual(model.optimize(self.lines,0),(F(0),F(21)))
  self.assertEqual(model.optimize(self.lines,100,1),(F(0),F(21)))
 def test_all_paths_via_independent_cash_loop(self):
  # Separate direct period budget test does not call model.trajectory or need.
  q=F(700,39);r=F(280,39);minimum=F(1000);failures=0
  for tax,div in self.pp:
   cash=r;lowcash=r-F(1,100000)
   for t in range(8):
    inflow=(2 if tax[t] else 7)+(1-q/100)*(1 if div[t] else 5)
    if t==1:inflow+=q*F(4,5)
    cash+=inflow-10;lowcash+=inflow-10
    minimum=min(minimum,cash)
    if lowcash<0:failures+=1
   self.assertGreaterEqual(cash,0)
  self.assertEqual(minimum,0);self.assertGreater(failures,0)
 def test_late_sale_can_worsen_reserve(self):
  lines=model.constraints(self.c,self.pp,4,F(1,5))
  self.assertEqual(model.optimize(lines,100),(F(0),F(21)))
  self.assertEqual(model.reserve(lines,25),F(87,4))
  self.assertEqual(model.reserve(lines,100),24)
 def test_income_rights_timing_is_material(self):
  lines=model.constraints(self.c,self.pp,4,F(1,5),income_loss_start=4)
  self.assertEqual(model.reserve(lines,100),21)
  p=((1,1,1,0,0,0,0,0),)*2
  self.assertEqual(model.trajectory(self.c,p,100,21,4,F(1,5),4)[2],0)
 def test_sale_with_no_net_proceeds_is_never_needed(self):
  lines=model.constraints(self.c,self.pp,2,1)
  self.assertEqual(model.optimize(lines,100),(F(0),F(21)))
 def test_no_overlap_certificate_fails_joint_path(self):
  lines=model.constraints(self.c,list(model.paths(self.c,'no_overlap')),2,F(1,5))
  q,r=model.optimize(lines,100)
  p=((1,1,1,0,0,0,0,0),)*2
  self.assertLess(min(model.trajectory(self.c,p,q,r,2,F(1,5))),0)
 def test_envelope_agrees_with_direct_paths_and_grid(self):
  # A smaller separate design spans all 256 two-stream paths.
  c=dict(self.c,horizon=4,max_tax_shocks=4,max_fund_shocks=4)
  pp=list(model.paths(c,'joint_allowed'));lines=model.constraints(c,pp,3,F(1,2))
  q,r=model.optimize(lines,100)
  for sale in range(101):
   direct=max(model.need(c,p,sale,3,F(1,2))[0] for p in pp)
   self.assertEqual(model.reserve(lines,sale),direct)
   self.assertGreaterEqual(direct,r)
  self.assertEqual(model.reserve(lines,q),r)

if __name__=='__main__':unittest.main()
