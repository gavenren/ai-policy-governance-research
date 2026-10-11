"""Boundary, external-formula, and small ledger checks for S007."""
from pathlib import Path
import itertools
import json
import unittest
from model import simulate, expand

class ModelTests(unittest.TestCase):
    def test_small_ledger_by_hand(self):
        rows, summary = simulate([4,4],[2,2],[2,2],[2,2],recovery=.5)
        # Two dated cohorts. Half the first cohort is served in period 1;
        # its other half is served in period 2. The new cohort then waits.
        expected = [
            dict(backlog_eligible=1,backlog_ineligible=1,appeal_net_outflow=3,
                 advance_net_outflow=5.5,extra_cash_net=1.5,extra_cash_gross=2,
                 deadline_extra_cash_net=1,deadline_extra_cash_gross=1),
            dict(backlog_eligible=2,backlog_ineligible=2,appeal_net_outflow=6,
                 advance_net_outflow=11,extra_cash_net=3,extra_cash_gross=3.5,
                 deadline_extra_cash_net=2.5,deadline_extra_cash_gross=3)]
        for row, target in zip(rows, expected):
            for key,value in target.items():
                self.assertAlmostEqual(row[key],value,msg=key)
        self.assertAlmostEqual(summary['delay_claim_periods'],3)

    def test_zero_ineligible_uses_only_earmarked_cash(self):
        rows, summary = simulate([10]*4,[5]*4,[0]*4,[0]*4)
        self.assertEqual(summary['peak_extra_cash_net'],0)
        self.assertEqual(summary['deadline_peak_extra_cash_net'],0)
        self.assertEqual(summary['terminal_eligible_arrears'],20)
        self.assertEqual(summary['delay_claim_periods'],50)
        self.assertEqual(rows[-1]['spending_gap'],20)

    def test_full_recovery_is_unresolved_ineligible_only(self):
        rows,_ = simulate([10]*5,[4]*5,[2]*5,[3]*5,recovery=1,benefit=7)
        for row in rows:
            self.assertAlmostEqual(row['extra_cash_net'],7*row['backlog_ineligible'])
            self.assertAlmostEqual(row['deadline_extra_cash_net'],7*row['backlog_ineligible'])

    def test_no_recovery_matches_all_advanced_claims(self):
        rows,_ = simulate([10]*5,[4]*5,[2]*5,[3]*5,recovery=0,benefit=7)
        for row in rows:
            self.assertEqual(row['extra_cash_net'],14*row['period'])
            self.assertAlmostEqual(row['deadline_extra_cash_net'],7*row['deadline_ineligible_advanced'])

    def test_stable_backlog_does_not_bound_cash(self):
        rows,s = simulate([100]*60,[10]*60,[2]*60,[0]+[12]*59,recovery=.5)
        for row in rows:
            self.assertAlmostEqual(row['backlog_eligible']+row['backlog_ineligible'],12)
            self.assertAlmostEqual(row['extra_cash_net'],row['period']+1)
            self.assertAlmostEqual(row['deadline_extra_cash_net'],row['period']+1)
        self.assertEqual(s['deadline_peak_extra_cash_net'],61)

    def test_fast_review_makes_deadline_rule_avoid_initial_losses(self):
        _,s = simulate([100]*12,[10]*12,[2]*12,[15]*12,recovery=.5)
        self.assertEqual(s['delay_claim_periods'],0)
        self.assertEqual(s['peak_extra_cash_net'],12)
        self.assertEqual(s['deadline_peak_extra_cash_net'],0)

    def test_unpaid_exposure_survives_final_catchup(self):
        _,s = simulate([10,0],[10,0],[0,0],[0,10])
        self.assertEqual(s['terminal_eligible_arrears'],0)
        self.assertEqual(s['delay_claim_periods'],10)

    def test_deadline_is_due_plus_d_not_total_age_at_end(self):
        _,s = simulate([10,0,0],[10,0,0],[0,0,0],[0,0,0],deadline=2)
        self.assertEqual(s['deadline_misses'],10)
        _,s2 = simulate([10,0],[10,0],[0,0],[0,0],deadline=2)
        self.assertEqual(s2['deadline_misses'],0)  # not yet observable

    def test_queue_against_scalar_lindley_recursion(self):
        # Independent scalar recurrence, with every length-3 capacity path.
        for caps in itertools.product([0,2,5],repeat=3):
            rows,_ = simulate([10]*3,[2,4,1],[1,0,2],list(caps))
            backlog = 0
            for row,e,i,c in zip(rows,[2,4,1],[1,0,2],caps):
                backlog = max(0,backlog+e+i-c)
                self.assertAlmostEqual(row['backlog_eligible']+row['backlog_ineligible'],backlog)

    def test_benefit_scaling_and_shared_review_cost(self):
        args=([10]*3,[3]*3,[2]*3,[2]*3)
        a,_=simulate(*args,benefit=1)
        b,_=simulate(*args,benefit=5,review_slot_cost=9)
        for x,y in zip(a,b):
            self.assertAlmostEqual(y['extra_cash_net'],5*x['extra_cash_net'])
            self.assertAlmostEqual(y['deadline_extra_cash_net'],5*x['deadline_extra_cash_net'])
            self.assertEqual(x['delay_claim_periods'],y['delay_claim_periods'])

    def test_all_designs_preserve_payment_dominance(self):
        design=json.loads((Path(__file__).resolve().parents[1]/'data/design.json').read_text())
        keys=list(design['grid'])
        for values in itertools.product(*(design['grid'][k] for k in keys)):
            spec=dict(zip(keys,values))
            rows,_=simulate(*expand(spec,design['horizon']),recovery=spec['recovery'])
            for row in rows:
                self.assertLessEqual(row['deadline_extra_cash_net'],row['extra_cash_net']+1e-8)
                self.assertGreaterEqual(row['extra_cash_gross']+1e-8,row['extra_cash_net'])
                self.assertGreaterEqual(row['deadline_extra_cash_gross']+1e-8,row['deadline_extra_cash_net'])

    def test_bad_inputs_rejected(self):
        for args in [([],[],[],[]),([1],[2],[0],[1]),([1],[0],[-1],[1]),([1],[0],[0],[-1])]:
            with self.assertRaises(ValueError): simulate(*args)
        with self.assertRaises(ValueError): simulate([1],[0],[0],[1],recovery=1.1)

if __name__=='__main__': unittest.main()
