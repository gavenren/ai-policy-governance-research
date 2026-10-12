"""Offline exact enumeration and positive replication of the pinned source."""
import argparse
import csv
import hashlib
import importlib.util
import io
import json
import platform
from contextlib import redirect_stdout
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path

from model import bounds, destinations, evaluate, receipts, witness

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_csv(path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def quantities(row, **values):
    for key, value in values.items():
        row[key + '_exact_T'] = str(value)
        row[key + '_billion_USD'] = format(float(value * 1000), '.9f')
    return row


def main(output):
    started = datetime.now(timezone.utc).isoformat()
    output.mkdir(parents=True, exist_ok=True)
    inputs_path = ROOT / 'data/raw/inputs.json'
    raw = json.loads(inputs_path.read_text())
    source_path = ROOT / 'sources/vendor/figure3-club/figure3.py'
    spec = importlib.util.spec_from_file_location('source_figure3', source_path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    import numpy as np
    assert raw['destinations'] == source.BUCKETS
    assert raw['source_commit'] == '1573447e94b21f0da8fbaa1e9cf78823a5e2663e'
    rate = F(raw['rate'])
    assert float(rate) == source.TAU
    configurations, groups, countries, joins = [], [], [], []
    witnesses = {}
    checks = {'group_endpoint_populations': 0,
              'member_upper_populations': 0,
              'source_point_cells': 0, 'source_ledger_cells': 0}
    largest_difference = 0.0
    names = raw['destinations']
    n = len(names)
    for universe, data in raw['universes'].items():
        values = tuple(map(F, data['values']))
        sales = [tuple(map(F, s)) for s in data['sales']]
        original_v = source.V_MKTCAP if universe == 'broad' else source.V_TECH
        original_s = source.S_BROAD if universe == 'broad' else source.S_TECH
        assert np.allclose(list(map(float, values)), original_v, atol=1e-12, rtol=0)
        assert np.allclose([[float(x) for x in row] for row in sales],
                           original_s, atol=1e-12, rtol=0)
        for cap_int in raw['caps']:
            cap = F(cap_int)
            for mask in range(2 ** n):
                members = tuple(i for i in range(n) if mask & (1 << i))
                labels = '+'.join(names[i] for i in members) or 'empty'
                keys = {'universe': universe, 'cap': cap_int, 'mask': mask,
                        'members': labels}
                lo, hi, point = F(0), F(0), [F(0)] * n
                country_lo, country_hi = [F(0)] * n, [F(0)] * n
                source_matrix = source.collection_matrix(
                    original_v, original_s, members, float(rate), float(cap))
                source_ledger = source.bucket_ledger(
                    original_v, original_s, members, float(rate), float(cap))
                for g, (value, s) in enumerate(zip(values, sales)):
                    lower, upper, member_lower, member_upper = bounds(s, members, cap)
                    p = receipts(s, members, cap)
                    charge = rate * value
                    low_population = destinations(s)
                    high_population = [(F(1), s)]
                    for population, endpoint in [(low_population, lower),
                                                 (high_population, upper)]:
                        mean, amount = evaluate(population, members, cap)
                        assert mean == s and sum(amount) == endpoint
                        checks['group_endpoint_populations'] += 1
                    for i in members:
                        target = list(member_lower)
                        target[i] = member_upper[i]
                        population = witness(s, members, cap, target)
                        mean, amount = evaluate(population, members, cap)
                        assert mean == s and amount == tuple(target)
                        checks['member_upper_populations'] += 1
                        if universe == 'broad' and cap == 3 and mask == 3 and g == 0:
                            witnesses[names[i] + '_upper'] = {
                                'target_receipts': list(map(str, target)),
                                'firms': [{'value_weight': str(w),
                                           'sales': list(map(str, x))}
                                          for w, x in population]}
                    for i in range(n):
                        discrepancy = abs(float(charge * p[i]) - source_matrix[g, i])
                        assert discrepancy <= 1e-10
                        largest_difference = max(largest_difference, discrepancy)
                        checks['source_point_cells'] += 1
                        point[i] += charge * p[i]
                        country_lo[i] += charge * member_lower[i]
                        country_hi[i] += charge * member_upper[i]
                    discrepancy = abs(float(charge * upper) - source_ledger['collected'][g])
                    assert discrepancy <= 1e-10
                    largest_difference = max(largest_difference, discrepancy)
                    checks['source_ledger_cells'] += 1
                    groups.append(quantities(dict(keys, group=names[g]),
                                              lower=charge * lower,
                                              point=charge * sum(p), upper=charge * upper))
                    lo += charge * lower
                    hi += charge * upper
                assert lo <= sum(point) == hi <= rate * sum(values)
                configurations.append(quantities(dict(keys), lower=lo, point=sum(point),
                                                 upper=hi, full_charge=rate * sum(values)))
                for i in members:
                    assert country_lo[i] <= point[i] <= country_hi[i]
                    countries.append(quantities(dict(keys, country=names[i]),
                                                lower=country_lo[i], point=point[i],
                                                upper=country_hi[i]))
                for population_name in ('destination_only', 'homogeneous'):
                    populations = [destinations(s) if population_name == 'destination_only'
                                   else [(F(1), s)] for s in sales]
                    before = [F(0)] * n
                    for value, population in zip(values, populations):
                        _, amount = evaluate(population, members, cap)
                        before = [a + rate * value * b for a, b in zip(before, amount)]
                    for joiner in range(n):
                        if joiner in members:
                            continue
                        after = [F(0)] * n
                        for value, population in zip(values, populations):
                            _, amount = evaluate(population, members + (joiner,), cap)
                            after = [a + rate * value * b for a, b in zip(after, amount)]
                        assert sum(after) >= sum(before)
                        assert all(after[i] <= before[i] for i in members)
                        assert before[joiner] == 0 <= after[joiner]
                        joins.append(quantities(dict(keys, population=population_name,
                                                      joiner=names[joiner]),
                                                 before=sum(before), after=sum(after),
                                                 joiner_receipt=after[joiner],
                                                 incumbent_loss=sum(before[i]-after[i]
                                                                    for i in members)))
    assert (len(configurations), len(groups), len(countries), len(joins)) == (384, 2304, 1152, 2304)
    for filename, rows in [('configurations.csv', configurations), ('groups.csv', groups),
                           ('members.csv', countries), ('entry.csv', joins)]:
        write_csv(output / filename, rows)
    (output / 'witnesses.json').write_text(json.dumps({
        'interpretation': 'Different feasible populations, not simultaneous upper endpoints.',
        'universe': 'broad', 'group': 'US', 'members': ['US', 'EU'], 'cap': 3,
        'mean_sales': raw['universes']['broad']['sales'][0],
        'witnesses': witnesses}, indent=2) + '\n')
    transcript = io.StringIO()
    with redirect_stdout(transcript):
        source_ok = source.checks()
    assert source_ok
    (output / 'source-checks.txt').write_text(transcript.getvalue())
    summary = {
        'conditional_scenario_only': True,
        'row_counts': {'configurations': len(configurations), 'groups': len(groups),
                       'members': len(countries), 'entry': len(joins)},
        'checks': checks, 'max_source_difference_T': largest_difference,
        'source_internal_checks_passed': bool(source_ok),
        'selected_cap3': [r for r in configurations if r['cap'] == 3 and r['mask'] in (1,3,15,47,63)],
        'except_China_caps': [r for r in configurations if r['mask'] == 47],
        'US_EU_member_cap3': [r for r in countries if r['mask'] == 3 and r['cap'] == 3],
    }
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    runtime = {
        'started_utc': started, 'completed_utc': datetime.now(timezone.utc).isoformat(),
        'python': platform.python_version(), 'numpy': np.__version__,
        'source_commit': raw['source_commit'], 'input_sha256': digest(inputs_path),
        'code_sha256': {p.name: digest(p) for p in sorted((ROOT / 'code').glob('*.py'))
                        if p.name in ('model.py', 'analyze.py', 'test_model.py')},
        'source_code_sha256': digest(source_path),
        'output_sha256': {p.name: digest(p) for p in sorted(output.iterdir())
                          if p.is_file() and p.name != 'run.json'},
        'exit_status': 0, 'network_used_by_analysis': False,
    }
    (output / 'run.json').write_text(json.dumps(runtime, indent=2) + '\n')
    print(json.dumps({**summary['row_counts'], **checks, 'source_checks': bool(source_ok)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / 'results')
    main(parser.parse_args().output)
