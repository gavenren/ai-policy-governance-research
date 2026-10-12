"""Separate review calculation. Does not import the author's implementation."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import csv
import hashlib
import json
import platform

STUDY = Path(__file__).resolve().parents[1]


def proportional(d, w, b):
    d, w, b = tuple(map(Q, d)), tuple(map(Q, w)), Q(b)
    weighted = [x*y for x, y in zip(d, w)]
    total = sum(weighted)
    return tuple(b*x/total for x in weighted) if total else (Q(0),)*len(d)


def capped_by_subsets(d, w, b):
    """Enumerate saturation sets; solve the scalar equation in each segment.

    This is separate from the author's iterative removal algorithm. Multiple
    valid saturation sets at a breakpoint must give the same award vector.
    """
    d, w, b = tuple(map(Q, d)), tuple(map(Q, w)), Q(b)
    target = min(b, sum(d))
    if target == sum(d):
        return d, b-target
    possible = set()
    for saturated in product((False, True), repeat=len(d)):
        fixed = sum(x for x, flag in zip(d, saturated) if flag)
        slope = sum(x*y for x, y, flag in zip(d, w, saturated) if not flag)
        if not slope or target < fixed:
            continue
        multiplier = (target-fixed)/slope
        awards = tuple(min(x, multiplier*y*x) for x, y in zip(d, w))
        if sum(awards) != target:
            continue
        if all((a == x if flag else a == multiplier*y*x)
               for a, x, y, flag in zip(awards, d, w, saturated)):
            possible.add(awards)
    assert len(possible) == 1, (d, w, b, possible)
    awards = possible.pop()
    return awards, b-sum(awards)


def pack(v):
    return '|'.join(map(str, v))


def run():
    rows = list(csv.DictReader((STUDY/'results/grid.csv').open()))
    expected = []
    counts = Counter()
    for d in product((1, 2, 5), repeat=2):
        for initial_w in product((1, 2, 4), repeat=2):
            w = tuple(Q(x, sum(initial_w)) for x in initial_w)
            for f in map(Q, ('0', '1/4', '1/2', '3/4', '1', '5/4')):
                b = f*sum(d)
                raw = proportional(d, w, b)
                capped, unused = capped_by_subsets(d, w, b)
                within = all(a <= x for a, x in zip(raw, d))
                threshold = sum(x*y for x, y in zip(d, w))/max(w)
                assert within == (b <= threshold)
                assert sum(raw) == b
                assert sum(capped) == min(b, sum(d))
                assert all(0 <= a <= x for a, x in zip(capped, d))
                assert unused == max(Q(0), b-sum(d))
                if within:
                    assert raw == capped
                if b and all(a < x for a, x in zip(capped, d)):
                    assert (capped[0]/d[0])/(capped[1]/d[1]) == w[0]/w[1]
                surplus = b > sum(d)
                counts['rows'] += 1
                counts['raw_within_claims' if within else 'raw_exceeds_a_claim'] += 1
                counts['surplus_rows'] += surplus
                counts['shortage_or_equal_exceedances'] += not within and not surplus
                expected.append(dict(claims=pack(d), weights=pack(w),
                    budget_fraction=str(f), budget=str(b), raw_awards=pack(raw),
                    raw_within_claims=str(within), raw_sum=str(sum(raw)),
                    threshold=str(threshold), capped_awards=pack(capped),
                    unused_capacity=str(unused),
                    domain='surplus' if surplus else 'shortage_or_equal'))
    canonical = lambda r: tuple(sorted(r.items()))
    assert Counter(map(canonical, expected)) == Counter(map(canonical, rows))
    summary = json.loads((STUDY/'results/summary.json').read_text())
    assert all(summary[k] == v for k, v in counts.items())

    cases = json.loads((STUDY/'data/raw/cases.json').read_text())
    saved = json.loads((STUDY/'results/named-cases.json').read_text())
    for case in cases['allocations']:
        d, w, b = case['claims'], case['weights'], case['budget']
        raw = proportional(d, w, b)
        capped, unused = capped_by_subsets(d, w, b)
        assert saved[case['id']] == dict(raw=list(map(str, raw)),
            capped=list(map(str, capped)), capped_unused=str(unused))
    for case in cases['floors']:
        d = tuple(map(Q, case['demands']))
        u = tuple(map(Q, case['floors']))
        b = Q(case['capacity'])-sum(u)
        assert b >= 0
        residual = tuple(max(Q(0), x-y) for x, y in zip(d, u))
        for name in ('raw', 'capped'):
            z = (proportional(residual, case['weights'], b) if name == 'raw'
                 else capped_by_subsets(residual, case['weights'], b)[0])
            awards = tuple(x+y for x, y in zip(u, z))
            assert saved[case['id']][name] == [list(map(str, awards)),
                str(Q(case['capacity'])-sum(awards))]
            assert all(a >= x for a, x in zip(awards, u))
            if name == 'capped':
                assert all(a <= max(x, y) for a, x, y in zip(awards, u, d))
    d, w = (Q(2), Q(2)), (Q(2, 3), Q(1, 3))
    low, high = proportional(d, w, 1), proportional(d, w, 2)
    left = tuple(x-y for x, y in zip(d, low))
    down = proportional(high, w, 1)
    up = tuple(x+y for x, y in zip(low, proportional(left, w, 1)))
    assert low == (Q(2, 3), Q(1, 3))
    assert high == (Q(4, 3), Q(2, 3))
    assert down == (Q(4, 5), Q(1, 5))
    assert up == (Q(50, 39), Q(28, 39))
    assert all(capped_by_subsets(x, w, b)[0] == proportional(x, w, b)
               for x, b in ((d, 1), (d, 2), (high, 1), (left, 1)))
    for key, val in dict(small=low, large=high, down=down, up=up,
                         remaining_claims=left,
                         fixed_claim_sum=tuple(2*x for x in low)).items():
        assert saved['composition'][key] == list(map(str, val))
    d, w = (2, 3, 5), (Q(1, 2), Q(1, 3), Q(1, 6))
    all_awards = proportional(d, w, 4)
    sub = proportional((d[0], d[2]), (w[0], w[2]), all_awards[0]+all_awards[2])
    assert sub == (all_awards[0], all_awards[2])
    assert saved['subset_consistency']['all'] == list(map(str, all_awards))
    assert saved['subset_consistency']['reapplied'] == list(map(str, sub))
    source = tuple(map(Q, saved['source_example']['raw']))
    shock = tuple(map(Q, saved['source_shock']['raw']))
    assert source == (Q(700000), Q(3600000, 7), Q(1200000, 7),
                      Q(2700000, 7), Q(200000, 7))
    assert shock == tuple(Q(2, 3)*a for a in source)
    assert capped_by_subsets((1, 9), (9, 1), 5)[0] == (Q(1), Q(4))
    checked = ['paper.md', 'protocol.md', 'code/analyze.py',
               'code/test_analysis.py', 'data/raw/cases.json',
               'results/grid.csv', 'results/named-cases.json',
               'results/summary.json', 'reviews/independent_checks.py']
    out = dict(completed_utc=datetime.now(timezone.utc).isoformat(),
               python=platform.python_version(), network_used=False,
               author_implementation_imported=False,
               method='Exact fractions; separate enumeration of saturation sets',
               all_saved_grid_cells_match=True, counts=dict(counts),
               allocation_cases_checked=len(cases['allocations']),
               floor_cases_checked=len(cases['floors']),
               composition_and_subset_checks_pass=True,
               source_example_and_shock_pass=True,
               sha256={s: hashlib.sha256((STUDY/s).read_bytes()).hexdigest()
                       for s in checked})
    (STUDY/'reviews/independent-checks.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    run()
