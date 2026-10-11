"""Optional public source capture. Originals remain ignored and unpublished."""
import hashlib,json,pathlib,subprocess,datetime
ROOT=pathlib.Path(__file__).resolve().parents[3]
DEST=ROOT/'.local-sources'/'dividend-reserves'
URLS={
'S1':('https://www.imf.org/-/media/files/publications/howtonotes/2020/english/htnea2020004.pdf','pdf'),
'S2':('https://www.imf.org/-/media/files/publications/howtonotes/2020/english/htnea2020003.pdf','pdf'),
'S3':('https://apfc.org/wp-content/uploads/2025/12/2024-APFC-Trustees-Paper-10.pdf','pdf'),
'S4':('https://apfc.org/the-fund/fund-structure/','html'),
'S5':('https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf','pdf'),
'S6':('https://www.nber.org/system/files/working_papers/w35437/w35437.pdf','pdf'),
'S7':('https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7323361','html'),
'S7z':('https://zenodo.org/api/records/22036502','json'),
'S7-package':('https://zenodo.org/api/records/22036502/files/AI_SWF_replication_package.zip/content','zip'),
}
def main():
 DEST.mkdir(parents=True,exist_ok=True)
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 out=[]
 for sid,(url,ext) in URLS.items():
  p=DEST/(sid+'-'+stamp+'.'+ext)
  at=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
  r=subprocess.run(['curl','-L','--max-time','40','-sS','-w','%{http_code}\n%{url_effective}\n%{content_type}',url,'-o',str(p)],capture_output=True,text=True)
  status=r.stdout.splitlines(); b=p.read_bytes() if p.exists() else b''
  out.append(dict(source_id=sid,requested_url=url,final_url=status[1] if len(status)>1 else '',http_status=status[0] if status else '',media_type=status[2] if len(status)>2 else '',retrieved_utc=at,method='curl public unauthenticated HTTPS; verified TLS',exit_status=r.returncode,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),local_file=p.name,error=r.stderr or None))
  print(sid, status[0] if status else 'error',len(b))
 (DEST/('acquisition-'+stamp+'.json')).write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
