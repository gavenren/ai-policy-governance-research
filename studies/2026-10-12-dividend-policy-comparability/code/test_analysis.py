import unittest
from analyze import trigger_floor,percentile,FLOOR
class PolicyTests(unittest.TestCase):
 def test_before_activation(self):self.assertEqual(trigger_floor(4,100000,5000),FLOOR)
 def test_first_strict_boundary(self):self.assertEqual(trigger_floor(5,.95*(FLOOR+850+5000),5000),FLOOR)
 def test_first_above_boundary(self):self.assertEqual(trigger_floor(5,.95*(FLOOR+850+5000)+.01,5000),FLOOR*1.12)
 def test_no_second_before_eight(self):self.assertEqual(trigger_floor(7,100000,5000),FLOOR*1.12)
 def test_second_strict_boundary(self):
  health_federal=10000-(FLOOR*1.12+850)
  self.assertEqual(9800/(FLOOR*1.12+850+health_federal),.98)
  self.assertEqual(trigger_floor(8,9800,health_federal),FLOOR*1.12)
 def test_second_above_boundary(self):self.assertEqual(trigger_floor(8,.98*(FLOOR*1.12+850+5000)+.01,5000),FLOOR*1.20)
 def test_second_uses_increased_floor(self):self.assertEqual(trigger_floor(8,.99*(FLOOR+850+5000),5000),FLOOR*1.12)
 def test_annual_reset(self):self.assertEqual(trigger_floor(8,100000,5000),FLOOR*1.20);self.assertEqual(trigger_floor(9,1000,5000),FLOOR)
 def test_upper_middle(self):self.assertEqual(percentile([-2,-1,0,3],.5),0)
 def test_strict_surplus(self):self.assertEqual(sum(x>0 for x in [-2,0,0,3])/4,.25)
 def test_median_sign_implication(self):
  for k in range(21):
   values=[-1]*(20-k)+[1]*k
   if percentile(values,.5)<0:self.assertLessEqual(sum(x>0 for x in values)/len(values),.5)
if __name__=='__main__':unittest.main()
