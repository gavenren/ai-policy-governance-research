#!/usr/bin/env python3
"""Replay two published policy rules on each unchanged source cohort."""
from pathlib import Path
import argparse,contextlib,csv,gzip,hashlib,io,json,math,platform,runpy
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[1]
FLOOR=4620.0

def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def percentile(values,p):return sorted(values)[min(int(len(values)*p),len(values)-1)]
def trigger_floor(year,revenue,health_federal):
    floor=FLOOR
    if year>=5 and revenue/(floor+850+health_federal)>.95:floor=FLOOR*1.12
    if year>=8 and revenue/(floor+850+health_federal)>.98:floor=FLOOR*1.20
    return floor

def policy_row(cohort,path,source):
    assert all(math.isfinite(v) for v in source.values() if isinstance(v,(float,int)))
    year=source['year'];revenue=source['total_revenue']
    source_floor=source['floor'] if cohort=='ten' else FLOOR
    nonfloor=source['total_outflows']-source_floor
    health_federal=nonfloor-850*(1.02**year)
    trigger=trigger_floor(year,revenue,health_federal)
    if cohort=='ten':
        assert abs(health_federal-source['healthcare']-source['federal_ops'])<1e-8
        assert abs(trigger-source_floor)<1e-8
    fixed_gap=revenue-(nonfloor+FLOOR)
    trigger_gap=revenue-(nonfloor+trigger)
    extra=trigger-FLOOR
    assert abs((fixed_gap-trigger_gap)-extra)<1e-8
    assert trigger_gap<=fixed_gap+1e-8
    assert year>=5 or extra==0
    assert abs(source['gap']-(trigger_gap if cohort=='ten' else fixed_gap))<1e-8
    row={'cohort':cohort,'path':path,'year':year,'revenue_billion':revenue,'nonfloor_billion':nonfloor,'health_federal_billion':health_federal,'source_floor_billion':source_floor,'fixed_floor_billion':FLOOR,'trigger_floor_billion':trigger,'fixed_gap_billion':fixed_gap,'trigger_gap_billion':trigger_gap,'additional_floor_billion':extra}
    assert all(math.isfinite(v) for v in row.values() if isinstance(v,(float,int)))
    return row

def write_csv(path,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)

