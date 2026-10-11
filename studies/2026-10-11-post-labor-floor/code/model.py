"""Deterministic two-good endowment model. Python standard library only."""
import csv
import hashlib
import itertools
import json
import math
import platform
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def outcome(p):
    n, a, beta = p['n'], p['alpha'], p['beta']
    pi, q, g = p['pi'], p['q'], p['g']
    assert 0 < n < 1 and 0 < a < 1 and 0 < beta < 1
    assert pi > 0 and q > 0 and g >= 0
    assert all(0 <= p[k] <= 1 for k in ('s', 'tau', 'e'))
    phi = p['s'] + (1 - p['s']) * p['e'] * p['tau']
    r = phi * pi - g
    b_owner = beta * (1 - phi) * pi
    if r <= 0:
        return dict(phi=phi, revenue=r, transfer=0.0, price=None,
                    essential=0.0, reproducible=0.0, feasible=False,
                    essential_total=None, reproducible_total=None)
    d = r / n
    price = (a * r + b_owner) / ((1 - beta) * q)
    essential = a * d / price
    reproducible = (1 - a) * d
    owner_income = (1 - phi) * pi + price * q
    return dict(phi=phi, revenue=r, transfer=d, price=price,
                essential=essential, reproducible=reproducible,
                feasible=essential >= p['h'] - 1e-10 and reproducible >= p['b'] - 1e-10,
                essential_total=n * essential + beta * owner_income / price,
                reproducible_total=n * reproducible + (1 - beta) * owner_income + g)


def capture_threshold(p):
    """Necessary and sufficient capture in this model, allowing phi=1."""
    n, a, beta, pi = p['n'], p['alpha'], p['beta'], p['pi']
    delta = (1 - beta) * p['q'] - n * p['h']
    if pi <= p['g'] or delta < -1e-12:
        return math.inf
    money = (p['g'] + n * p['b'] / (1 - a)) / pi
    if abs(delta) <= 1e-12:
        access = 1.0
    else:
        access = (a * delta * p['g'] + n * p['h'] * beta * pi) / (pi * (a * delta + n * p['h'] * beta))
    return max(money, access)


def csv_write(path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def run():
    design = json.loads((ROOT / 'data/design.json').read_text())
    base = design['base']
    results = ROOT / 'results'
    results.mkdir(exist_ok=True)
    named = []
    for name, changes in design['scenarios'].items():
        p = base | changes
        named.append(dict(scenario=name, **outcome(p), required_capture=capture_threshold(p)))
    csv_write(results / 'scenarios.csv', named)
    stress = []
    for s, tau, pi, q, e in itertools.product(design['policy_grid']['s'], design['policy_grid']['tau'], design['stress_grid']['pi'], design['stress_grid']['q'], design['stress_grid']['e']):
        p = base | dict(s=s, tau=tau, pi=pi, q=q, e=e)
        stress.append(dict(s=s, tau=tau, pi=pi, q=q, e=e, **outcome(p), required_capture=capture_threshold(p)))
    csv_write(results / 'stress.csv', stress)
    policies = []
    for s, tau in itertools.product(design['policy_grid']['s'], design['policy_grid']['tau']):
        rows = [r for r in stress if r['s'] == s and r['tau'] == tau]
        policies.append(dict(s=s, tau=tau, passed=sum(r['feasible'] for r in rows), total=len(rows), minimum_essential=min(r['essential'] for r in rows), minimum_reproducible=min(r['reproducible'] for r in rows)))
    csv_write(results / 'policies.csv', policies)
    investment = []
    for eta, amount in itertools.product(design['investment']['eta'], design['investment']['values']):
        for phase in ('completed', 'construction_delay'):
            q = base['q'] + eta * amount if phase == 'completed' else base['q']
            p = base | dict(q=q, g=base['g'] + amount)
            investment.append(dict(eta=eta, investment=amount, phase=phase, **outcome(p)))
    csv_write(results / 'investment.csv', investment)
    # Reproducible tables and metadata are kept separate from the run timestamp.
    tables = ['| Scenario | Capture | Essential units | Reproducible units | Both floors met? |', '| --- | ---: | ---: | ---: | :---: |']
    for r in named:
        tables.append(f"| {r['scenario']} | {r['phi']:.3f} | {r['essential']:.3f} | {r['reproducible']:.3f} | {'Yes' if r['feasible'] else 'No'} |")
    (results / 'table.md').write_text('\n'.join(tables) + '\n')
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(results.glob('*.csv'))}
    meta = dict(run_utc=datetime.now(timezone.utc).isoformat(), python=platform.python_version(), platform=platform.system(), input_sha256=hashlib.sha256((ROOT/'data/design.json').read_bytes()).hexdigest(), code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), output_sha256=hashes, stress_rows=len(stress), note='All values are synthetic. Grid counts are not probabilities.')
    (results / 'run.json').write_text(json.dumps(meta, indent=2) + '\n')
    print('\n'.join(tables))
    print(f"Stress cases: {len(stress)}; policies: {len(policies)}")


if __name__ == '__main__':
    run()
