"""Check market clearing, analytic boundaries, and policy counterexamples."""
import itertools
import json
import math
import unittest
from model import ROOT, outcome, capture_threshold

BASE = json.loads((ROOT/'data/design.json').read_text())['base']


class ModelTests(unittest.TestCase):
    def test_both_goods_clear(self):
        for pi, q, s, tau in itertools.product((50, 100, 200), (.5, 1.4, 3), (0, .3, 1), (.1, .5, 1)):
            p = BASE | dict(pi=pi, q=q, s=s, tau=tau)
            r = outcome(p)
            if r['revenue'] > 0:
                self.assertAlmostEqual(r['essential_total'], q)
                self.assertAlmostEqual(r['reproducible_total'], pi)

    def test_threshold_against_direct_market_solution(self):
        # 7,344 cases. No threshold function is used by outcome().
        for pi, q, beta, h, b in itertools.product((60, 100, 200), (.7, 1, 2, 4), (.1, .3, .6), (.3, .6), (10, 20)):
            p = BASE | dict(pi=pi, q=q, beta=beta, h=h, b=b, s=0, e=1)
            threshold = capture_threshold(p)
            for j in range(51):
                rate = j / 50
                self.assertEqual(outcome(p | dict(tau=rate))['feasible'], rate >= threshold - 1e-10)

    def test_equity_and_tax_equivalence_is_conditional(self):
        a = outcome(BASE)
        b = outcome(BASE | dict(s=0, tau=a['phi']/BASE['e']))
        self.assertAlmostEqual(a['essential'], b['essential'])
        self.assertAlmostEqual(a['reproducible'], b['reproducible'])
        # Equity acquired with debt is not a free budget gain.
        gross = outcome(BASE | dict(s=.35))
        debt = outcome(BASE | dict(s=.35, g=23))
        self.assertGreater(gross['reproducible'], a['reproducible'])
        self.assertLess(debt['reproducible'], a['reproducible'])

    def test_capacity_and_full_capture_boundaries(self):
        q_at_limit = BASE['n']*BASE['h']/(1-BASE['beta'])
        p = BASE | dict(q=q_at_limit, s=1)
        self.assertTrue(outcome(p)['feasible'])
        self.assertEqual(capture_threshold(p), 1)
        self.assertFalse(outcome(p | dict(s=.99, tau=0))['feasible'])
        self.assertTrue(math.isinf(capture_threshold(p | dict(q=q_at_limit-.01))))

    def test_investment_derivative_and_delay(self):
        r = outcome(BASE)
        B = BASE['beta']*(1-r['phi'])*BASE['pi']
        for eta in (.01, .04, .08):
            analytic = eta/BASE['q']-B/(r['revenue']*(BASE['alpha']*r['revenue']+B))
            eps = 1e-5
            changed = outcome(BASE | dict(q=BASE['q']+eta*eps, g=BASE['g']+eps))
            numerical = (math.log(changed['essential'])-math.log(r['essential']))/eps
            self.assertAlmostEqual(analytic, numerical, places=6)
        delayed = outcome(BASE | dict(g=BASE['g']+2))
        self.assertLess(delayed['essential'], r['essential'])
        self.assertLess(delayed['reproducible'], r['reproducible'])

    def test_no_spendable_surplus(self):
        r = outcome(BASE | dict(s=0, tau=0))
        self.assertFalse(r['feasible'])
        self.assertEqual(r['transfer'], 0)


if __name__ == '__main__':
    unittest.main()
