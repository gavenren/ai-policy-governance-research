"""Check retained public evidence, source linkage, arithmetic, and optional private bytes."""
import argparse, csv, hashlib, io, json
from pathlib import Path
from analyze import ROOT,analyze,read_rows,READINESS
REPO=ROOT.parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument('--with-local',action='store_true');args=p.parse_args()
    sources=json.loads((ROOT/'sources/manifest.json').read_text());by={x['id']:x for x in sources}
    assert len(by)==len(sources)==13
    quotes=list(csv.DictReader((ROOT/'sources/extracts.csv').open()))
    counts={}
    for q in quotes:
        assert q['source_id'] in by
        assert q['source_sha256']==by[q['source_id']]['sha256']
        assert int(q['word_count'])==len(q['quote'].split())
        counts[q['source_id']]=counts.get(q['source_id'],0)+len(q['quote'].split())
        if args.with_local:
            text=' '.join((REPO/by[q['source_id']]['extracted_path']).read_text().split())
            assert q['quote'] in text
    assert all(x<=25 for x in counts.values())
    for row in read_rows():
        for ident in row['source_id'].split(';'):assert ident in by
        assert all(row[k]=='unknown' for k in READINESS)
    expected,detail,summary=analyze(read_rows())
    assert json.loads((ROOT/'results/summary.json').read_text())==summary
    assert json.loads((ROOT/'results/scenario-detail.json').read_text())==detail
    sio=io.StringIO(newline='');w=csv.DictWriter(sio,fieldnames=list(expected[0]));w.writeheader();w.writerows(expected)
    assert sio.getvalue().encode()==(ROOT/'results/pairs.csv').read_bytes()
    run=json.loads((ROOT/'results/run.json').read_text())
    for path,digest in run['sha256'].items():assert sha(ROOT/path)==digest,path
    for source in sources:
        if args.with_local:
            assert sha(REPO/source['original_path'])==source['sha256'],source['id']
            assert sha(REPO/source['extracted_path'])==source['extracted_sha256'],source['id']
            assert (REPO/source['original_path']).stat().st_size==source['bytes']
    if args.with_local:
        for capture in map(json.loads,(ROOT/'sources/captures.jsonl').read_text().splitlines()):
            if capture['status']=='failed':continue
            assert sha(REPO/capture['original_path'])==capture['sha256']
            assert sha(REPO/capture['extracted_path'])==capture['extracted_sha256']
        for row in json.loads((ROOT/'logs/searches.json').read_text())['events']:
            if row.get('private_response_path'):
                assert sha(REPO/row['private_response_path'])==row['private_response_sha256']
    print(json.dumps({'status':'passed','public_sources':len(sources),'extracts':len(quotes),
        'max_quoted_words_per_source':max(counts.values()),'deployments':len(read_rows()),
        'scenario_pair_rows':len(expected),'private_source_bytes_checked':args.with_local}))
if __name__=='__main__':main()