def main(output,logs):
    output.mkdir(parents=True,exist_ok=True);logs.mkdir(parents=True,exist_ok=True)
    started=datetime.now(timezone.utc).isoformat();vendor=BASE/'vendor/four-pillars'
    ten=vendor/'monte_carlo_tax.py';twenty=vendor/'extended_monte_carlo.py'
    expected=json.loads((BASE/'data/source-hashes.json').read_text())
    for p in (ten,twenty):assert h(p)==expected[p.name]
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):runpy.run_path(str(ten),run_name='__main__')
    (logs/'source-ten-stdout.txt').write_text(buf.getvalue())
    module=runpy.run_path(str(ten),run_name='s018_source_ten')
    original_stats,short=module['run_monte_carlo']()
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf):extended=runpy.run_path(str(twenty),run_name='__main__')
    (logs/'source-twenty-stdout.txt').write_text(buf.getvalue());long=extended['all_results']
    allrows=[];summaries=[];pairs=[];source_matches=[]
    for cohort,paths,years in [('ten',short,10),('twenty',long,20)]:
        assert len(paths)==2000
        for index,path in enumerate(paths):
            assert [r['year'] for r in path]==list(range(1,years+1))
            allrows.extend(policy_row(cohort,index+1,row) for row in path)
        selected=[r for r in allrows if r['cohort']==cohort]
        for year in range(1,years+1):
            rows=[r for r in selected if r['year']==year];assert len(rows)==2000
            for policy in ['fixed','trigger']:
                gaps=[r[policy+'_gap_billion'] for r in rows];floors=[r[policy+'_floor_billion'] for r in rows]
                summary={'cohort':cohort,'policy':policy,'year':year,'paths':len(rows),'revenue_p50_billion':percentile([r['revenue_billion'] for r in rows],.5),'outflow_p50_billion':percentile([r['nonfloor_billion']+r[policy+'_floor_billion'] for r in rows],.5),'auto_tax_p50_billion':percentile([path[year-1]['auto_tax'] for path in paths],.5),'vat_p50_billion':percentile([path[year-1]['vat'] for path in paths],.5),'gap_p10_billion':percentile(gaps,.1),'gap_p50_billion':percentile(gaps,.5),'gap_p90_billion':percentile(gaps,.9),'surplus_fraction':sum(g>0 for g in gaps)/len(gaps),'mean_floor_billion':math.fsum(floors)/len(rows),'base_count':sum(f==FLOOR for f in floors),'level28_count':sum(f==FLOOR*1.12 for f in floors),'level30_count':sum(f==FLOOR*1.20 for f in floors)}
                assert summary['base_count']+summary['level28_count']+summary['level30_count']==2000
                summaries.append(summary)
                if cohort=='ten' and policy=='trigger':
                    for ours,theirs in [('gap_p10_billion','gap_p10'),('gap_p50_billion','gap_p50'),('gap_p90_billion','gap_p90'),('surplus_fraction','surplus_probability'),('revenue_p50_billion','revenue_p50'),('outflow_p50_billion','outflow_p50'),('auto_tax_p50_billion','auto_tax_p50'),('vat_p50_billion','vat_p50')]:
                        difference=abs(summary[ours]-original_stats[year-1][theirs]);assert difference<1e-8
                        source_matches.append({'year':year,'field':ours,'absolute_difference':difference})
            cross=sum(r['fixed_gap_billion']>0 and r['trigger_gap_billion']<=0 for r in rows)
            reverse=sum(r['trigger_gap_billion']>0 and r['fixed_gap_billion']<=0 for r in rows);assert reverse==0
            pairs.append({'cohort':cohort,'year':year,'paths':2000,'mean_extra_floor_billion':math.fsum(r['additional_floor_billion'] for r in rows)/2000,'mean_gap_reduction_billion':math.fsum(r['fixed_gap_billion']-r['trigger_gap_billion'] for r in rows)/2000,'fixed_to_trigger_surplus_reduction_pp':100*cross/2000,'crossing_count':cross,'reverse_crossing_count':reverse})
    assert len(allrows)==60000 and len(summaries)==60 and len(pairs)==30
    write_csv(output/'summary.csv',summaries);write_csv(output/'paired-summary.csv',pairs)
    # Deterministic gzip; all path-year records retained, not only endpoints.
    stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=list(allrows[0]),lineterminator='\n');writer.writeheader();writer.writerows(allrows)
    (output/'paired-paths.csv.gz').write_bytes(gzip.compress(stream.getvalue().encode(),mtime=0))
    same=sum(a['total_revenue']==b['total_revenue'] for aa,bb in zip(short,long) for a,b in zip(aa,bb[:10]))
    first_all=all(a['total_revenue']==b['total_revenue'] for a,b in zip(short[0],long[0][:10]))
    lookup={(x['cohort'],x['policy'],x['year']):x for x in summaries}
    target_rows=[]
    for target in json.loads((BASE/'data/printed-targets.json').read_text()):
        value=lookup[(target['cohort'],target['policy'],target['year'])][target['field']]
        rendered=format(value*target['scale'],target['format'])
        target_rows.append({**target,'computed':value,'rendered':rendered,'matches':rendered==target['printed']})
    write_csv(output/'printed-checks.csv',target_rows)
    record={'started_at_utc':started,'completed_at_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'code_sha256':h(Path(__file__)),'protocol_sha256':h(BASE/'protocol.md'),'source_hashes':expected,'source_cohort_paths':{'ten':2000,'twenty':2000},'paired_path_year_rows':60000,'policy_outcomes':120000,'summary_rows':60,'paired_summary_rows':30,'original_source_summary_matches':source_matches,'same_seed_cross_cohort_equal_revenue_cells':same,'compared_revenue_cells':20000,'first_path_first_ten_revenues_match':first_all,'printed_targets':len(target_rows),'printed_target_matches':sum(x['matches'] for x in target_rows),'outputs':{p.name:h(p) for p in output.iterdir() if p.is_file()},'source_stdout_hashes':{p.name:h(p) for p in logs.glob('source-*-stdout.txt')},'exclusions':[],'scope':'Conditional accounting comparison; no probability calibration or policy feedback.'}
    (logs/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ['original_source_summary_matches','outputs']},indent=2))
    for key in [('ten','trigger',10),('ten','fixed',10),('twenty','fixed',10),('twenty','trigger',10),('twenty','fixed',20),('twenty','trigger',20)]:print(json.dumps(lookup[key]))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=BASE/'results');p.add_argument('--logs',type=Path,default=BASE/'logs');a=p.parse_args();main(a.output,a.logs)
