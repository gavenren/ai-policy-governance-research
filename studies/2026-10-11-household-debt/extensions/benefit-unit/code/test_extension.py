import unittest
import numpy as np
import pandas as pd
from analyze import calibrated_transfer, outcome_vectors, derive_members, statistics, combine
from check_feasibility import FIELDS,REL,AGE,DEP

def roster_row(ages,dependent=None):
    row={f:0 for f in FIELDS}
    dep=dependent or [True]*len(ages)
    row.update(YY1=1,Y1=11,X7001=sum(dep),X7020=2 if len(ages)>1 and dep[1] else 1,X101=len(ages),X42001=1)
    for j,age in enumerate(ages):
        row[AGE[j]]=age;row[DEP[j]]=1 if dep[j] else 5;row[REL[j]]=1 if j==0 else 2 if j==1 else 4
    return row

class ExtensionTests(unittest.TestCase):
    def test_equal_weighted_budget(self):
        u,c,e=calibrated_transfer(np.array([1.,2.,3.]),np.array([1.,2.,1.]))
        self.assertEqual(c,1000);np.testing.assert_array_equal(u,[1000,2000,3000]);self.assertEqual(e,0)
    def test_square_root_worked_example(self):
        u,c,_=calibrated_transfer(np.array([1.,2.]),np.ones(2))
        self.assertAlmostEqual(c,4000/3);self.assertAlmostEqual(u.sum(),4000)
    def test_refit_with_replicate_weights(self):
        v=np.array([1.,2.])
        _,c1,_=calibrated_transfer(v,np.array([1.,1.]))
        _,c2,_=calibrated_transfer(v,np.array([2.,1.]))
        self.assertAlmostEqual(c1,4000/3);self.assertEqual(c2,1500)
    def test_payment_resource_example(self):
        v=outcome_vectors(np.array([500.]),np.array([1800.]),np.array([2000.]),np.array([1000.]))
        self.assertEqual(v['gross_pass'][0],1);self.assertEqual(v['after_pass'][0],0)
        self.assertEqual(v['classification_gap'][0],1);self.assertEqual(v['shortfall'][0],300)
    def test_age18_is_adult_17_is_child(self):
        d=pd.DataFrame([roster_row([40,18,17,25])])
        n,a=derive_members(d);self.assertEqual(n[0],4);self.assertEqual(a[0],3)
    def test_independent_resident_not_in_peu(self):
        d=pd.DataFrame([roster_row([40,40,25],[True,True,False])])
        n,a=derive_members(d);self.assertEqual(n[0],2);self.assertEqual(a[0],2)
    def test_zero_adult_stops(self):
        with self.assertRaisesRegex(ValueError,'Zero-adult'):derive_members(pd.DataFrame([roster_row([17])]))
    def test_missing_member_age_stops(self):
        with self.assertRaisesRegex(ValueError,'Incomplete'):derive_members(pd.DataFrame([roster_row([40,0])]))
    def test_variance_hand_fixture(self):
        point,se=combine(np.array([[1],[2],[3],[4],[5]]),np.array([[2],[4],[6]]))
        self.assertEqual(point[0],3);self.assertAlmostEqual(se[0],np.sqrt(7))
    def test_topcode_and_paired_identity(self):
        d=pd.DataFrame(dict(INCOME=[0]*4,WAGEINC=[0]*4,TPAY=[1000,1500,2200,5000],PEU_SIZE=[1,2,3,12],ADULTS=[1,2,1,2]))
        values,_,_=statistics(d,np.ones(4))
        self.assertEqual(values['exact/allocation/family/annual_total'],72000)
        self.assertEqual(values['capped/allocation/family/annual_total'],96000)
        for sample in ['exact','capped']:
            for floor in ['sqrt','fixed']:
                for arm in ['family','adult','size']:
                    stem=f'{sample}/{floor}/{arm}/all/'
                    self.assertAlmostEqual(values[stem+'gross_pass']-values[stem+'after_pass'],values[stem+'classification_gap'])
                for metric in ['after_pass','shortfall']:
                    self.assertAlmostEqual(values[f'{sample}/{floor}/adult_minus_family/{metric}'],values[f'{sample}/{floor}/adult/all/{metric}']-values[f'{sample}/{floor}/family/all/{metric}'])

if __name__=='__main__':unittest.main()

