"""Optional source capture; analysis does not require network access."""
import pathlib,subprocess,datetime,json,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[3]
URLS={'S2':'https://pau-belda.eu/wp-content/uploads/Belda_Rojas_Zoi_SWF.pdf','D1':'https://www.aeaweb.org/articles?id=10.1257/jep.20251452'}
def main():
 out=ROOT/'.local-sources/public-capital-acquisition';out.mkdir(parents=True,exist_ok=True)
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ');rows=[]
 for sid,url in URLS.items():
  f=out/(sid+'-'+stamp+('.pdf' if url.endswith('.pdf') else '.html'))
  at=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
  p=subprocess.run(['curl','-L','-sS','--max-time','40',url,'-o',str(f),'-w','%{http_code}\n%{url_effective}\n%{content_type}'],capture_output=True,text=True)
  a=p.stdout.splitlines();b=f.read_bytes()
  rows.append(dict(source_id=sid,requested_url=url,final_url=a[1],http_status=a[0],media_type=a[2] if len(a)>2 else '',retrieved_utc=at,method='curl HTTPS with TLS verification',exit_status=p.returncode,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),local_file=f.name))
  print(sid,a[0],len(b))
 (out/('acquisition-'+stamp+'.json')).write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
