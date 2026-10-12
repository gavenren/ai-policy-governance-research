"""Retain original public source bytes and separate text. No existing capture is replaced."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from html.parser import HTMLParser
import hashlib, io, json, sys
import pypdf
ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
LOCAL = REPO / '.local-sources' / 'supplier-continuity'
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
class Visible(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'): self.skip += 1
        if tag in ('p','div','section','article','tr','li','h1','h2','h3','h4','br'): self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self,data):
        if not self.skip: self.parts.append(data)
def main():
    ident,url=sys.argv[1:]
    if not ident.replace('-','').isalnum(): raise ValueError('Invalid identifier')
    LOCAL.mkdir(parents=True,exist_ok=True)
    if any(LOCAL.glob(ident+'.*')): raise FileExistsError('Use a new version ID')
    row={'id':ident,'requested_url':url,'retrieval_started_utc':utc(),'acquisition':'Python urllib.request; User-Agent Research evidence capture'}
    try:
        with urlopen(Request(url,headers={'User-Agent':'Research evidence capture'}),timeout=45) as r:
            raw,final,media=r.read(),r.url,r.headers.get_content_type()
        row.update(retrieval_completed_utc=utc(),final_url=final,media_type=media)
        suffix='.pdf' if raw.startswith(b'%PDF') else '.html'
        path=LOCAL/(ident+suffix);path.write_bytes(raw)
        row.update(original_path=path.relative_to(REPO).as_posix(),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw))
        if suffix=='.pdf':
            reader=pypdf.PdfReader(io.BytesIO(raw))
            text='\n'.join(f'\n[PDF PAGE {i+1}]\n'+(p.extract_text() or '') for i,p in enumerate(reader.pages))
            row.update(pages=len(reader.pages),extraction=f'pypdf {pypdf.__version__}; page markers; no OCR')
        else:
            parser=Visible();parser.feed(raw.decode('utf-8',errors='replace'))
            text='\n'.join(' '.join(line.split()) for line in ''.join(parser.parts).splitlines() if line.strip())
            row.update(extraction='Python html.parser.HTMLParser; omit script/style; normalize whitespace; no rendering')
        extracted=LOCAL/(ident+'.txt');extracted.write_bytes(text.encode('utf-8'))
        row.update(extracted_path=extracted.relative_to(REPO).as_posix(),extracted_sha256=hashlib.sha256(text.encode('utf-8')).hexdigest(),extracted_bytes=len(text.encode('utf-8')),status='captured-requires-content-review')
    except Exception as e: row.update(status='failed',retrieval_completed_utc=utc(),error=str(e))
    (ROOT/'sources').mkdir(exist_ok=True)
    with (ROOT/'sources/captures.jsonl').open('a') as f: f.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(json.dumps(row,ensure_ascii=False))
if __name__=='__main__': main()

