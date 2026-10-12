"""Check the public evidence graph and reproduce descriptive audit outputs."""
import argparse
import csv
import hashlib
import json
import pathlib
import platform
import re
from collections import Counter
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
DIMENSIONS = {'claim', 'spending', 'voting', 'direction', 'oversight', 'challenge'}
CASES = {'AK', 'NO', 'NZ'}


def read_csv(name):
    with (ROOT / name).open(newline='') as stream:
        return list(csv.DictReader(stream))


def normal(text):
    text = re.sub(r'L\d+(?:@P\d+(?:-\d+)?)?:', ' ', text)
    return ' '.join(text.split()).casefold()


def check_graph(coding, routes, manifest, instruments, extracts):
    sources = {x['id']: x for x in manifest['sources']}
    assert len(sources) == len(manifest['sources']), 'duplicate source ID'
    ids = {x['row_id'] for x in coding}
    assert len(ids) == len(coding), 'duplicate coding ID'
    assert {(x['case'], x['dimension']) for x in coding} == {(c, d) for c in CASES for d in DIMENSIONS}, 'unbalanced coverage'
    assert len(coding) == len(CASES) * len(DIMENSIONS)
    for row in coding:
        assert all(row.values()), f'incomplete coding row {row}'
        assert set(row['source_ids'].split(';')) <= sources.keys(), 'unknown source'
        assert row['source_fact'] != row['author_interpretation'], 'fact and interpretation must be distinct'
    assert len({x['route_id'] for x in routes}) == len(routes), 'duplicate route'
    assert {(x['case'], x['decision']) for x in routes} == {(c, d) for c in CASES for d in ('payment', 'vote', 'complaint')}
    for row in routes:
        assert all(row.values()), f'incomplete route {row}'
        assert set(row['coding_rows'].split(';')) <= ids, 'broken coding reference'
        assert row['unknown_further_route'] in {'yes', 'no'}
        assert row['binding_requested_remedy'] in {'unknown', 'scope-limited eligibility review', 'scope-limited eligibility review; no guaranteed budget result'}
    assert {x['source_id'] for x in instruments} == set(sources), 'instrument coverage'
    quotes = Counter()
    for row in extracts:
        assert row['source_id'] in sources and row['locator']
        quotes[row['source_id']] += len(row['extract'].split())
    assert all(n <= 25 for n in quotes.values()), 'extract word budget'
    assert all(re.fullmatch('[a-f0-9]{64}', x['sha256']) for x in sources.values()), 'invalid hash'
    return sources


def render(coding, routes):
    table = ['# Case evidence matrix', '', 'Generated from `data/coding.csv`. These are descriptions, not scores.', '', '| Case | Dimension | Source fact | Interpretation | Evidence |', '| --- | --- | --- | --- | --- |']
    for row in coding:
        table.append('| ' + ' | '.join(row[k].replace('|', '/') for k in ('case', 'dimension', 'source_fact', 'author_interpretation', 'source_ids')) + ' |')
    route_table = ['# Decision routes and sensitivity', '', 'An additional route is assumed possible in the permissive case. This does not create evidence of a legal power.', '', '| Case and decision | Authority to reach | Documented power | Baseline further route | Permissive assumption |', '| --- | --- | --- | --- | --- |']
    for row in routes:
        route_table.append('| ' + ' | '.join([row['route_id'], row['responsible_authority'], row['documented_power'], 'unknown' if row['unknown_further_route'] == 'yes' else 'documented', 'possible additional route' if row['unknown_further_route'] == 'yes' else 'unchanged']) + ' |')
    sensitivity = {
        'type': 'logical boundary test; not an empirical or legal power estimate',
        'baseline': 'Additional unsearched remedies unknown; only documented scope stated.',
        'permissive_assumption': 'Every unknown additional challenge route may exist.',
        'affected_routes': [r['route_id'] for r in routes if r['unknown_further_route'] == 'yes'],
        'positive_separation_evidence_retained': ['AK-spending', 'AK-voting', 'AK-challenge', 'NO-spending', 'NO-voting', 'NZ-spending', 'NZ-voting', 'NZ-challenge'],
        'conclusion_withheld_under_both': 'No general conclusion that citizens lack court access or a binding remedy.',
        'limited_conclusion': 'The remedy must reach the documented authority for that decision; an additional route could supply that connection.'
    }
    return {'results/case-matrix.md': '\n'.join(table) + '\n', 'results/decision-routes.md': '\n'.join(route_table) + '\n', 'results/sensitivity.json': json.dumps(sensitivity, indent=2) + '\n'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true', help='Write generated tables and run record.')
    parser.add_argument('--with-local', action='store_true', help='Also verify ignored source bytes and exact text anchors.')
    args = parser.parse_args()
    coding, routes = read_csv('data/coding.csv'), read_csv('data/decision_routes.csv')
    instruments, extracts = read_csv('sources/instruments.csv'), read_csv('sources/extracts.csv')
    manifest = json.loads((ROOT / 'sources/manifest.json').read_text())
    sources = check_graph(coding, routes, manifest, instruments, extracts)
    local_checks = 0
    if args.with_local:
        for source in sources.values():
            body = (REPO / source['original_path']).read_bytes()
            assert len(body) == source['bytes'], source['id'] + ' byte length changed'
            assert hashlib.sha256(body).hexdigest() == source['sha256'], source['id'] + ' bytes changed'
            if source.get('extracted_path'):
                extracted = (REPO / source['extracted_path']).read_bytes()
                assert hashlib.sha256(extracted).hexdigest() == source['extracted_sha256']
            local_checks += 1
        for row in extracts:
            if row['source_id'] == 'AK12':
                continue  # Manual scan transcription, expressly not machine-verified.
            source = sources[row['source_id']]
            content = (REPO / source.get('extracted_path', source['original_path'])).read_text()
            assert normal(row['extract']) in normal(content), 'extract not found: ' + row['source_id']
        for item in manifest.get('visual_derivatives', []):
            assert hashlib.sha256((REPO / item['path']).read_bytes()).hexdigest() == item['sha256']
    for path, text in render(coding, routes).items():
        if args.write:
            (ROOT / path).write_text(text)
        else:
            assert (ROOT / path).read_text() == text, 'stale output: ' + path
    for page in ROOT.glob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', page.read_text()):
            if not target.startswith(('http:', 'https:', '#')):
                if args.write and target == 'results/run.json':
                    continue  # This run writes the record after it checks all inputs.
                assert (ROOT / target.split('#')[0]).exists(), f'broken local link {page.name}: {target}'
    inputs = ['paper.md', 'protocol.md', 'codebook.md', 'data/coding.csv', 'data/decision_routes.csv', 'sources/manifest.json', 'sources/instruments.csv', 'sources/extracts.csv', 'code/validate.py']
    record = {'run_utc': datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'), 'python': platform.python_version(), 'dependencies': 'Python standard library only', 'command': 'python3 code/validate.py' + (' --write' if args.write else '') + (' --with-local' if args.with_local else ''), 'exit_status': 0, 'source_entries': len(sources), 'coded_relations': len(coding), 'decision_routes': len(routes), 'local_representations_verified': local_checks, 'manual_transcription_not_machine_verified': ['AK12'], 'input_sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in inputs}, 'limits': ['Checks do not establish legal correctness or completeness.', 'Permissive remedy sensitivity is logical, not empirical.', 'No human or independent double coding is claimed.']}
    if args.write:
        (ROOT / 'results/run.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({k: v for k, v in record.items() if k != 'input_sha256'}, indent=2))


if __name__ == '__main__':
    main()
