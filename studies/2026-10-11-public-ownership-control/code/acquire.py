"""Retain separately hashed source bytes and extracted text; originals stay ignored."""
import csv, hashlib, io, json, pathlib, sys, urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
import pypdf
ROOT=pathlib.Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
LOCAL=REPO/'.local-sources/public-ownership-control'
LOCAL.mkdir(parents=True, exist_ok=True)
class Strip(HTMLParser):
 def __init__(self): super().__init__(); self.out=[]; self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'):self.skip+=1
  if tag in ('p','div','section','h1','h2','h3','h4','li','tr','br'):self.out.append('\n')
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,data):
  if not self.skip:self.out.append(data)
for item in json.loads((ROOT/'sources/acquisition.json').read_text()):
 ident=item['id']; stamp=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
 try:
  with urllib.request.urlopen(urllib.request.Request(item['url'],headers={'User-Agent':'Research source preservation; Python urllib'}), timeout=45) as r:
   data=r.read();final=r.url;media=r.headers.get_content_type()
   if len(data)<300 or b'Request Rejected' in data: raise RuntimeError('Empty or rejected response; not valid evidence')
  ext='pdf' if data.startswith(b'%PDF') else 'html'; target=LOCAL/f'{ident}.{ext}'
  if target.exists():raise RuntimeError('Capture exists; use a new source id for a new capture')
  target.write_bytes(data)
  if ext=='pdf':
   text='\n'.join(f'\n[PDF PAGE {i+1}]\n'+(p.extract_text() or '') for i,p in enumerate(pypdf.PdfReader(io.BytesIO(data)).pages));method=f'pypdf {pypdf.__version__}; page markers; no OCR'
  else:
   parser=Strip();parser.feed(data.decode('utf-8',errors='replace'));text='\n'.join(' '.join(x.split()) for x in ''.join(parser.out).splitlines() if x.strip());method='Python html.parser; omit scripts/styles; whitespace collapse; UTF-8 replacement'
  target.with_suffix('.txt').write_text(text)
  row={**item,'retrieved_utc':stamp,'final_url':final,'original_path':f'.local-sources/public-ownership-control/{target.name}','media_type':media,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'extracted_path':f'.local-sources/public-ownership-control/{ident}.txt','extracted_sha256':hashlib.sha256(text.encode()).hexdigest(),'extraction':method,'status':'captured'}
 except Exception as exc:row={**item,'retrieved_utc':stamp,'status':'failed','error':str(exc)}
 with (ROOT/'sources/captures.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 print(ident,row['status'],row.get('bytes',row.get('error')))
