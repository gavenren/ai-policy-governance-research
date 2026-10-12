"""Reviewer checks. No author code is imported; no legal result is computed."""
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

STUDY = Path(__file__).resolve().parents[1]
TREATMENTS = ['no_payment', 'counted_cash', 'shared_disregard', 'proposed_split']
# Manually transcribed from the prospective case table, not the author tests.
# Final four digits are the independently assessed combined pass outcomes.
CASES = [
    ('low-income opening', 0, 1000, True, False, '0101'),
    ('upper-ceiling crossing', 1000, 1000, True, False, '1011'),
    ('prior income route', 600, 1000, True, False, '1111'),
    ('other route', 0, 1000, True, True, '1111'),
    ('insufficient added cash', 0, 400, True, False, '0000'),
    ('requirement inapplicable', 0, 1000, False, False, '1111'),
    ('upper test already fails', 2000, 1000, True, True, '0000'),
    ('exact lower boundary', 580, 0, True, False, '1111'),
    ('exact upper boundary', 1800, 0, True, False, '1111'),
    ('above upper boundary', 1801, 0, True, False, '0000'),
]

def main():
    start = datetime.now(timezone.utc).isoformat()
    settings = json.loads((STUDY/'data/raw/settings.json').read_text())
    assert settings['upper_ceiling'] == 1800
    assert settings['lower_threshold'] == 580 == 725*80//100
    raw = list(csv.DictReader((STUDY/'data/raw/cases.csv').open()))
    rows = list(csv.DictReader((STUDY/'results/cases.csv').open()))
    assert len(raw) == 10 and len(rows) == 40
    assert len({(r['case_id'], r['treatment']) for r in rows}) == 40
    observed = {(r['case_id'], r['treatment']): r for r in rows}
    checked = 0
    details = []
    for index, (name, y, d, applies, other, combined) in enumerate(CASES):
        assert raw[index]['case_id'] == name
        assert [int(raw[index]['y']), int(raw[index]['d'])] == [y, d]
        assert raw[index]['A'] == str(applies).lower()
        assert raw[index]['E'] == str(other).lower()
        # Parallel arrays encode each treatment directly. This does not call
        # the author function to generate a second copy of its answer.
        payments = [0, d, d, d]
        upper = [y, y+d, y, y]
        lower = [y, y+d, y, y+d]
        for j, treatment in enumerate(TREATMENTS):
            r = observed[name, treatment]
            expected = {
                'y': y, 'd': d, 'A': applies, 'E': other,
                'upper_ceiling': 1800, 'lower_threshold': 580,
                'cash_received': payments[j], 'income_for_upper': upper[j],
                'income_for_lower': lower[j], 'upper_pass': upper[j] <= 1800,
                'lower_income_route_pass': lower[j] >= 580,
                'lower_requirement_pass': not (applies and not other and lower[j] < 580),
                'combined_pass': combined[j] == '1',
            }
            for field, value in expected.items():
                assert r[field] == str(value).lower(), (name, treatment, field, r[field], value)
                checked += 1
        details.append({'case_id': name, 'combined_pass': [v == '1' for v in combined]})
    # Three rows and all twelve outcomes printed in the manuscript.
    paper = (STUDY/'paper.md').read_text()
    expected_table_rows = [
        '| $0 | Lower test fails | Both tests pass | Lower test fails | Both tests pass |',
        '| $1,000 | Both tests pass | Upper test fails | Both tests pass | Both tests pass |',
        '| $600 | Both tests pass | Both tests pass | Both tests pass | Both tests pass |',
    ]
    for row in expected_table_rows:
        assert row in paper, row
    result = {
        'start_utc': start, 'end_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Independent fixed-input and arithmetic checks; no author import; no legal eligibility inference.',
        'case_count': 10, 'row_count': 40, 'checked_output_fields': checked,
        'manuscript_case_rows_checked': 3, 'combined_results': details,
        'result_sha256': hashlib.sha256((STUDY/'results/cases.csv').read_bytes()).hexdigest(),
        'passed': True,
    }
    (STUDY/'reviews/independent-results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
