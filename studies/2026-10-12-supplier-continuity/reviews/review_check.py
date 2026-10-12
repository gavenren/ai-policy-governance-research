"""Independent S013 enumeration and optional current-source check.

This does not import the author's enumeration or change the core study files.
"""
import argparse
import csv
import datetime
import hashlib
import itertools
import json
import platform
import urllib.request
from pathlib import Path
from html.parser import HTMLParser

STUDY = Path(__file__).resolve().parents[1]
REPO = STUDY.parents[1]

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(self.skip - 1, 0)
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--network', action='store_true')
    args = parser.parse_args()
    # The reviewer checked these labels against D1-D4 after reading the paper.
    # This is a separate source check, not a blind coding exercise.
    model = {'A': 'Claude Sonnet 4.5', 'B': 'Claude Sonnet 4.5', 'C': 'Nova Pro', 'D': 'Gemini 2.5 Pro'}
    cloud = {'A': 'Amazon Bedrock', 'B': 'Google Cloud', 'C': 'Amazon Bedrock', 'D': 'Google Cloud'}
    eligible = {
        'incumbent_candidate_benchmark': set('ABCD'),
        'new_buyer_lifecycle_gate': set('BCD'),
        'announced_support_2026_10_21': set('ABC'),
        'new_buyer_and_support_2026_10_21': set('BC'),
        'claude_only_task_sensitivity': set('AB'),
        'shared_dependency_loss_sensitivity': set(),
    }
    with (STUDY / 'results/pairs.csv').open(newline='') as stream:
        rows = list(csv.DictReader(stream))
    keyed = {(r['case'], r['pair']): r for r in rows}
    assert len(keyed) == len(rows) == 36
    checks = []
    for name, allowed in eligible.items():
        for pair_tuple in itertools.combinations('ABCD', 2):
            pair = ''.join(pair_tuple)
            row = keyed[name, pair]
            pool = set(pair) & allowed
            # Directly remove each named dependency and test the remaining set.
            per_model = [bool({x for x in pool if model[x] != shock}) for shock in set(model.values())]
            per_cloud = [bool({x for x in pool if cloud[x] != shock}) for shock in set(cloud.values())]
            expected = {'model_pass': all(per_model), 'platform_pass': all(per_cloud),
                        'joint_pass': all(per_model + per_cloud)}
            for field, value in expected.items():
                assert (row[field] == 'True') == value, (name, pair, field)
            assert row['remaining_candidates'] == ','.join(sorted(pool))
            assert row['operational_continuity'] == 'unverified'
            checks.append({'case': name, 'pair': pair, **expected})
    # Positive and negative conditions are checked without the author's tests.
    assert keyed['incumbent_candidate_benchmark', 'AB']['platform_pass'] == 'True'
    assert keyed['incumbent_candidate_benchmark', 'AB']['model_pass'] == 'False'
    assert keyed['incumbent_candidate_benchmark', 'AC']['model_pass'] == 'True'
    assert keyed['incumbent_candidate_benchmark', 'AC']['platform_pass'] == 'False'
    assert not any(x['joint_pass'] for x in checks if 'sensitivity' in x['case'])
    sources = json.loads((STUDY / 'sources/manifest.json').read_text())
    local_checks = []
    for source in sources:
        for path_key, hash_key in [('original_path', 'sha256'), ('extracted_path', 'extracted_sha256')]:
            path = REPO / source[path_key]
            if path.exists():
                assert hashlib.sha256(path.read_bytes()).hexdigest() == source[hash_key]
                local_checks.append(source[path_key])
    network = []
    if args.network:
        for sid in ('D1', 'D6', 'D4'):
            source = next(x for x in sources if x['id'] == sid)
            record = {'source_id': sid, 'requested_url': source['requested_url'], 'started_utc': now()}
            try:
                req = urllib.request.Request(source['requested_url'], headers={'User-Agent': 'Research evidence check'})
                with urllib.request.urlopen(req, timeout=45) as response:
                    raw = response.read()
                    record['final_url'] = response.url
                record.update(completed_utc=now(), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
                record['same_original_bytes_as_author_capture'] = record['sha256'] == source['sha256']
                html = Text(); html.feed(raw.decode('utf-8', errors='replace'))
                visible = ' '.join(' '.join(html.parts).split())
                saved = Text(); saved.feed((REPO / source['original_path']).read_text(errors='replace'))
                saved_visible = ' '.join(' '.join(saved.parts).split())
                record['normalized_visible_text_same_as_saved'] = visible == saved_visible
                record['normalized_visible_text_sha256'] = hashlib.sha256(visible.encode()).hexdigest()
                if sid == 'D1':
                    tests = ['Model lifecycle: Legacy', 'April 8, 2027']
                elif sid == 'D6':
                    tests = ["New customers can't use Legacy models", 'Claude Sonnet 4.5', 'October 8, 2026', 'April 8, 2027', 'us-east-1']
                else:
                    tests = ['October 20, 2026', 'retirement of support in Gemini Enterprise Agent Platform']
                record['critical_texts_present'] = all(x in visible for x in tests)
                assert record['critical_texts_present'], record
                record['status'] = 'passed'
            except Exception as exc:
                record.update(completed_utc=now(), status='failed', error=str(exc))
            network.append(record)
    report = {'run_utc': now(), 'python': platform.python_version(),
              'scope': 'Independent enumeration and local source hashes; optional read-only public source requests.',
              'enumeration_rows_checked': len(checks), 'independent_enumeration': checks,
              'retained_source_files_hash_checked': len(local_checks), 'network': network,
              'numerical_status': 'passed',
              'limits': 'No account access, API inference, capacity trial, contract review, or population inference.'}
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
