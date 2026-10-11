"""Public-source acquisition only; offline model needs no network or packages.

Use curl with normal TLS checks. Originals stay in ignored .local-sources.
HTML extraction uses Python's HTMLParser. PDF extraction, if requested, uses
the optional pypdf package. Never install packages automatically.
"""
from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime, timezone
import csv
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
STUDY = Path(__file__).resolve().parents[1]

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.skip:
            self.skip -= 1
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'li'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def main():
    specs = json.loads((STUDY / 'sources/catalog.json').read_text())
    capture = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    folder = ROOT / '.local-sources/benefit-access' / capture
    folder.mkdir(parents=True, exist_ok=False)
    rows = []
    for spec in specs:
        path = folder / (spec['source_id'] + ('.pdf' if spec['media_type'] == 'application/pdf' else '.html'))
        start = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        proc = subprocess.run(['curl', '--fail', '--location', '--silent', '--show-error', '--max-time', '45', '--output', str(path), '--write-out', '%{url_effective}\n%{http_code}', spec['url']], capture_output=True, text=True)
        row = dict(spec, retrieved_utc=start, requested_url=spec['url'], acquisition='curl HTTPS, TLS verification enabled', exit_status=proc.returncode, final_url=proc.stdout.splitlines()[0] if proc.stdout else '', diagnostics=proc.stderr.strip())
        if proc.returncode == 0:
            raw = path.read_bytes()
            row.update(original_path=str(path.relative_to(ROOT)), original_bytes=len(raw), original_sha256=sha(raw))
            if spec['media_type'] == 'application/pdf':
                try:
                    import pypdf
                    reader = pypdf.PdfReader(path)
                    content = '\n'.join(f'\n[PDF PAGE {n}]\n'+ (p.extract_text() or '') for n,p in enumerate(reader.pages,1))
                    method = 'pypdf ' + pypdf.__version__ + '; no OCR; page markers added'
                except ImportError:
                    content, method = '', 'not extracted: optional pypdf absent'
            else:
                parser = TextParser()
                parser.feed(raw.decode('utf-8', errors='replace'))
                content = '\n'.join(' '.join(p.split()) for p in ''.join(parser.parts).splitlines() if p.strip())
                method = 'Python '+sys.version.split()[0]+' HTMLParser; script/style removed; whitespace normalized; no OCR'
            if content:
                extracted = path.with_suffix('.txt')
                extracted.write_text(content, encoding='utf-8')
                text_bytes = extracted.read_bytes()
                row.update(extracted_path=str(extracted.relative_to(ROOT)), extracted_bytes=len(text_bytes), extracted_sha256=sha(text_bytes), extraction=method)
        rows.append(row)
        print(spec['source_id'], proc.returncode, row.get('original_bytes', 0))
    log = STUDY / ('logs/acquisition-' + capture + '.json')
    log.write_text(json.dumps(rows, indent=2)+'\n')

if __name__ == '__main__':
    main()
