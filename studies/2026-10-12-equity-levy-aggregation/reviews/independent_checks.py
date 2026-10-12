"""Separate review calculations. Does not import the author or vendor model.

Run from the repository root with Python 3.12+.
The source constants below were transcribed from the pinned figure3.py.
This checks arithmetic and constructions, not empirical input accuracy.
"""
import csv
import hashlib
import json
import platform
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
STUDY = HERE.parent
NAMES = ['US', 'EU', 'UK', 'JKT', 'CN', 'RoW']
RATE = Q(1, 100)
SOURCE = {
    'broad': (
        list(map(Q, ['62.19', '11.06', '4.40', '10.12', '16.31', '22.63'])),
        [list(map(Q, row.split())) for row in (
            '.58 .13 .02 .08 .06 .13', '.22 .44 .04 .06 .07 .17',
            '.28 .18 .19 .05 .06 .24', '.24 .09 .01 .40 .13 .13',
            '.04 .04 .01 .03 .85 .03', '.20 .12 .02 .08 .08 .50')]),
    'mag7': ([Q(22), *([Q(0)] * 5)],
             [list(map(Q, '.55 .17 .03 .07 .06 .12'.split()))]
             + [[Q(1, 6)] * 6 for _ in range(5)]),
}


def member_set(mask, size=6):
    return [i for i in range(size) if mask & (1 << i)]


def firm_take(x, members, cap):
    """Calculate the firm's total bill, then divide the bill among members."""
    exposure = sum(x[i] for i in members)
    if exposure == 0:
        return [Q(0)] * len(x)
    bill = cap * exposure
    if bill > 1:
        bill = Q(1)
    return [bill * x[i] / exposure if i in members else Q(0)
            for i in range(len(x))]


def integrate(population, members, cap):
    size = len(population[0][1])
    assert sum(w for w, _ in population) == 1
    mean, receipts = [Q(0)] * size, [Q(0)] * size
    for w, x in population:
        assert w >= 0 and all(z >= 0 for z in x) and sum(x) == 1
        take = firm_take(x, members, cap)
        assert 0 <= sum(take) <= 1
        for i in range(size):
            mean[i] += w * x[i]
            receipts[i] += w * take[i]
    return mean, receipts


def populations(s, mode):
    if mode == 'homogeneous':
        return [(Q(1), s)]
    assert mode == 'destination_only'
    return [(s[i], [Q(int(i == j)) for j in range(len(s))])
            for i in range(len(s)) if s[i]]


def witness_from_proof(s, members, targets):
    """Implement the proof's mixture for review, then evaluate actual firms."""
    outsiders = [i for i in range(len(s)) if i not in members]
    outside_total = sum(s[j] for j in outsiders)
    if outside_total == 0:
        return [(Q(1), s)]
    mix = []
    for i in members:
        if targets[i] == 0:
            assert s[i] == 0
            continue
        x = [Q(0)] * len(s)
        x[i] = s[i] / targets[i]
        for j in outsiders:
            x[j] = (targets[i] - s[i]) * s[j] / (targets[i] * outside_total)
        mix.append((targets[i], x))
    remaining = 1 - sum(targets)
    if remaining:
        mix.append((remaining, [s[j] / outside_total if j in outsiders else Q(0)
                                for j in range(len(s))]))
    return mix


