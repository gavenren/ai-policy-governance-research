#!/usr/bin/env python3
"""Run the public reconstruction twice, then save checks and exact byte hashes."""
import hashlib,json,subprocess,sys
from pathlib import Path
from datetime import datetime,timezone
STUDY=Path(__file__).resolve().parents[1]
REPO=STUDY.parents[1]
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def hashes(root):return {str(p.relative_to(STUDY)):sha(p) for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts}
def run(script):
    start=now();p=subprocess.run([sys.executable,str(STUDY/'code'/script)],capture_output=True,text=True)
    return {'script':script,'started_utc':start,'completed_utc':now(),'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
def main():
    meta={'started_utc':now(),'python':sys.version,'commands':[]}
    for name in ['analyze.py','check_printed.py']:meta['commands'].append(run(name))
    first=hashes(STUDY/'results')
    for name in ['analyze.py','check_printed.py']:meta['commands'].append(run(name))
    second=hashes(STUDY/'results');meta['public_output_bytes_identical']=first==second
    meta['commands'].append(run('test_analysis.py'))
    # The test suite also regenerates the six analytical output files.
    meta['output_bytes_unchanged_after_tests']=second==hashes(STUDY/'results')
    meta['public_aggregate_verification_passed']=all(x['returncode']==0 for x in meta['commands']) and first==second and meta['output_bytes_unchanged_after_tests']
    private=[REPO/'.local-sources/ai-output-reconciliation'/n/'aggregate-export.json' for n in ['run-01','run-02']]
    meta['private_repeat_available']=all(p.exists() for p in private)
    if meta['private_repeat_available']:
        meta['private_repeat_hashes']=[sha(p) for p in private]
        meta['private_repeat_bytes_identical']=private[0].read_bytes()==private[1].read_bytes()
        assert meta['private_repeat_bytes_identical']
    meta['printed_presentation_comparison']=json.loads((STUDY/'results/printed-check-summary.json').read_text())
    meta['input_hashes']=hashes(STUDY/'data/raw');meta['output_hashes']=second
    own=['analyze.py','check_printed.py','check_private_controls.py','reproduce_private.py','test_analysis.py','verify.py']
    meta['script_hashes']={str(Path('code')/n):sha(STUDY/'code'/n) for n in own}
    meta['protocol_sha256']=sha(STUDY/'protocol.md');meta['completed_utc']=now()
    (STUDY/'logs/numerical-verification.json').write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:meta[k] for k in ['completed_utc','public_output_bytes_identical','output_bytes_unchanged_after_tests','public_aggregate_verification_passed','private_repeat_available']},indent=2))
    if not meta['public_aggregate_verification_passed']:raise SystemExit(1)
if __name__=='__main__':main()
