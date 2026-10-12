import unittest
import numpy as np
import pandas as pd
from analysis import outcomes,topups,resources,weighted_quantile,combine,estimate

class AccountingTests(unittest.TestCase):
 def test_hand_worked_family(self):
  # 500 remaining income + 2000 transfer - 1800 debt = 700, below 1000.
  x=outcomes(np.array([500.]),np.array([1800.]),np.array([900.]),2000,1000)[0]
  np.testing.assert_allclose(x,[1,0,1,300,300,0,1,0])
 def test_no_debt_no_classification_gap(self):
  x=outcomes(np.array([0.,1500.]),np.zeros(2),np.zeros(2),500,1000)
  np.testing.assert_array_equal(x[:,2],0)
 def test_topup_identity(self):
  n=np.array([0.,700.,1200.,6000.]);debt=np.array([800.,800.,800.,800.]);f=1000
  t0,t1,extra=topups(n,debt,f)
  np.testing.assert_allclose(extra,np.maximum(f+debt-n-t0,0))
  self.assertTrue((extra<=debt).all())
 def test_payment_relief_can_fail_to_help_non_debtor(self):
  n=np.array([0.]);v=outcomes(n,np.zeros(1),np.zeros(1),500,1000)
  self.assertEqual(v[0,3],500)
 def test_partial_relief_equals_cash_for_immediate_budget(self):
  n=np.array([100.]);d=np.array([1000.]);l=np.array([0.])
  np.testing.assert_allclose(outcomes(n,d*.5,l,1000,1000)[:,1:4],outcomes(n,d,l,1500,1000)[:,1:4])
 def test_resources_units_clipping_and_broad_flow(self):
  d=pd.DataFrame(dict(INCOME=[24000.,10000.],WAGEINC=[12000.,12000.],BUSSEFARMINC=[6000.,-500.],KGINC=[1200.,0.],PENACCTWD=[1200.,0.]))
  n,c=resources(d,'wage_only');np.testing.assert_allclose(n,[1000,0]);np.testing.assert_array_equal(c,[False,True])
  n,c=resources(d,'wider_flow');np.testing.assert_allclose(n,[300,0])
 def test_weighted_mean_and_total(self):
  v=np.array([2.,4.]);w=np.array([1.,3.]);m=np.array([True,True])
  self.assertEqual(estimate(v,w,m,False),3.5);self.assertEqual(estimate(v,w,m,True),14)
 def test_hand_variance_fixture(self):
  # Five values have sample variance 2.5; three replicate values variance 4.
  point,se=combine([1,2,3,4,5],[2,4,6]);self.assertEqual(point,3);self.assertAlmostEqual(se,np.sqrt(7))
 def test_quantile_tie_convention(self):
  self.assertEqual(weighted_quantile([10,20,30],[1,1,2],.5),20)
 def test_transfer_and_payment_monotonicity(self):
  n=np.array([0,500,2000.]);d=np.array([0,1000,4000.]);l=np.zeros(3)
  for u in [0,1000,2000]:
   a=outcomes(n,d,l,u,1000);b=outcomes(n,d,l,u+1000,1000);c=outcomes(n,d/2,l,u,1000)
   self.assertTrue((b[:,1]>=a[:,1]).all());self.assertTrue((c[:,1]>=a[:,1]).all())
if __name__=='__main__':unittest.main()
