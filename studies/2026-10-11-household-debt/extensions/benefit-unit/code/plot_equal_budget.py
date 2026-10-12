#!/usr/bin/env python3
"""Plot nine saved S011 estimates; do not load microdata or run a model.

Only percentage scaling and the complement of the saved family pass share are
applied. All interval endpoints come from the published outcomes file.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path
import platform

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager


BASE = Path(__file__).resolve().parents[1]
OUTCOMES_HASH = 'cbc9cca343d5d50ed82c1ba03b25eccfa37321d9b453f3c2e5cbe946b90484a2'
PAPER_HASH = 'bd37d56ca09edfc28b053265666e794af0fd2587dd46da3830b5613b01256f15'
ARMS = ('family','adult','size')
LABELS = ('Equal per family','Equal per adult','Square-root family size')
COLORS = ('#444444','#0072B2','#D55E00')
MARKERS = ('o','s','^')
METRICS = ('after_pass','person_failure','shortfall')


def hash_file(path):
    return sha256(path.read_bytes()).hexdigest()


def selected_rows():
    source = BASE/'results/outcomes.csv'
    assert hash_file(source) == OUTCOMES_HASH, 'Saved results have changed'
    paper = BASE.parents[1]/'paper.md'
    assert hash_file(paper) == PAPER_HASH, 'Published manuscript has changed'
    with source.open(newline='',encoding='utf-8') as handle:
        saved = {r['key']:r for r in csv.DictReader(handle)}
    rows = []
    for metric in METRICS:
        for arm,label in zip(ARMS,LABELS):
            key = f'exact/sqrt/{arm}/all/{metric}'
            row = saved[key]
            est,low,high,se = [Decimal(row[x]) for x in ('estimate','lower_95','upper_95','standard_error')]
            if metric == 'after_pass':
                plotted = ((1-est)*100,(1-high)*100,(1-low)*100,se*100)
                transform = '100*(1-estimate); bounds=100*(1-upper_95),100*(1-lower_95)'
                unit = 'percent of all included families'
            elif metric == 'person_failure':
                plotted = (est*100,low*100,high*100,se*100)
                transform = 'Multiply estimate, saved interval endpoints and standard error by 100'
                unit = 'percent of people in all included SCF families'
            else:
                plotted = (est,low,high,se)
                transform = 'Identity; use saved estimate and interval endpoints'
                unit = 'US dollars per month per included family; includes zero shortfalls'
            assert plotted[1] <= plotted[0] <= plotted[2]
            rows.append({'source_key':key,'arm':arm,'payment_rule':label,'source_metric':metric,
                         **{'source_'+x:row[x] for x in ('estimate','standard_error','lower_95','upper_95')},
                         'plotted_estimate':str(plotted[0]),'plotted_lower_95':str(plotted[1]),
                         'plotted_upper_95':str(plotted[2]),'plotted_standard_error':str(plotted[3]),
                         'label':f'{plotted[0]:.2f}','unit':unit,'transformation':transform})
    # Check all nine displayed values against the published Section 8 table.
    table = {}
    for line in paper.read_text(encoding='utf-8').splitlines():
        if line.startswith('| Equal per ') or line.startswith('| Proportional to square-root size |'):
            fields = [x.strip() for x in line.strip('|').split('|')]
            table[fields[0]] = fields[2:5]
    names = {'family':'Equal per family','adult':'Equal per adult','size':'Proportional to square-root size'}
    checks = []
    for row in rows:
        expected = table[names[row['arm']]][METRICS.index(row['source_metric'])]
        assert row['label'] == expected, (row,expected)
        checks.append({'key':row['source_key'],'figure_label':row['label'],'paper_table_label':expected,'matches':True})
    return rows, checks, source, paper


def build(output):
    rows, checks, source, paper = selected_rows()
    output.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':10,
                         'axes.labelsize':9.3,'xtick.labelsize':9,'ytick.labelsize':9.4,
                         'pdf.fonttype':42,'ps.fonttype':42,'svg.fonttype':'path',
                         'svg.hashsalt':'s011-equal-budget-figure-v1','axes.unicode_minus':True})
    fig,axes = plt.subplots(1,3,figsize=(7.8,4.65),sharey=True)
    fig.subplots_adjust(left=.235,right=.965,bottom=.34,top=.71,wspace=.27)
    titles = ('a  Families below\nthe floor','b  People in families\nbelow the floor','c  Mean shortfall\nacross all families')
    units = ('Percent of families','Percent of people','US$ per family per month')
    limits = ((26,35),(30,43),(440,650))
    ticks = ([26,29,32,35],[30,34,38,42],[450,550,650])
    artists = []
    for ax,metric,title,unit,xlim,xticks in zip(axes,METRICS,titles,units,limits,ticks):
        selected = [r for r in rows if r['source_metric']==metric]
        for y,row,color,marker in zip((2,1,0),selected,COLORS,MARKERS):
            est,low,high = [float(row[x]) for x in ('plotted_estimate','plotted_lower_95','plotted_upper_95')]
            ax.axhline(y,color='#E5E7EB',linewidth=.65,zorder=0)
            ax.errorbar(est,y,xerr=[[est-low],[high-est]],fmt=marker,color=color,
                        markersize=6.4,elinewidth=1.35,capsize=3,capthick=1.15,zorder=3)
            artists.append(ax.annotate(row['label'],(est,y),xytext=(0,10),textcoords='offset points',
                                       ha='center',va='bottom',fontsize=9.2,color='#1F2937'))
        ax.set_title(title,loc='left',pad=17,fontweight='bold',linespacing=1.3)
        ax.set_xlabel(unit,labelpad=8)
        ax.set_xlim(*xlim);ax.set_xticks(xticks);ax.set_ylim(-.48,2.52)
        ax.set_yticks([2,1,0]);ax.tick_params(axis='y',length=0,pad=10)
        ax.tick_params(axis='x',length=3,color='#6B7280')
        ax.spines[['top','right','left']].set_visible(False)
        ax.spines['bottom'].set_color('#6B7280');ax.spines['bottom'].set_linewidth(.65)
        ax.set_axisbelow(True)
    axes[0].set_yticklabels(LABELS)
    fig.text(.045,.958,'Equal budgets, different outcomes',fontsize=16,fontweight='bold',ha='left',va='top',color='#18232D')
    fig.text(.045,.892,'Three payment rules in the same wage-loss stress test',fontsize=10.5,ha='left',va='top',color='#495560')
    notes = [
        'Same gross budget: $2,000 × weighted family count per month. Debt payments stay fixed.',
        'Floor: $1,000 × square root of SCF family size. Primary sample: 4,358 families per implicate.',
        'Points show estimates; bars show saved normal 95% intervals. Different horizontal scales.',
        'Source: S011, Section 8; 2025 Survey of Consumer Finances. Conditional results, not a forecast.'
    ]
    for y,note in zip((.215,.17,.125,.08),notes):
        fig.text(.045,y,note,fontsize=8.3,ha='left',va='top',color='#4B5563')
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    text_boxes = []
    for text in fig.findobj(matplotlib.text.Text):
        if not text.get_visible() or not text.get_text():continue
        b = text.get_window_extent(renderer)
        assert b.x0 >= 0 and b.y0 >= 0 and b.x1 <= fig.bbox.width and b.y1 <= fig.bbox.height, text.get_text()
        text_boxes.append({'text':text.get_text(),'bounds_at_100_dpi':[b.x0,b.y0,b.x1,b.y1]})
    stem = output/'equal-budget-outcomes'
    fig.savefig(stem.with_suffix('.png'),dpi=400,facecolor='white')
    fig.savefig(stem.with_suffix('.pdf'),metadata={'Title':'S011 equal-budget outcomes','Author':'AI-assisted research draft; no human peer review','CreationDate':None,'ModDate':None},facecolor='white')
    fig.savefig(stem.with_suffix('.svg'),metadata={'Title':'S011 equal-budget outcomes','Date':None},facecolor='white')
    plt.close(fig)
    with (output/'plotted-data.csv').open('w',newline='',encoding='utf-8') as handle:
        writer=csv.DictWriter(handle,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
    font=Path(font_manager.findfont('DejaVu Sans'))
    record={'created_at_utc':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
            'source_files':{'results/outcomes.csv':hash_file(source),'../../paper.md':hash_file(paper),
                            'data/DICTIONARY.md':hash_file(BASE/'data/DICTIONARY.md')},
            'source_selection':'sample=exact; floor=sqrt; group=all; three arms; after_pass, person_failure, shortfall',
            'code_sha256':hash_file(Path(__file__)),'model_recalculated':False,
            'uncertainty':'Only saved normal 95% endpoints; complement reverses family-pass endpoints. No interval for a paired difference is inferred.',
            'number_label_checks':checks,'all_text_inside_canvas':True,'text_boxes':text_boxes,
            'font':{'name':'DejaVu Sans','sha256':hash_file(font)},
            'versions':{'python':platform.python_version(),'matplotlib':matplotlib.__version__},
            'files':{p.name:hash_file(p) for p in [stem.with_suffix(x) for x in ('.png','.pdf','.svg')]+[output/'plotted-data.csv']}}
    (output/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['created_at_utc','model_recalculated','files']},indent=2))


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=BASE/'output/figures')
    build(p.parse_args().output)
