import unittest
from analyze import analyze,coverage,read_rows,within_announced_horizon
class AuditTests(unittest.TestCase):
    def setUp(self): self.rows=read_rows();self.by={r['deployment_id']:r for r in self.rows}
    def test_unique_keys(self): self.assertEqual(len(self.by),4)
    def test_same_model_different_platform(self):
        x=coverage([self.by['A'],self.by['B']],self.rows)
        self.assertFalse(x['model_pass']);self.assertTrue(x['platform_pass'])
    def test_same_platform_different_model(self):
        x=coverage([self.by['A'],self.by['C']],self.rows)
        self.assertTrue(x['model_pass']);self.assertFalse(x['platform_pass'])
    def test_crossed_pair(self): self.assertTrue(coverage([self.by['B'],self.by['C']],self.rows)['joint_pass'])
    def test_empty_candidate_set(self): self.assertFalse(coverage([self.by['A'],self.by['D']],self.rows,set())['joint_pass'])
    def test_retirement_boundary(self):
        self.assertTrue(within_announced_horizon(self.by['D'],'2026-10-19'))
        self.assertFalse(within_announced_horizon(self.by['D'],'2026-10-20'))
    def test_unknown_date_not_exact(self): self.assertTrue(within_announced_horizon(self.by['B'],'2027-01-01'))
    def test_removal_cannot_improve_coverage(self):
        for a in self.rows:
            for b in self.rows:
                if a==b:continue
                full=coverage([a,b],self.rows);less=coverage([a,b],self.rows,{a['deployment_id']})
                self.assertFalse(less['joint_pass'] and not full['joint_pass'])
    def test_complete_enumeration_and_negative_cases(self):
        rows,detail,summary=analyze(self.rows)
        self.assertEqual(len(rows),36);self.assertEqual(len(detail),36)
        self.assertEqual(summary['cases']['incumbent_candidate_benchmark']['joint_pass'],['AD','BC','CD'])
        self.assertEqual(summary['cases']['new_buyer_lifecycle_gate']['joint_pass'],['BC','CD'])
        self.assertEqual(summary['cases']['new_buyer_and_support_2026_10_21']['joint_pass'],['BC'])
        self.assertEqual(summary['cases']['announced_support_2026_10_21']['joint_pass'],['BC'])
        self.assertEqual(summary['cases']['claude_only_task_sensitivity']['joint_pass'],[])
        self.assertEqual(summary['cases']['shared_dependency_loss_sensitivity']['joint_pass'],[])
    def test_readiness_never_inferred(self):
        rows,detail,summary=analyze(self.rows)
        self.assertEqual(summary['readiness_unknown_cells'],24)
        self.assertTrue(all(x['operational_continuity']=='unverified' for x in rows))
if __name__=='__main__':unittest.main()

