"""Build a provenance ledger and short extracts from locally retained captures."""
from pathlib import Path
import csv
import hashlib
import json
import re

STUDY=Path(__file__).resolve().parents[1]
ROOT=STUDY.parents[1]
DETAILS={
 'B01':('Abstract; sections 3, 4, 6','Standard queueing guidance from Erlang-A that does not address endogenous congestion fundamentally understaffs','CC BY 4.0 stated on arXiv HTML; attribution given; full capture not distributed','US SNAP call-center model; not post-labor benefits or advance-payment finance','Queueing access failures and endogenous repeat calls already have a formal model.'),
 'B02':('Author abstract on NBER landing page','Using a field experiment involving 65,000 Los Angeles applicants','All Rights Reserved stated on NBER footer; short extract only','Los Angeles SNAP experiment; abstract read, full paper not acquired','Interview access affects approvals; no model parameter is borrowed.'),
 'B03':('Abstract; Data collection; Findings; Discussion','We conclude by highlighting three costs: temporal, financial, and emotional.','CC BY 4.0 stated in publisher HTML; attribution given; full capture not distributed','44 UK Universal Credit participants; qualitative study, not a prevalence estimate','Automated payment processes can impose time, money, and emotional costs.'),
 'B04':('Strategy, third key action','provide accessible, multi-channel grievance redress mechanisms integrated into delivery systems','Full redistribution terms not checked; short attributed extract only','World Bank programme overview; institutional design, not causal evaluation','Payments, registries, and grievance systems are already linked in delivery-system policy.'),
 'B05':('Abstract; sections 1.2 and 2','high-need users have no viable outside option','arXiv perpetual non-exclusive licence stated; redistribution permission not assumed; short extract only','Stylized congested social services with strategic arrivals; not benefit funding','Prior models explicitly study users without viable outside options.'),
 'B06':('Assessment paragraph 13 and Statistical Annex paragraph 6','The median payment delay is one day longer','Open Government Licence v3.0 stated, except third-party rights; short attributed extract only','UK UC advances model self-assessment, 1 April 2025 to 31 March 2026','Official report states a one-day median additional delay among referred requests later approved; not a tail guarantee.'),
 'B07':('PDF page 11 / printed page 9, section 2.3; introduction and section 3','The aim of prepayments is to prevent applicants from facing liquidity constraints while awaiting the application decision.','Public working paper; full redistribution terms not checked; short attributed extract only','Rotterdam applications 2013-2019; empirical processing-time and prepayment study','Prepayments and their role during review predate this study; employment estimates are not transferred to a post-labor case.')
}

def main():
    paths=sorted((STUDY/'logs').glob('acquisition-*.json'))
    rows=json.loads(paths[-1].read_text())
    manifest=[]
    for row in rows:
        sid=row['source_id']
        location, quote, rights, coverage, interpretation=DETAILS[sid]
        content=(ROOT/row['extracted_path']).read_text()
        normalized=re.sub(r'\s+',' ',content)
        if quote not in normalized:
            raise ValueError('extract not present: '+sid)
        if len(quote.split())>25:
            raise ValueError('extract too long')
        if sid=='B03':
            row['authors']='Hayley Bennett; Morgan Currie; Lena Podoletz'
            row['publication_date']='2024-09-18 online; 2026-01 journal issue'
        if sid=='B04': row['publication_date']='unknown; URL contains 2025-09-19, no visible date verified'
        if sid=='B06': row['publication_date']='2026-07-09'
        extract=f'# {sid}: evidence extract\n\nTitle: {row["title"]}\n\nAuthor or issuer: {row["authors"]}\n\nSource: {row["url"]}\n\nLocation: {location}\n\n> {quote}\n\nThis is a short extract, not a full snapshot. Rights: {rights}.\n'
        dest=STUDY/'sources/snapshots'/f'{sid}.md'
        dest.write_text(extract)
        row.update(claim_location=location, interpretation=interpretation,
                   coverage=coverage, rights=rights, redistribution='short extract only; original and extracted full text excluded from Git',
                   public_extract_path=str(dest.relative_to(STUDY)),
                   public_extract_bytes=dest.stat().st_size,
                   public_extract_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),
                   extract_quote_words=len(quote.split()),
                   capture_relationship='first retained capture; immutable acquisition log keeps initial unverified metadata',
                   adoption_date='not applicable',effective_date='not applicable',applicability_date='not applicable',
                   status='research or official report; not treated as binding law',
                   extraction_limits='HTML layout and equations may be imperfect; B07 has ligature/punctuation artifacts and ten repaired PDF object warnings; selected extract verified in extracted text')
        manifest.append(row)
    fields=list(dict.fromkeys(k for row in manifest for k in row))
    with (STUDY/'sources/manifest.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields)
        writer.writeheader()
        writer.writerows(manifest)
    print('Verified and recorded',len(manifest),'source extracts.')

if __name__=='__main__': main()
