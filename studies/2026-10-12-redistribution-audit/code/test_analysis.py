"""Exact examples, boundary cases and independent arithmetic checks."""
from fractions import Fraction as F
import math
import unittest

from analyze import affine, ces, consumption, covariance, measures


class AuditTests(unittest.TestCase):
    def test_population_denominator(self):
        self.assertEqual(measures([1, 3])["variance"], 1)
        self.assertEqual(measures([1, 3])["cv2"], 0.25)

    def test_equal_addition(self):
        m = measures([2, 4])
        self.assertEqual(m["variance"], 1)
        self.assertAlmostEqual(m["cv2"], float(F(1, 9)))
        self.assertAlmostEqual(m["gini"], float(F(1, 6)))

    def test_scale_control(self):
        for factor in [0.01, 2, 1000]:
            self.assertAlmostEqual(measures(affine([1, 3], factor, 0))["cv2"], 0.25)

    def test_equal_population_and_zero_scale(self):
        self.assertEqual(measures([3, 3, 3])["cv2"], 0)
        self.assertEqual(measures(affine([1, 100], 0, 2))["cv2"], 0)

    def test_undefined_and_negative_inputs_rejected(self):
        for x in [[], [0, 0], [-1, 3], [1, float("nan")]]:
            with self.assertRaises(ValueError):
                measures(x)

    def test_indexed_equal_not_proportional(self):
        equal = [F(1) + F(2, 3), F(3) + F(2, 3)]
        proportional = [F(4, 3), F(4)]
        self.assertEqual(sum(equal), sum(proportional))
        self.assertAlmostEqual(measures(equal)["cv2"], float(F(9, 64)))
        self.assertAlmostEqual(measures(proportional)["cv2"], 0.25)

    def test_balanced_common_consumption_tax(self):
        y, b, revenue, residual = consumption([1, 3], [0, 0], 1)
        self.assertEqual(y, [1.5, 2.5])
        self.assertEqual(b, 2)
        self.assertEqual(revenue, 4)
        self.assertEqual(residual, 0)
        self.assertEqual(measures(y)["cv2"], 1 / 16)

    def test_no_consumption_no_revenue(self):
        y, b, revenue, residual = consumption([1, 9], [1, 1], 100)
        self.assertEqual(y, [1, 9])
        self.assertEqual((b, revenue, residual), (0, 0, 0))

    def test_heterogeneous_saving_exact_reversal(self):
        y, b, _, residual = consumption([1, 9], [0, 1], 1)
        self.assertAlmostEqual(b, float(F(1, 3)))
        self.assertAlmostEqual(y[0], float(F(2, 3)))
        self.assertAlmostEqual(y[1], float(F(28, 3)))
        self.assertAlmostEqual(measures(y)["cv2"], float(F(169, 225)))
        self.assertGreater(measures(y)["cv2"], measures([1, 9])["cv2"])
        self.assertAlmostEqual(residual, 0)

    def test_heterogeneous_budget_direct_equations(self):
        x, saving, tax = [2, 5, 11], [0.2, 0.4, 0.8], 0.7
        y, b, revenue, residual = consumption(x, saving, tax)
        self.assertAlmostEqual(sum(x), sum(y))
        self.assertAlmostEqual(revenue, len(x) * b)
        self.assertAlmostEqual(residual, 0)
        for initial, final, s in zip(x, y, saving):
            self.assertAlmostEqual(initial + b, final + tax * (1 - s) * final)

    def test_ces_exact_counterexample(self):
        s, y, shares = ces(1, 2, 2, 0.5, 0.5, -1, 1)
        self.assertEqual(s, 2)
        self.assertAlmostEqual(y, float(F(4, 3)))
        for actual, expected in zip(shares, [F(2, 3), F(1, 6), F(1, 6)]):
            self.assertAlmostEqual(actual, float(expected))
        self.assertGreater(abs(math.log(y) - math.log(2) / 3), 0.05)

    def test_ces_equal_input_control(self):
        _, y, _ = ces(1, 1, 1, 0.5, 0.5, -1, 1)
        self.assertEqual(y, 1)

    def test_constant_ratio_labor_disappears(self):
        k = math.exp(20)
        _, _, shares = ces(k, 1, 2 * k - 1, 0.5, 0.5, -1, 1)
        self.assertAlmostEqual(shares[0], 0.5)
        self.assertLess(shares[1], 1e-8)

    def test_relative_abundance_supports_capital_limit(self):
        for ratio in [1, 10, 100, 1000]:
            _, _, shares = ces(1, 1, 2 * ratio - 1, 0.5, 0.5, -1, 1)
            self.assertAlmostEqual(shares[0], ratio / (1 + ratio))

    def test_negative_covariance_matters(self):
        x, z = [1, 3], [3, 1]
        self.assertEqual(covariance(x, z), -1)
        self.assertEqual(measures([a + b for a, b in zip(x, z)])["variance"], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
