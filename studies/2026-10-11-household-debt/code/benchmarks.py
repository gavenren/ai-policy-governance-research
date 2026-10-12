"""Check two published public-SCF cells against the retained descriptive results."""
import argparse
import csv
import hashlib
import json
from pathlib import Path, PurePosixPath
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NS = {'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'

def cell_value(path, sheet, cell):
    with zipfile.ZipFile(path) as z:
        wb = ET.fromstring(z.read('xl/workbook.xml'))
        rels = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        rid = next(s.attrib[R] for s in wb.findall('s:sheets/s:sheet', NS) if s.attrib['name'] == sheet)
        target = next(s.attrib['Target'] for s in rels if s.attrib['Id'] == rid)
        name = target.lstrip('/') if target.startswith('/') else str(PurePosixPath('xl')/target)
        data = ET.fromstring(z.read(name))
        node = next(c for c in data.findall('.//s:c', NS) if c.attrib['r'] == cell)
        return float(node.find('s:v', NS).text)

def main():
    p=argparse.ArgumentParser();p.add_argument('--workbook', type=Path, required=True);a=p.parse_args()
    s=next(r for r in json.loads((ROOT/'sources/manifest.json').read_text())['records'] if r['source_id']=='D8')
    assert hashlib.sha256(a.workbook.read_bytes()).hexdigest()==s['original']['sha256'], 'Workbook version changed'
    desc={r['metric']:float(r['estimate']) for r in csv.DictReader((ROOT/'results/descriptive.csv').open())}
    rows=[]
    for metric,sheet,cell,tolerance,scale in [('mean_INCOME','Table 1 01-25','AI7',0.5,1000),('has_debt','Table 13 25 %s & medians','H7',0.0000005,0.01)]:
        official=cell_value(a.workbook,sheet,cell)*scale
        difference=abs(desc[metric]-official)
        rows.append(dict(metric=metric,estimate=desc[metric],official=official,tolerance=tolerance,source='D8',sheet=sheet,cell=cell,absolute_difference=difference,passed=difference<=tolerance))
    assert all(r['passed'] for r in rows), rows
    with (ROOT/'results/official-benchmarks.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print('Both published-cell benchmarks pass at their rounding precision.')

if __name__=='__main__':main()
