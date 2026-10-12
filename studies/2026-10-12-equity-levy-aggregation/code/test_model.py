import unittest
from fractions import Fraction as F

from model import bounds, destinations, evaluate, ratio_bounds, receipts, witness


def q(*values):
    return tuple(map(F, values))


class ReceiptTests(unittest.TestCase):
    def test_same_mean_different_totals(self):
        s = q('1/4', '3/4')
        mean_a, a = evaluate([(F(1), s)], (0,), F(3))
        mean_b, b = evaluate(destinations(s), (0,), F(3))
        self.assertEqual(mean_a, mean_b)
        self.assertEqual(a, q('3/4', 0))
        self.assertEqual(b, q('1/4', 0))

    def test_empty_club(self):
        s = q('1/3', '2/3')
        self.assertEqual(receipts(s, (), F(3)), q(0, 0))
        mean, take = evaluate(witness(s, (), F(3), q(0, 0)), (), F(3))
        self.assertEqual((mean, take), (s, q(0, 0)))

    def test_zero_exposure(self):
        s = q(0, 1)
        self.assertEqual(bounds(s, (0,), F(3)), (0, 0, q(0, 0), q(0, 0)))
        self.assertEqual(evaluate(witness(s, (0,), F(3), q(0, 0)), (0,), F(3)),
                         (s, q(0, 0)))

    def test_global_membership(self):
        s = q('1/4', '3/4')
        self.assertEqual(bounds(s, (0, 1), F(3)), (1, 1, s, s))
        self.assertEqual(evaluate(destinations(s), (0, 1), F(3)), (s, s))
        self.assertEqual(evaluate(witness(s, (0, 1), F(3), s), (0, 1), F(3)), (s, s))

    def test_cap_one(self):
        s = q('1/5', '3/10', '1/2')
        self.assertEqual(bounds(s, (0, 1), F(1)),
                         (F('1/2'), F('1/2'), q('1/5', '3/10', 0), q('1/5', '3/10', 0)))
        self.assertEqual(evaluate(destinations(s), (0, 1), F(1))[1], q('1/5', '3/10', 0))

    def test_source_point_not_country_upper(self):
        s = q('.58', '.13', '.29')
        self.assertEqual(receipts(s, (0, 1), F(3)), q('58/71', '13/71', 0))
        self.assertEqual(bounds(s, (0, 1), F(3))[3], q('.87', '.39', 0))

    def test_US_endpoint_preserves_all_means(self):
        s = q('.58', '.13', '.02', '.08', '.06', '.13')
        target = q('.87', '.13', 0, 0, 0, 0)
        mean, take = evaluate(witness(s, (0, 1), F(3), target), (0, 1), F(3))
        self.assertEqual((mean, take), (s, target))

    def test_EU_endpoint_has_unused_charge(self):
        s = q('.58', '.13', '.29')
        target = q('.58', '.39', 0)
        population = witness(s, (0, 1), F(3), target)
        self.assertEqual(evaluate(population, (0, 1), F(3)), (s, target))
        self.assertEqual(sum(target), F('.97'))

    def test_incompatible_upper_endpoints_rejected(self):
        s = q('.58', '.13', '.29')
        with self.assertRaises(ValueError):
            witness(s, (0, 1), F(3), q('.87', '.39', 0))

    def test_interior_receipt_set(self):
        s = q('.2', '.2', '.6')
        target = q('.3', '.4', 0)
        self.assertEqual(evaluate(witness(s, (0, 1), F(3), target), (0, 1), F(3)),
                         (s, target))

    def test_entry_same_population(self):
        population = [(F('.4'), q('.2', '.3', '.5')),
                      (F('.6'), q('.8', '.1', '.1'))]
        before = evaluate(population, (0,), F(3))[1]
        after = evaluate(population, (0, 1), F(3))[1]
        self.assertGreaterEqual(sum(after), sum(before))
        self.assertLessEqual(after[0], before[0])
        self.assertGreater(after[1], 0)

    def test_ratio_endpoints(self):
        self.assertEqual(ratio_bounds(F('1/2'), F(1), F(3)), q('1/4', '3/4'))
        for t, expected in [(q(1, 3), F('3/4')), (q(3, 1), F('1/4'))]:
            x, revenue_weights = q(0, 1), q('1/2', '1/2')
            mean_t = sum(w * ti for w, ti in zip(revenue_weights, t))
            mean_x = sum(w * xi for w, xi in zip(revenue_weights, x))
            exy = sum(w * ti * xi for w, ti, xi in zip(revenue_weights, t, x))
            covariance = exy - mean_t * mean_x
            self.assertEqual(exy / mean_t, expected)
            self.assertEqual(mean_x + covariance / mean_t, expected)

    def test_ratio_boundary_and_invalid_values(self):
        self.assertEqual(ratio_bounds(F(0), F(1), F(3)), q(0, 0))
        self.assertEqual(ratio_bounds(F(1), F(1), F(3)), q(1, 1))
        for args in [(F('1/2'), F(0), F(3)), (F(2), F(1), F(3)),
                     (F('1/2'), F(3), F(1))]:
            with self.assertRaises(ValueError):
                ratio_bounds(*args)

    def test_invalid_profiles_and_members(self):
        for s, members, cap in [(q('.2', '.2'), (0,), F(3)),
                                 (q(-1, 2), (0,), F(3)),
                                 (q(0, 1), (0, 0), F(3)),
                                 (q(0, 1), (2,), F(3)),
                                 (q(0, 1), (0,), F('.5'))]:
            with self.assertRaises(ValueError):
                receipts(s, members, cap)

    def test_invalid_weights_and_receipts(self):
        with self.assertRaises(ValueError):
            evaluate([(F('.5'), q('.5', '.5'))], (0,), F(3))
        with self.assertRaises(ValueError):
            witness(q('.5', '.5'), (0,), F(3), q('.4', 0))
        with self.assertRaises(ValueError):
            witness(q('.5', '.5'), (0,), F(3), q('.5', '.1'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
