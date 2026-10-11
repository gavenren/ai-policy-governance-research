"""Build narrow published evidence files from retained source captures."""
import datetime, hashlib, json, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
local=pathlib.Path(sys.argv[1])
records=json.loads((local/'acquisition.json').read_text())
meta={
'A1':dict(title='Simulating a Post-Automation Economy',authors=['Leonard Wossnig'],version='arXiv:2606.20649v1',publication_date='2026-06-07',source_type='research preprint',location='Section 10.2, An explicit welfare criterion; also Sections 6.6, 6.15, 6.17 and Appendix A',quote='Policy comparisons remain positive (inequality and solvency), not welfare-optimal',rights='CC BY 4.0 stated in captured HTML; only a short attributed extract is distributed',coverage='Synthetic automation economy; domestic and foreign ownership; no current law claim',reading='Selected full-text sections'),
'A2':dict(title='When are digital services taxes optimal? Output taxes and profit shifting',authors=['Johannes Becker'],version='Version of record; doi:10.1007/s10797-026-09987-z',publication_date='2026-09-03',source_type='research journal article',location='Section 6, concluding remarks; also Sections 2.3-2.8, 3, 5; selected appendix',quote='Higher taxes on foreign-owned firms may enhance national welfare but reduce global welfare.',rights='CC BY 4.0 stated by publisher; only a short attributed extract is distributed',coverage='General tax model; foreign ownership; no national legal status used',reading='Selected full-text sections; some equations are images in HTML'),
'A3':dict(title='Public Finance in the Age of AI: A Primer',authors=['Anton Korinek','Lee M. Lockwood'],version='Brookings January 2026 release; manuscript 2025-12-30',publication_date='2026-01 (day unknown)',source_type='research working paper',location='Section 4.2, printed page 27 (PDF page 29); Section 2.4 for fixed factors',quote='between intermediate versus final use, and between the normal return to capital and rents',rights='No general redistribution licence verified; full PDF excluded; short attributed extract only',coverage='Theoretical AI fiscal stages; no present law interpretation',reading='Sections 2.4 and 4.2; PDF extraction with pypdf'),
'A5':dict(title='The Taxation of Digital Services as a Rent-Extracting Policy',authors=['Wolfram F. Richter'],version='FinanzArchiv 77(3), 225-246; doi:10.1628/fa-2021-0012',publication_date='2021-10-18 (publisher online date)',source_type='publisher abstract for research article',location='Publisher abstract, fifth sentence',quote='the quality of digital services will be negatively affected.',rights='No general redistribution licence verified; full page excluded; short attributed extract only',coverage='Abstract-level prior-work comparison only; full text not accessed',reading='Publisher abstract only'),
'A6':dict(title='Fiscal Limits to Protectionism: The 2025 U.S. Tariff Laffer Curve',authors=['Pau S. Pujolas','Jack Rossbach'],version='arXiv:2602.18938v1',publication_date='2026-02-21',source_type='research preprint',location='Abstract; Section 4.2; Appendix A.1-A.2; model overview',quote='We introduce the Marginal Fiscal Efficiency Index',rights='arXiv perpetual non-exclusive licence; this does not grant general redistribution; short attributed extract only',coverage='Tariff model and reported US calibration; this study does not adopt its calibration or current policy facts',reading='Selected full-text sections')}
manifest=[]
for row in records:
 sid=row['source_id']
 if sid not in meta: continue
 item=dict(row,**meta[sid])
 text=' '.join((local/(sid+'.txt')).read_text().split())
 quote=item['quote'];assert quote in text,(sid,quote);assert len(quote.split())<25
 item.update(language='English',rights_checked_utc=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),original_snapshot_scope='Original and extraction retained locally, excluded from Git; retrieve using code/acquire.py',original_snapshot_path=str(local/row['original_local_file']),extracted_snapshot_path=str(local/row['extracted_local_file']),legal_status='Research, not a binding instrument; adoption/effective/applicability dates not applicable')
 path=root/'sources/extracts'/f'{sid}.md'
 body=f"# {sid}: {item['title']}\n\nAuthors: {', '.join(item['authors'])}. Version: {item['version']}.\n\nSource: {item['requested_url']}\n\nRetrieved: {item['retrieved_utc']}. Location: {item['location']}.\n\n> {quote}\n\nThis is a narrow evidence extract, not a full source snapshot. Whitespace is normalized. Full source and extracted-text hashes are in the source manifest. Reading scope: {item['reading']}.\n\nRights: {item['rights']}. No change to the quoted words.\n"
 path.write_text(body)
 item.update(published_extract=str(path.relative_to(root)),published_extract_bytes=path.stat().st_size,published_extract_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),quoted_words=len(quote.split()))
 manifest.append(item)
(root/'sources/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(root/'logs/acquisition.json').write_text(json.dumps(records,indent=2)+'\n')
print('Verified',len(manifest),'source extracts; all below 25 quoted words')
