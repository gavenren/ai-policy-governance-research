"""Meaningful boundary cases and counterexamples, not empirical validation."""
import unittest
from fractions import Fraction as F
from analyze import raw,capped,floor_awards

class AllocationChecks(unittest.TestCase):
    def test_source_table(self):
        a=raw([700000,600000,400000,900000,200000],[7,6,3,3,1],1800000)
        self.assertEqual(a,(F(700000),F(3600000,7),F(1200000,7),F(2700000,7),F(200000,7)))
        self.assertEqual(capped([700000,600000,400000,900000,200000],[7,6,3,3,1],1800000)[0],a)
    def test_source_shock(self):
        d,w=[700000,600000,400000,900000,200000],[7,6,3,3,1]
        self.assertEqual(raw(d,w,1200000),tuple(x*F(2,3) for x in raw(d,w,1800000)))
    def test_raw_over_fulfillment_and_cap(self):
        self.assertEqual(raw([1,9],[9,1],5),(F(5,2),F(5,2)))
        self.assertEqual(capped([1,9],[9,1],5),((F(1),F(4)),F(0)))
    def test_zero_residual_breaks_exhaustion(self):
        self.assertEqual(floor_awards([1,1],[2,1],3,[1,1]),((F(1),F(1)),F(1)))
    def test_no_residual_capacity(self):
        self.assertEqual(floor_awards([4,5],[2,1],3,[1,2],True),((F(1),F(2)),F(0)))
    def test_floor_can_exceed_own_use(self):
        self.assertEqual(floor_awards([1,3],[2,1],7,[2,3],True),((F(2),F(3)),F(2)))
    def test_impossible_floor_rejected(self):
        with self.assertRaises(ValueError):floor_awards([2,3],[1,1],2,[1,2])
    def test_composition_failures_with_inactive_caps(self):
        small,large=raw([2,2],[2,1],1),raw([2,2],[2,1],2)
        self.assertEqual(raw(large,[2,1],1),(F(4,5),F(1,5)))
        left=tuple(F(2)-x for x in small)
        up=tuple(x+y for x,y in zip(small,raw(left,[2,1],1)))
        self.assertEqual(up,(F(50,39),F(28,39)))
        self.assertNotEqual(up,large);self.assertNotEqual(raw(large,[2,1],1),small)
        for d,b in [([2,2],1),([2,2],2),(large,1),(left,1)]:self.assertEqual(capped(d,[2,1],b)[0],raw(d,[2,1],b))
    def test_fixed_claim_additivity_and_scale(self):
        d,w=[2,3,5],[3,2,1]
        self.assertEqual(raw(d,w,5),tuple(x+y for x,y in zip(raw(d,w,2),raw(d,w,3))))
        self.assertEqual(raw(d,w,5),raw(d,[30,20,10],5))
    def test_subset_consistency(self):
        a=raw([2,3,5],[3,2,1],4)
        self.assertEqual(raw([2,5],[3,1],a[0]+a[2]),(a[0],a[2]))
    def test_equal_weights_restore_standard_composition(self):
        a=raw([2,6],[1,1],4);small=raw([2,6],[1,1],2)
        self.assertEqual(raw(a,[1,1],2),small)
        self.assertEqual(tuple(x+y for x,y in zip(small,raw([F(2)-small[0],F(6)-small[1]],[1,1],2))),a)
    def test_surplus_is_recorded(self):
        self.assertEqual(capped([1,2],[2,1],5),((F(1),F(2)),F(2)))
    def test_zero_claim_and_zero_budget(self):
        self.assertEqual(capped([0,3],[2,1],2),((F(0),F(2)),F(0)))
        self.assertEqual(capped([0,0],[2,1],2),((F(0),F(0)),F(2)))
        self.assertEqual(capped([2,3],[2,1],0),((F(0),F(0)),F(0)))
    def test_invalid_domain(self):
        for d,w,b in [([],[],1),([1],[0],1),([-1],[1],1),([1],[1],-1),([1,2],[1],1)]:
            with self.assertRaises(ValueError):capped(d,w,b)
    def test_fulfillment_ratios_change_after_caps(self):
        a=raw([1,9],[9,1],5);z,_=capped([1,9],[9,1],5)
        self.assertEqual((a[0]/1)/(a[1]/9),9)
        self.assertEqual((z[0]/1)/(z[1]/9),F(9,4))

if __name__=='__main__':unittest.main()
