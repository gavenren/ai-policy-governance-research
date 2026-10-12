#!/usr/bin/env python3
"""Run S017's fixed illustrative cases. Standard library; no network access.

The output is not a legal eligibility or enrollment determination.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import platform


TREATMENTS = ('no_payment', 'counted_cash', 'shared_disregard', 'proposed_split')
EXPECTED_PROTOCOL = '4b753984475f33712d617925995ae3e76d8f3c5b1bdca2a9b6b0989418691566'
STUDY = Path(__file__).resolve().parents[1]


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def file_hash(path):
    return sha256(path.read_bytes()).hexdigest()


def check(y, d, applies, other_route, upper_ceiling, lower_threshold, treatment):
    """Return the two protocol tests. Currency amounts are whole dollars here."""
    for name, amount in [('y',y), ('d',d), ('upper_ceiling',upper_ceiling),
                         ('lower_threshold',lower_threshold)]:
        if type(amount) is not int or amount < 0:
            raise ValueError(f'{name} must be a nonnegative whole-dollar integer')
    if type(applies) is not bool or type(other_route) is not bool:
        raise ValueError('applies and other_route must be booleans')
    if treatment not in TREATMENTS:
        raise ValueError(f'Unknown treatment: {treatment}')
    received = 0 if treatment == 'no_payment' else d
    upper = y + d if treatment == 'counted_cash' else y
    lower = y + d if treatment in ('counted_cash', 'proposed_split') else y
    upper_pass = upper <= upper_ceiling
    lower_income_pass = lower >= lower_threshold
    lower_pass = (not applies) or other_route or lower_income_pass
    return {'cash_received': received, 'income_for_upper': upper,
            'income_for_lower': lower, 'upper_pass': upper_pass,
            'lower_income_route_pass': lower_income_pass,
            'lower_requirement_pass': lower_pass,
            'combined_pass': upper_pass and lower_pass}


def read_cases(path):
    cases = []
    with path.open(newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            for key in ('y','d'):
                row[key] = int(row[key])
            for key in ('A','E'):
                if row[key] not in ('true','false'):
                    raise ValueError(f'{key} must be true or false')
                row[key] = row[key] == 'true'
            cases.append(row)
    if len(cases) != 10 or len({r['case_id'] for r in cases}) != 10:
        raise ValueError('Require exactly ten distinct protocol cases')
    return cases


def compute_rows(cases, settings):
    rows = []
    for case in cases:
        for treatment in TREATMENTS:
            outcome = check(case['y'], case['d'], case['A'], case['E'],
                            settings['upper_ceiling'], settings['lower_threshold'], treatment)
            rows.append({**case, 'treatment': treatment,
                         'upper_ceiling': settings['upper_ceiling'],
                         'lower_threshold': settings['lower_threshold'], **outcome})
    return rows


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        for row in rows:
            writer.writerow({k: str(v).lower() if type(v) is bool else v for k,v in row.items()})


def run(output_dir, log_path):
    started = utc_now()
    inputs = [STUDY/'protocol.md', STUDY/'data/raw/cases.csv', STUDY/'data/raw/settings.json', Path(__file__)]
    if file_hash(inputs[0]) != EXPECTED_PROTOCOL:
        raise ValueError('Protocol differs from the frozen pre-execution version')
    settings = json.loads(inputs[2].read_text(encoding='utf-8'))
    if settings['protocol_sha256'] != EXPECTED_PROTOCOL:
        raise ValueError('Settings name a different protocol')
    cases = read_cases(inputs[1])
    rows = compute_rows(cases, settings)
    if len(rows) != 40 or len({(r['case_id'],r['treatment']) for r in rows}) != 40:
        raise ValueError('Require exactly ten cases times four treatments')
    output = output_dir/'cases.csv'
    write_csv(output, rows)
    record = {'started_at_utc':started, 'completed_at_utc':utc_now(), 'exit_status':0,
              'python_version':platform.python_version(), 'dependencies':'Python standard library only',
              'case_count':len(cases), 'treatments':list(TREATMENTS), 'output_count':len(rows),
              'input_hashes':{str(p.relative_to(STUDY)):file_hash(p) for p in inputs},
              'output':{'filename':'cases.csv','sha256':file_hash(output),'bytes':output.stat().st_size},
              'interpretation':'Fixed illustrative arithmetic cases. No prevalence, legal eligibility, enrollment or welfare inference.',
              'diagnostics':[]}
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(json.dumps(record,indent=2)+'\n', encoding='utf-8')
    return record


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=STUDY/'results')
    parser.add_argument('--log', type=Path, default=STUDY/'logs/execution.json')
    args = parser.parse_args()
    print(json.dumps(run(args.output_dir,args.log),indent=2))
