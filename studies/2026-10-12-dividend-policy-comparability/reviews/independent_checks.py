"""Independent review arithmetic from retained rows; no author imports."""
from pathlib import Path
from decimal import Decimal, getcontext
from collections import defaultdict
from datetime import datetime, timezone
import csv, gzip, json, hashlib, re

getcontext().prec = 40
D = Decimal
S = Path(__file__).resolve().parents[1]
TOL = D('1e-8')
BASE = D(4620)
LEVEL28 = D('5174.4')
LEVEL30 = D(5544)
COUNT = 0
MAX_ERROR = D(0)

def near(actual, expected):
    global COUNT, MAX_ERROR
    error = abs(D(str(actual))-expected)
    assert error < TOL, (actual, expected, error)
    COUNT += 1
    MAX_ERROR = max(MAX_ERROR, error)

def main():
    start = datetime.now(timezone.utc).isoformat()
    with gzip.open(S/'results/paired-paths.csv.gz', 'rt') as f:
        records = list(csv.DictReader(f))
    assert len(records) == 60000
    seen = set()
    groups = defaultdict(list)
    min_boundary_distance = None
    for raw in records:
        cohort, path, year = raw['cohort'], int(raw['path']), int(raw['year'])
        assert cohort in ('ten', 'twenty') and 1 <= path <= 2000
        assert 1 <= year <= (10 if cohort == 'ten' else 20)
        assert (cohort,path,year) not in seen
        seen.add((cohort,path,year))
        r = {k:D(v) for k,v in raw.items() if k.endswith('_billion')}
        assert all(v.is_finite() for v in r.values())
        revenue, hf, nonfloor = r['revenue_billion'], r['health_federal_billion'], r['nonfloor_billion']
        near(nonfloor, hf+D(850)*D('1.02')**year)
        # Cross multiplication in decimal arithmetic is independent of the
        # author's floating-point division implementation.
        floor = BASE
        if year >= 5:
            distance = revenue-D('0.95')*(BASE+D(850)+hf)
            min_boundary_distance = abs(distance) if min_boundary_distance is None else min(min_boundary_distance,abs(distance))
            if distance > 0:
                floor = LEVEL28
        if year >= 8:
            distance = revenue-D('0.98')*(floor+D(850)+hf)
            min_boundary_distance = min(min_boundary_distance,abs(distance))
            if distance > 0:
                floor = LEVEL30
        near(r['fixed_floor_billion'], BASE)
        near(r['trigger_floor_billion'], floor)
        near(r['source_floor_billion'], floor if cohort=='ten' else BASE)
        near(r['additional_floor_billion'], floor-BASE)
        near(r['fixed_gap_billion'], revenue-nonfloor-BASE)
        near(r['trigger_gap_billion'], revenue-nonfloor-floor)
        near(r['fixed_gap_billion']-r['trigger_gap_billion'], floor-BASE)
        assert r['fixed_gap_billion'] >= r['trigger_gap_billion']-TOL
        if year < 5:
            near(r['additional_floor_billion'], D(0))
        r.update(cohort=cohort,path=path,year=year,independent_floor=floor)
        groups[cohort,year].append(r)

    calculated = {}
    for (cohort,year), rows in groups.items():
        assert len(rows)==2000
        for policy in ('fixed','trigger'):
            floors = [BASE if policy=='fixed' else r['independent_floor'] for r in rows]
            gaps = sorted(r['revenue_billion']-r['nonfloor_billion']-f for r,f in zip(rows,floors))
            outflows = sorted(r['nonfloor_billion']+f for r,f in zip(rows,floors))
            calculated[cohort,policy,year] = {
                'paths':D(2000),
                'revenue_p50_billion':sorted(r['revenue_billion'] for r in rows)[1000],
                'outflow_p50_billion':outflows[1000],
                'gap_p10_billion':gaps[200], 'gap_p50_billion':gaps[1000],
                'gap_p90_billion':gaps[1800],
                'surplus_fraction':D(sum(g>0 for g in gaps))/2000,
                'mean_floor_billion':sum(floors)/2000,
                'base_count':D(floors.count(BASE)),
                'level28_count':D(floors.count(LEVEL28)),
                'level30_count':D(floors.count(LEVEL30)),
            }
    aggregates=list(csv.DictReader((S/'results/summary.csv').open()))
    assert len(aggregates)==60
    for row in aggregates:
        c=calculated[row['cohort'],row['policy'],int(row['year'])]
        for field,value in c.items():near(row[field],value)
    paired=list(csv.DictReader((S/'results/paired-summary.csv').open()))
    assert len(paired)==30
    for row in paired:
        rs=groups[row['cohort'],int(row['year'])]
        extra=sum(r['independent_floor']-BASE for r in rs)/2000
        crossing=sum(r['fixed_gap_billion']>0 and r['trigger_gap_billion']<=0 for r in rs)
        for field,value in {'paths':D(2000),'mean_extra_floor_billion':extra,
            'mean_gap_reduction_billion':extra,'crossing_count':D(crossing),
            'fixed_to_trigger_surplus_reduction_pp':D(crossing)/20,
            'reverse_crossing_count':D(0)}.items():near(row[field],value)

    # Baseline stdout checks provide source display precision for the two
    # revenue-component medians not retained in the paired path CSV.
    source_component_checks=0
    lines=(S/'logs/source-twenty-stdout.txt').read_text().splitlines()
    beginning=next(i for i,line in enumerate(lines) if 'Rev P50' in line)+2
    lookup={(r['cohort'],r['policy'],int(r['year'])):r for r in aggregates}
    for year,line in enumerate(lines[beginning:beginning+20],1):
        money=re.findall(r'\$\s*([+-]?\d+\.\d+)T',line)
        for field,index in [('auto_tax_p50_billion',5),('vat_p50_billion',6)]:
            actual=lookup['twenty','fixed',year][field]
            assert format(float(actual)/1000,'.2f')==money[index]
            assert actual==lookup['twenty','trigger',year][field]
            source_component_checks+=1
    ten_lines=(S/'logs/source-ten-stdout.txt').read_text().splitlines()
    beginning=next(i for i,line in enumerate(ten_lines) if 'Auto Tax P50' in line)+2
    for year,line in enumerate(ten_lines[beginning:beginning+10],1):
        money=re.findall(r'\$\s*([+-]?\d+\.\d+)T',line)
        for field,index in [('auto_tax_p50_billion',0),('vat_p50_billion',1)]:
            actual=lookup['ten','trigger',year][field]
            assert format(float(actual)/1000,'.2f')==money[index]
            assert actual==lookup['ten','fixed',year][field]
            source_component_checks+=1

    comparisons=list(csv.DictReader((S/'results/printed-checks.csv').open()))
    assert len(comparisons)==28
    target_inputs=json.loads((S/'data/printed-targets.json').read_text())
    for target,row in zip(target_inputs,comparisons):
        key=(target['cohort'],target['policy'],target['year'])
        value=calculated[key].get(target['field'])
        if value is not None:near(row['computed'],value)
        else:value=D(lookup[key][target['field']])
        rendered=format(float(value)*target['scale'],target['format'])
        assert rendered==row['rendered']
        assert (rendered==target['printed'])==(row['matches']=='True')
    failures=[r for r in comparisons if r['matches']!='True']
    assert len(failures)==1 and failures[0]['cohort']=='ten' and failures[0]['field']=='surplus_fraction'

    paper=(S/'paper.md').read_text()
    selected=[('ten',10),('twenty',10),('twenty',20)]
    table_rows=[]
    for cohort,year in selected:
        for policy in ('fixed','trigger'):
            c=calculated[cohort,policy,year]
            label='Ten-year' if cohort=='ten' else 'Twenty-year'
            policy_label='Fixed nominal floor' if policy=='fixed' else 'Original trigger rule'
            gap=format(c['gap_p50_billion']/1000,'+.3f').replace('-','−')
            line=f"| {label} cohort, year {year} | {policy_label} | {gap} | {c['surplus_fraction']*100:.2f} | {c['mean_floor_billion']/1000:.3f} |"
            assert line in paper,line
            table_rows.append(line)
    c=calculated['ten','trigger',10]
    assert [c[k] for k in ['base_count','level28_count','level30_count']]==[522,426,1052]
    near(calculated['ten','fixed',10]['gap_p10_billion'],c['gap_p10_billion'])
    by_path={(r['cohort'],r['path'],r['year']):r for rs in groups.values() for r in rs}
    same=[(path,year) for path in range(1,2001) for year in range(1,11)
          if by_path['ten',path,year]['revenue_billion']==by_path['twenty',path,year]['revenue_billion']]
    assert same==[(1,y) for y in range(1,11)]
    record={'start_utc':start,'end_utc':datetime.now(timezone.utc).isoformat(),
        'method':'Decimal cross-products and independent reducers; no author or source model import.',
        'decimal_precision':40,'tolerance_billion':str(TOL),'scalar_checks':COUNT,
        'maximum_absolute_error_billion':str(MAX_ERROR),'minimum_trigger_margin_billion':str(min_boundary_distance),
        'path_year_rows':60000,'aggregate_rows':60,'paired_rows':30,
        'independent_full_precision_summary_fields_per_row':11,
        'source_component_median_display_checks':source_component_checks,
        'printed_targets_checked':28,'printed_matches':27,'printed_failure':failures,
        'manuscript_numeric_table_rows_checked':6,'cross_cohort_equal_revenue_cells':len(same),
        'scope_limit':'Automation-tax and VAT medians checked at original stdout precision, not reconstructed at full precision from paired CSV, which omits those components.',
        'passed':True}
    (S/'reviews/independent-results.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))

if __name__=='__main__':main()
