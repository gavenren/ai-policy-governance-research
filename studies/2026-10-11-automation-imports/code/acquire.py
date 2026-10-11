"""Public-source capture. Does not run during offline model reproduction."""
import argparse, datetime, hashlib, html.parser, json, pathlib, subprocess
class Text(html.parser.HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'): self.skip+=1
        if tag in ('p','div','section','h1','h2','h3','h4','li'): self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self,data):
        if not self.skip: self.parts.append(data)
SOURCES=[
 ('A1','https://arxiv.org/html/2606.20649v1','html'),
 ('A2','https://link.springer.com/article/10.1007/s10797-026-09987-z','html'),
 ('A3','https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf','pdf'),
 ('A4','https://www.journals.uchicago.edu/doi/10.1086/670401','html'),
 ('A5','https://www.mohrsiebeck.com/en/article/the-taxation-of-digital-services-as-a-rent-extracting-policy-101628fa-2021-0012/','html'),
 ('A6','https://arxiv.org/html/2602.18938v1','html')]
def main():
    parser=argparse.ArgumentParser();parser.add_argument('directory',type=pathlib.Path);args=parser.parse_args()
    args.directory.mkdir(parents=True,exist_ok=True); records=[]
    for sid,url,suffix in SOURCES:
        path=args.directory/(sid+'.'+suffix)
        if path.exists(): raise SystemExit('Refuse overwrite: use a new capture directory.')
        result=subprocess.run(['curl','--location','--fail','--silent','--show-error','--max-time','50','--output',str(path),'--write-out','%{url_effective}\n%{http_code}\n%{content_type}',url],capture_output=True,text=True)
        now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        info=result.stdout.splitlines();record={'source_id':sid,'requested_url':url,'final_url':info[0] if info else None,'http_status':info[1] if len(info)>1 else None,'media_type':info[2] if len(info)>2 else None,'retrieved_utc':now,'method':'curl public HTTPS with TLS verification','exit_status':result.returncode,'error':result.stderr or None}
        if path.exists():
            data=path.read_bytes();record.update(original_local_file=path.name,original_bytes=len(data),original_sha256=hashlib.sha256(data).hexdigest())
            if suffix=='html':
                extractor=Text();extractor.feed(data.decode('utf-8','replace'))
                text='\n'.join(' '.join(line.split()) for line in ''.join(extractor.parts).splitlines() if line.strip())+'\n'
                extracted=args.directory/(sid+'.txt');extracted.write_text(text)
                record.update(extracted_local_file=extracted.name,extracted_sha256=hashlib.sha256(extracted.read_bytes()).hexdigest(),extracted_bytes=extracted.stat().st_size,extraction='Python HTMLParser; strip script/style; normalize whitespace per block; no OCR')
        records.append(record);print(sid,result.returncode,record.get('original_bytes'))
    (args.directory/'acquisition.json').write_text(json.dumps(records,indent=2)+'\n')
if __name__=='__main__': main()
