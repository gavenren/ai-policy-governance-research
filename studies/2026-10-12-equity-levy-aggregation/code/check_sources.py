"""Read-only checks of S015 source bytes and metadata; no model execution."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import re

STUDY = Path(__file__).resolve().parents[1]
PIN = '1573447e94b21f0da8fbaa1e9cf78823a5e2663e'


def check_file(path, expected_hash, expected_bytes=None):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_hash:
        raise ValueError('Source hash mismatch: ' + str(path))
    if expected_bytes not in (None, '') and len(raw) != int(expected_bytes):
        raise ValueError('Source byte count mismatch: ' + str(path))


def relative(root, name):
    p = Path(name)
    if p.is_absolute() or '..' in p.parts:
        raise ValueError('Expected a retained relative path: ' + name)
    return root/p


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repository', type=Path,
                        help='Also check ignored originals under this repository')
    args = parser.parse_args()
    records = json.loads((STUDY/'sources/manifest.json').read_text())
    with (STUDY/'sources/manifest.csv').open(newline='') as f:
        csv_rows = list(csv.DictReader(f))
    if csv_rows != [{k: str(v) for k, v in row.items()} for row in records]:
        raise ValueError('JSON and CSV source ledgers differ')
    required = ('id', 'title', 'author_or_issuer', 'canonical_url', 'version',
                'source_type', 'language', 'publication_date', 'acquisition_method',
                'retained_at_utc', 'retained_original_path', 'media_type', 'bytes',
                'sha256', 'claim_location', 'rights', 'coverage', 'read_scope')
    ids = [r['id'] for r in records]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate source IDs')
    public = set()
    for record in records:
        for key in required:
            if record.get(key) in (None, ''):
                raise ValueError('Missing source field: ' + record['id'] + ' ' + key)
        if record['public_path']:
            check_file(relative(STUDY, record['public_path']), record['sha256'],
                       record['bytes'])
            public.add(record['public_path'])
            if record['version'] != PIN:
                raise ValueError('Vendor revision mismatch')
    license_text = (STUDY/'sources/vendor/LICENSE').read_text()
    if 'Copyright (c) 2026 Silviu Pitis' not in license_text:
        raise ValueError('Missing upstream copyright notice')
    quotes = json.loads((STUDY/'sources/quotations.json').read_text())
    evidence = (STUDY/'sources/evidence.md').read_text()
    totals = {}
    for quote in quotes:
        n = len(quote['quote'].split())
        if n != quote['word_count'] or quote['quote'] not in evidence:
            raise ValueError('Quotation bookkeeping mismatch')
        totals[quote['source_id']] = totals.get(quote['source_id'], 0) + n
    if any(n > 25 for n in totals.values()):
        raise ValueError('Evidence quotation limit exceeded')
    local = set()
    if args.repository is not None:
        for record in records:
            check_file(relative(args.repository, record['retained_original_path']),
                       record['sha256'], record['bytes'])
            local.add(record['retained_original_path'])
            if record['extracted_path']:
                check_file(relative(args.repository, record['extracted_path']),
                           record['extracted_sha256'], record['extracted_bytes'])
                local.add(record['extracted_path'])
        acquisition = json.loads((STUDY/'logs/source-acquisition.json').read_text())
        for path_key, hash_key, bytes_key in (
                ('clone_metadata_path', 'clone_metadata_sha256', 'clone_metadata_bytes'),
                ('raw_acquisition_log_path', 'raw_acquisition_log_sha256', None)):
            check_file(relative(args.repository, acquisition[path_key]),
                       acquisition[hash_key], acquisition.get(bytes_key))
            local.add(acquisition[path_key])
        by_id = {r['id']: r for r in records}
        captured = json.loads(relative(args.repository,
                    by_id['G1']['retained_original_path']).read_text())
        if captured['sha'] != PIN:
            raise ValueError('Captured current-main revision differs from pin')
        normalize = lambda s: re.sub(r'\s+', ' ', s)
        for quote in quotes:
            record = by_id[quote['source_id']]
            original = relative(args.repository, record['extracted_path']).read_text()
            if normalize(quote['quote']) not in normalize(original):
                raise ValueError('Quotation absent from retained source')
    print(json.dumps({'source_records': len(records), 'public_vendor_files_checked':
                      len(public), 'local_byte_files_checked': len(local),
                      'json_csv_match': True, 'evidence_quotation_words': totals,
                      'local_mode': args.repository is not None,
                      'source_code_executed': False}, indent=2))


if __name__ == '__main__':
    main()
