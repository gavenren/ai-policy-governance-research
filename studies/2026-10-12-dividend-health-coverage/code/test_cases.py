"""Focused checks of the conditional illustration, not legal-source tests."""
import json
from pathlib import Path
import unittest

from check_cases import STUDY, TREATMENTS, check, compute_rows, read_cases


# Independently hand-coded expected outcomes, in TREATMENTS order. These were
# written before running the checker and do not import any legal-source code.
EXPECTED = {
    'low-income opening': (False,True,False,True),
    'upper-ceiling crossing': (True,False,True,True),
    'prior income route': (True,True,True,True),
    'other route': (True,True,True,True),
    'insufficient added cash': (False,False,False,False),
    'requirement inapplicable': (True,True,True,True),
    'upper test already fails': (False,False,False,False),
    'exact lower boundary': (True,True,True,True),
    'exact upper boundary': (True,True,True,True),
    'above upper boundary': (False,False,False,False),
}


class CaseChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = read_cases(STUDY/'data/raw/cases.csv')
        cls.settings = json.loads((STUDY/'data/raw/settings.json').read_text())
        cls.rows = compute_rows(cls.cases, cls.settings)
        cls.by_key = {(r['case_id'],r['treatment']):r for r in cls.rows}

    def test_fixed_case_set_and_forty_outputs(self):
        self.assertEqual(set(EXPECTED),{c['case_id'] for c in self.cases})
        self.assertEqual(len(self.rows),40)
        self.assertEqual(len(self.by_key),40)

    def test_hand_coded_outcome_table(self):
        for case, expected in EXPECTED.items():
            for treatment, value in zip(TREATMENTS,expected):
                with self.subTest(case=case,treatment=treatment):
                    self.assertIs(self.by_key[case,treatment]['combined_pass'],value)

    def test_hand_arithmetic_for_opening_and_crossing(self):
        opening = self.by_key['low-income opening','proposed_split']
        self.assertEqual((opening['income_for_upper'],opening['income_for_lower']),(0,1000))
        counted = self.by_key['upper-ceiling crossing','counted_cash']
        self.assertEqual((counted['income_for_upper'],counted['income_for_lower']),(2000,2000))
        self.assertFalse(counted['upper_pass'])
        self.assertTrue(counted['lower_requirement_pass'])

    def test_shared_disregard_preserves_baseline_inputs_and_checks(self):
        fields = ('income_for_upper','income_for_lower','upper_pass','lower_income_route_pass',
                  'lower_requirement_pass','combined_pass')
        for case in EXPECTED:
            baseline = self.by_key[case,'no_payment']
            shared = self.by_key[case,'shared_disregard']
            self.assertEqual([baseline[k] for k in fields],[shared[k] for k in fields])

    def test_no_payment_equivalence_when_cash_is_zero(self):
        fields = ('cash_received','income_for_upper','income_for_lower','upper_pass',
                  'lower_income_route_pass','lower_requirement_pass','combined_pass')
        for case in self.cases:
            if case['d'] == 0:
                values = [tuple(self.by_key[case['case_id'],t][k] for k in fields) for t in TREATMENTS]
                self.assertEqual(len(set(values)),1)

    def test_inclusive_lower_and_upper_boundaries(self):
        for treatment in TREATMENTS:
            self.assertTrue(self.by_key['exact lower boundary',treatment]['lower_income_route_pass'])
            self.assertTrue(self.by_key['exact upper boundary',treatment]['upper_pass'])
            self.assertFalse(self.by_key['above upper boundary',treatment]['upper_pass'])

    def test_other_route_and_inapplicability_remove_lower_income_need(self):
        for case in ('other route','requirement inapplicable'):
            row = self.by_key[case,'shared_disregard']
            self.assertFalse(row['lower_income_route_pass'])
            self.assertTrue(row['lower_requirement_pass'])
            self.assertTrue(row['combined_pass'])
        for treatment in TREATMENTS:
            row = self.by_key['upper test already fails',treatment]
            self.assertTrue(row['lower_requirement_pass'])
            self.assertFalse(row['combined_pass'])

    def test_split_weakly_includes_shared_passes_in_fixed_cases(self):
        for case in EXPECTED:
            if self.by_key[case,'shared_disregard']['combined_pass']:
                self.assertTrue(self.by_key[case,'proposed_split']['combined_pass'])
        self.assertFalse(self.by_key['insufficient added cash','proposed_split']['combined_pass'])

    def test_negative_amounts_fail_clearly(self):
        for index in (0,1,4,5):
            values = [0,1000,True,False,1800,580,'counted_cash']
            values[index] = -1
            with self.subTest(index=index), self.assertRaisesRegex(ValueError,'nonnegative whole-dollar integer'):
                check(*values)

    def test_unknown_treatment_and_invalid_boolean_fail(self):
        with self.assertRaisesRegex(ValueError,'Unknown treatment'):
            check(0,1000,True,False,1800,580,'unknown')
        with self.assertRaisesRegex(ValueError,'must be booleans'):
            check(0,1000,1,False,1800,580,'counted_cash')


if __name__ == '__main__':
    unittest.main(verbosity=2)
