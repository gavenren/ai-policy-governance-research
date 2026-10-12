"""Fetch pinned original sources into a new directory. Never overwrite a capture."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--destination', type=Path, required=True)
    p.add_argument('--ids', nargs='+', default=['D1', 'D2', 'D8'])
    a = p.parse_args()
    if a.destination.exists():
        raise SystemExit('Use a new destination. Existing captures are never overwritten.')
    sources = {r['source_id']: r for r in json.loads((ROOT/'sources/manifest.json').read_text())['records']}
    if any(i not in sources or sources[i]['original'] is None for i in a.ids):
        raise SystemExit('Unknown ID or no original download was retained for that ID.')
    a.destination.mkdir(parents=True)
    records = []
    for sid in a.ids:
        s = sources[sid]
        dest = a.destination/s['original']['local_file']
        at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        call = subprocess.run(['curl', '--fail', '--location', '--silent', '--show-error',
                               '--max-time', '120', s['retrieval']['requested_url'],
                               '--output', str(dest), '--write-out', '%{http_code}\n%{url_effective}'],
                              capture_output=True, text=True)
        digest = hashlib.sha256(dest.read_bytes()).hexdigest() if dest.exists() else None
        record = dict(source_id=sid, retrieved_utc=at, requested_url=s['retrieval']['requested_url'],
                      response=call.stdout.splitlines(), error=call.stderr or None,
                      exit_status=call.returncode, sha256=digest,
                      matches_retained_version=digest == s['original']['sha256'])
        records.append(record)
        (a.destination/'acquisition.json').write_text(json.dumps(records, indent=2)+'\n')
        if call.returncode or not record['matches_retained_version']:
            raise SystemExit(f'{sid}: unavailable or changed source. Preserve this capture and investigate; do not silently use it.')
        if sid in ('D1', 'D2'):
            member_name = 'SCFP2025.csv' if sid == 'D1' else 'p25_rw1.dta'
            with zipfile.ZipFile(dest) as archive:
                matches = [n for n in archive.namelist() if Path(n).name == member_name]
                if len(matches) != 1:
                    raise SystemExit('Unexpected archive member list')
                # Write only the named member, without trusting paths in the archive.
                (a.destination/member_name).write_bytes(archive.read(matches[0]))
        print(sid, 'pinned source verified')

if __name__ == '__main__':
    main()
