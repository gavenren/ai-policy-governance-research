#!/usr/bin/env python3
"""Run an acquired source archive privately; export only aggregate accounting inputs.

This adapter contains no third-party implementation. The AST edit happens in
memory to the user's local copy and is recorded; files in that copy are unchanged.
"""
import argparse, ast, contextlib, csv, hashlib, importlib.metadata, json, os
from pathlib import Path
import runpy, sys, traceback, zipfile
from datetime import datetime, timezone

ZIP_HASH = '85bf1b23a99f606abf3ab87b39ed9d3bc69a6d53a27d50ee31ff20d1f974ff8c'
PROTOCOL_HASH = 'f0d6c33785243a6220af8c9f4ee998b31a6a4eb7964006dc1d1f5c4ebdd6ce60'
STUDY = Path(__file__).resolve().parents[1]
REPO = STUDY.parents[1]
def utc(): return datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True, allow_nan=False)+'\n')
def csv_save(p, rows):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def native(x):
    if isinstance(x,dict): return {str(k):native(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [native(v) for v in x]
    return x.item() if hasattr(x,'item') else x

def run(run_id, export):
    archive=REPO/'.local-sources/next-design-screen/original-replication.zip'
    assert sha(archive)==ZIP_HASH, 'Source archive has changed'
    assert sha(STUDY/'protocol.md')==PROTOCOL_HASH, 'Reviewed protocol snapshot has changed'
    private=REPO/'.local-sources/ai-output-reconciliation'/run_id
    private.mkdir(parents=True,exist_ok=False)
    meta={'run_id':run_id,'setup_started_utc':utc(),'archive_sha256':sha(archive),
          'protocol_sha256':sha(STUDY/'protocol.md'),'adapter_sha256':sha(__file__),
          'python':sys.version,'packages':{d.metadata['Name']:d.version for d in importlib.metadata.distributions()},
          'network_attempts':[], 'status':'started'}
    log=STUDY/'logs'/f'execution-{run_id}.json'
    save(log,meta)
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            path=Path(info.filename)
            assert not path.is_absolute() and '..' not in path.parts
            if info.filename.startswith('replication/'):
                z.extract(info,private)
    source=private/'replication'
    immutable={str(p.relative_to(source)):sha(p) for p in source.rglob('*')
               if p.is_file() and ('results' not in p.relative_to(source).parts)
               and '__pycache__' not in p.parts}
    meta['unchanged_members_before']=immutable
    meta['shipped_output_hashes']={str(p.relative_to(source)):sha(p) for p in (source/'results').glob('*') if p.is_file()}
    os.environ['MPLBACKEND']='Agg';os.environ['MPLCONFIGDIR']=str(private/'mpl-cache')
    sys.dont_write_bytecode=True
    def network_guard(event,args):
        if event=='socket.connect':
            meta['network_attempts'].append(repr(args));raise RuntimeError('Offline source run forbids network access')
    sys.addaudithook(network_guard)
    sys.path.insert(0,str(source));os.chdir(source)
    try:
        meta['first_source_execution_utc']=utc();save(log,meta)
        with (private/'source-run.log').open('w') as f, contextlib.redirect_stdout(f),contextlib.redirect_stderr(f):
            namespace=runpy.run_path(str(source/'main.py'),run_name='__main__')
        state=namespace['results']; calc=sys.modules['calculations']; res=sys.modules['results']; cfg=sys.modules['config']
        meta['full_main_completed_utc']=utc()
        # Only baseline whole-US outputs belong to main.py. They remain private.
        state['total_gdp_df'].to_csv(private/'baseline-whole-us-private.csv',index=False)
        state['gdp_df'].to_csv(private/'baseline-ai-private.csv',index=False)
        listed=[float(x) for x in namespace['ANNUAL_POWER_TOTALS']]
        years=[2023,2024,2025]; monthly=state['power_monthly']; annual=[]; monthly_rows=[]; cases={}; control={}
        params={name:native(getattr(cfg,name)) for name in ['POWER_PRICES','INFERENCE_SHARE','AI_SERVICES_MARKUP','AI_SERVICES_LABOR_SHARE','INFERENCE_DEFLATOR_RATIO','TRAINING_DEFLATOR_RATIO','H100_OPs_per_year']}
        params['listed_power_Wh']=listed;params['years']=years
        # Change one global-name expression inside the original local GDP function.
        tree=ast.parse((source/'results.py').read_text())
        function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='calculate_ai_gdp')
        class Bridge(ast.NodeTransformer):
            count=0
            def visit_Name(self,node):
                if node.id=='TRAINING_DEFLATOR_RATIO':
                    self.count+=1
                    return ast.copy_location(ast.Subscript(value=ast.Name(id='bridge_prices',ctx=ast.Load()),slice=ast.Name(id='i',ctx=ast.Load()),ctx=ast.Load()),node)
                return node
        edit=Bridge();function=edit.visit(function);assert edit.count==1
        module=ast.fix_missing_locations(ast.Module(body=[function],type_ignores=[]))
        bridge_ns=dict(vars(res));exec(compile(module,'<documented-training-price-adapter>','exec'),bridge_ns)
        meta['source_adapter']={'training_price_name_replacements':edit.count,'scope':'calculate_ai_gdp only; transition-specific bridge_prices[i]; AST in memory; no source-file edit',
                                'power_rule':'multiply every source monthly value in a year by listed annual Wh / generated annual Wh',
                                'full_main':'unchanged source via runpy; Agg plotting; socket.connect audit guard; cached input files',
                                'alternative_scope':'AI island only; no whole-US alternative'}
        for rule in ['released','annual_preserving']:
            selected=monthly.copy()
            for i,y in enumerate(years):
                generated=float(monthly.loc[str(y)].sum())
                if rule=='annual_preserving': selected.loc[str(y)]*=listed[i]/generated
            details={}; series={}
            for label,column in [('spending','revenue_per_Wh'),('ops','OP_per_Wh'),('labor','labor_cost_per_Wh')]:
                detail=calc.calculate_monthly_spending_detailed(selected,state['final_df'],share_col='IT_power_adjusted',price_col=column)
                details[label]=detail
                series[label]=calc.aggregate_spending_by_month(detail)
            if rule=='released':
                for label,key in [('spending','compute_spending'),('ops','compute_ops'),('labor','labor_spending')]:
                    assert series[label].equals(state[key]), label+' baseline mismatch'
                released_details=details
            else:
                import numpy as np
                for label,d in details.items():
                    base=released_details[label]
                    assert d[['date','entity']].equals(base[['date','entity']])
                    assert np.array_equal(d['proportion'],base['proportion'])
                    expected=base['date'].dt.year.map({y:listed[i]/float(monthly.loc[str(y)].sum()) for i,y in enumerate(years)})
                    assert np.allclose(d['power_allocated'],base['power_allocated']*expected,rtol=2e-14,atol=0)
                    assert np.allclose(d['spending'],base['spending']*expected,rtol=2e-14,atol=0,equal_nan=True)
                control['row_allocation_and_composition_preserved']=True
            for date,value in selected.items():
                monthly_rows.append({'power_rule':rule,'month':date.strftime('%Y-%m'),'power_Wh':float(value)})
            spending={f'spending_{y}':float(series['spending'].loc[str(y)].sum()) for y in years}
            labor={f'labor_{y}':float(series['labor'].loc[str(y)].sum()) for y in years}
            ops={y:float(series['ops'].loc[str(y)].sum()) for y in years}
            bridges=[None]+[float(cfg.TRAINING_DEFLATOR_RATIO)*(spending[f'spending_{y}']/spending[f'spending_{y-1}'])/(ops[y]/ops[y-1]) for y in years[1:]]
            bridge_ns['bridge_prices']=bridges
            for price_rule,fn in [('released',res.calculate_ai_gdp),('operations_bridge',bridge_ns['calculate_ai_gdp'])]:
                key=rule+'__'+price_rule
                df=fn(spending,labor,listed)
                cases[key]=native(df.to_dict(orient='records'))
            for i,y in enumerate(years):
                generated=float(monthly.loc[str(y)].sum())
                annual.append({'power_rule':rule,'year':y,'compute_spending_usd':spending[f'spending_{y}'],'physical_bit_ops':ops[y],
                    'data_center_labor_usd':labor[f'labor_{y}'],'listed_power_Wh':listed[i],'released_generated_power_Wh':generated,
                    'selected_power_Wh':float(selected.loc[str(y)].sum()),'electricity_price_usd_per_kWh':float(cfg.POWER_PRICES[i]),
                    'charged_listed_power_cost_usd':listed[i]/1000*float(cfg.POWER_PRICES[i]),
                    'released_generated_power_cost_usd':generated/1000*float(cfg.POWER_PRICES[i])})
        output={'parameters':params,'annual_inputs':annual,'monthly_power':monthly_rows,'source_case_outputs':cases,
                'baseline_qa':native(state['qa_results']),'baseline_spending':native(state['spending_results']),
                'baseline_compute':native(state['compute_results']),'baseline_indices':native(state['indices_df'].to_dict(orient='records')),
                'source_checks':control}
        save(private/'aggregate-export.json',output)
        if export:
            raw=STUDY/'data/raw'
            save(raw/'parameters.json',params);csv_save(raw/'annual-inputs.csv',annual);csv_save(raw/'monthly-power.csv',monthly_rows)
            save(raw/'source-case-outputs.json',cases)
            save(raw/'source-control.json',{k:output[k] for k in ['baseline_qa','baseline_spending','baseline_compute','baseline_indices','source_checks']})
        after={n:sha(source/n) for n in immutable}
        assert after==immutable,'A source/input file changed'
        meta['unchanged_members_after']=after
        meta['private_output_hashes']={str(p.relative_to(private)):sha(p) for p in private.rglob('*') if p.is_file() and (p.parent==private or p.parent==source/'results')}
        text=(private/'source-run.log').read_text()
        meta['warnings']=[line for line in text.splitlines() if 'Warning' in line or 'Expected' in line]
        meta['aggregate_export_sha256']=sha(private/'aggregate-export.json');meta['status']='passed';meta['completed_utc']=utc()
    except BaseException:
        meta['status']='failed';meta['failure']=traceback.format_exc();meta['completed_utc']=utc();save(log,meta);raise
    save(log,meta)
    print(json.dumps({'status':meta['status'],'run_id':run_id,'aggregate_export_sha256':meta['aggregate_export_sha256'],'warnings':meta['warnings']},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--run-id',required=True);parser.add_argument('--export',action='store_true')
    args=parser.parse_args();run(args.run_id,args.export)
