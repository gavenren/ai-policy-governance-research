"""Capture source versions without replacing the original ledger or older captures.
Run from the repository root. Requires pypdf. Network access is not used by model.py.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, urllib.request
import pypdf
STUDY=Path(__file__).resolve().parents[1]
REPO=STUDY.parents[1]
now=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
private=REPO/'.local-sources/international-dividend'/('recapture-'+now)
private.mkdir(parents=True,exist_ok=False)
records=[]
for source in json.loads((STUDY/'sources/manifest.json').read_text()):
    if source['status']!='retrieved':continue
    sid=source['id'];url=source['requested_url']
    row={'id':sid,'requested_url':url,'retrieved_utc':datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),'method':'Python urllib.request; pypdf '+pypdf.__version__}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 research source retrieval'})
        with urllib.request.urlopen(request,timeout=45) as response:raw=response.read();row['final_url']=response.url
        snapshot=private/(sid+'.pdf');snapshot.write_bytes(raw)
        row.update(snapshot_path=str(snapshot.relative_to(REPO)),byte_length=len(raw),sha256=hashlib.sha256(raw).hexdigest(),matches_original_hash=hashlib.sha256(raw).hexdigest()==source['sha256'])
        reader=pypdf.PdfReader(snapshot)
        extracted=''.join('\n--- PDF PAGE '+str(i+1)+' ---\n'+(page.extract_text() or '') for i,page in enumerate(reader.pages)).encode('utf-8')
        xp=private/(sid+'.txt');xp.write_bytes(extracted)
        row.update(extraction_path=str(xp.relative_to(REPO)),extraction_bytes=len(extracted),extraction_sha256=hashlib.sha256(extracted).hexdigest(),pages=len(reader.pages),status='retrieved')
    except Exception as error:row.update(status='failed',error=type(error).__name__+': '+str(error))
    records.append(row);print(sid,row['status'])
(private/'recapture-manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print('Saved a new private capture. The published evidence ledger was not changed.')