def main():
    start = datetime.now(timezone.utc).isoformat()
    raw = json.loads((STUDY / 'data/raw/inputs.json').read_text())
    assert raw['destinations'] == NAMES and Q(raw['rate']) == RATE
    assert raw['caps'] == [2, 3, 5]
    for name, (values, sales) in SOURCE.items():
        assert values == list(map(Q, raw['universes'][name]['values']))
        assert sales == [list(map(Q, s)) for s in raw['universes'][name]['sales']]
    counts = {}
    fields_checked = 0

    def verify(row, **expected):
        nonlocal fields_checked
        for field, value in expected.items():
            assert Q(row[field + '_exact_T']) == value, (row, field, value)
            assert row[field + '_billion_USD'] == format(float(value * 1000), '.9f')
            fields_checked += 1

    selected = {}
    for filename in ['configurations', 'groups', 'members', 'entry']:
        rows = list(csv.DictReader((STUDY / 'results' / (filename + '.csv')).open()))
        counts[filename] = len(rows)
        identities = set()
        for row in rows:
            name, cap, mask = row['universe'], Q(row['cap']), int(row['mask'])
            members = member_set(mask)
            assert row['members'] == ('+'.join(NAMES[i] for i in members) or 'empty')
            values, sales = SOURCE[name]
            lows, highs, points, member_highs = [], [], [], []
            for value, s in zip(values, sales):
                charge = RATE * value
                # Two actual firm populations supply the coalition endpoints.
                _, low_take = integrate(populations(s, 'destination_only'), members, cap)
                _, high_take = integrate(populations(s, 'homogeneous'), members, cap)
                lows.append(charge * sum(low_take))
                highs.append(charge * sum(high_take))
                points.append([charge * v for v in high_take])
                # Give every other member its minimum; use only remaining capacity.
                member_highs.append([charge * min(cap * s[i],
                    1 - sum(s[j] for j in members if j != i)) if i in members else Q(0)
                    for i in range(6)])
            key = (name, str(cap), mask)
            if filename == 'configurations':
                verify(row, lower=sum(lows), point=sum(highs), upper=sum(highs),
                       full_charge=RATE * sum(values))
                if mask in [1, 3, 15, 47, 63] and cap == 3:
                    selected[name + ':' + str(mask)] = {
                        'lower_B': str(sum(lows) * 1000), 'upper_B': str(sum(highs) * 1000)}
            elif filename == 'groups':
                g = NAMES.index(row['group'])
                key += (g,)
                verify(row, lower=lows[g], point=highs[g], upper=highs[g])
            elif filename == 'members':
                i = NAMES.index(row['country'])
                assert i in members
                key += (i,)
                verify(row, lower=sum(RATE * v * s[i] for v, s in zip(values, sales)),
                       point=sum(x[i] for x in points), upper=sum(x[i] for x in member_highs))
            else:
                joiner = NAMES.index(row['joiner'])
                assert joiner not in members
                mode = row['population']
                key += (mode, joiner)
                # Construct each population once; keep it fixed across both memberships.
                fixed = [populations(s, mode) for s in sales]
                before, after = [Q(0)] * 6, [Q(0)] * 6
                for value, population in zip(values, fixed):
                    _, old = integrate(population, members, cap)
                    _, new = integrate(population, members + [joiner], cap)
                    for i in range(6):
                        before[i] += RATE * value * old[i]
                        after[i] += RATE * value * new[i]
                assert sum(after) >= sum(before)
                assert all(before[i] >= after[i] for i in members)
                verify(row, before=sum(before), after=sum(after), joiner_receipt=after[joiner],
                       incumbent_loss=sum(before[i] - after[i] for i in members))
                assert sum(after) - sum(before) == after[joiner] - sum(
                    before[i] - after[i] for i in members)
            assert key not in identities
            identities.add(key)
    assert counts == {'configurations': 384, 'groups': 2304, 'members': 1152, 'entry': 2304}

    saved = json.loads((STUDY / 'results/witnesses.json').read_text())
    saved_means = list(map(Q, saved['mean_sales']))
    for data in saved['witnesses'].values():
        pop = [(Q(f['value_weight']), list(map(Q, f['sales']))) for f in data['firms']]
        mean, take = integrate(pop, [0, 1], Q(3))
        assert mean == saved_means and take == list(map(Q, data['target_receipts']))
    assert Q('.87') + Q('.39') == Q('1.26') > 1

    # Exercise the theorem outside the author's numerical grid: zero shares,
    # no holdouts, empty clubs, cap one, a noninteger cap, and interior vectors.
    proof_checks = 0
    for s, cap, mask in product(
        [list(map(Q, x)) for x in [('0', '0', '1'), ('1', '0', '0'),
                                 ('.2', '.3', '.5'), ('.58', '.13', '.29')]],
        [Q(1), Q(3, 2), Q(3)], range(8)):
        members = member_set(mask, 3)
        lower = [s[i] if i in members else Q(0) for i in range(3)]
        targets = [lower]
        for i in members:
            target = lower[:]
            target[i] = min(cap * s[i], 1 - sum(s[j] for j in members if j != i))
            targets.extend([target, [(a + b) / 2 for a, b in zip(target, lower)]])
        for target in targets:
            mean, take = integrate(witness_from_proof(s, members, target), members, cap)
            assert mean == s and take == target
            proof_checks += 1

    necessity_checks = 0
    for a in range(11):
        for b in range(11 - a):
            x = [Q(a, 10), Q(b, 10), Q(10 - a - b, 10)]
            for cap, mask in product([Q(1), Q(3, 2), Q(3)], range(8)):
                members = member_set(mask, 3)
                take = firm_take(x, members, cap)
                assert sum(take) <= 1
                assert all(x[i] <= take[i] <= cap * x[i] for i in members)
                necessity_checks += 1

    for ratios, expected in [([Q(1), Q(3)], Q(3, 4)), ([Q(3), Q(1)], Q(1, 4))]:
        x, weights = [Q(0), Q(1)], [Q(1, 2), Q(1, 2)]
        mean_t = sum(w * t for w, t in zip(weights, ratios))
        mean_x = sum(w * y for w, y in zip(weights, x))
        mean_tx = sum(w * t * y for w, t, y in zip(weights, ratios, x))
        covariance = mean_tx - mean_t * mean_x
        direct = ratios[1] / sum(ratios)
        assert direct == mean_x + covariance / mean_t == expected
    output = {
        'started_utc': start, 'completed_utc': datetime.now(timezone.utc).isoformat(),
        'python': platform.python_version(), 'author_or_vendor_model_imported': False,
        'network_used': False, 'all_checks_passed': True,
        'csv_row_counts': counts, 'exact_and_decimal_quantity_pairs_checked': fields_checked,
        'stored_witnesses_checked': len(saved['witnesses']),
        'proof_construction_edge_and_interior_checks': proof_checks,
        'single_firm_necessity_checks': necessity_checks,
        'weighting_examples': 2, 'selected_totals': selected,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'limitations': ['Finite checks are not a proof of the theorem.',
                        'No source financial anchors or real firm population were validated.'],
    }
    (HERE / 'independent-results.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
