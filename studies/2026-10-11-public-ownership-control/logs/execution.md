# Execution log

## Source extraction

Original downloads used Python `urllib.request` and HTML extraction through `html.parser`. PDF extraction used `pypdf 6.10.0`. Original bytes and extracted text have separate hashes. The Alaska investment policy was a scan. Its cover and pages 6–7 were rendered with `pdftoppm` and read visually; no OCR accuracy claim is made.

Primary-page reader capture times and representation hashes are in the source manifest. Direct requests that returned empty, blocked, or irrelevant content are excluded in the access log. Full source bytes are retained only in the ignored local source directory.

## Validation

Working directory for all commands below: this study directory. Environment: Python 3.13.7, standard library only. No random process or statistical estimate is used.

The first `python3 code/validate.py --write --with-local` run failed because the README linked the run record before the first run had written it. Source hashes and extract checks had passed before that error. The script was corrected to permit the run-record link during its initial write, then check that link in the independent read-only run. This was an execution-order error, not a changed evidence result.

At **2026-10-11T21:37:25Z**, the following commands completed with exit status 0:

```sh
python3 code/validate.py --write --with-local
python3 code/validate.py
```

The local run checked all 22 retained representations, the extraction hashes where present, and the exact text anchors except the explicitly manual AK12 transcription. Fourteen representations are downloaded original sources, six are institutional primary-page reader captures, and two are discovery-only records. The public run verified the same 18 coded relations and nine decision routes without depending on the ignored sources. Generated case and route tables agreed with a fresh computation. Input hashes and the exact run time are in `results/run.json`.

The sensitivity output grants every unknown additional review route as a possibility. It preserves the positive allocations of authority while withholding all general claims that a remedy is absent. This is a logical boundary check. It cannot show the real availability or effectiveness of a court remedy.

## Independent review

The stable package was sent to a separate AI reviewer after these checks. That reviewer did not write the central analysis. Its report and the author's response are now saved. The reviewer independently checked 13 high-risk relations and reran the local checks after three minor fixes. No blocking issue remains in the reviewed scope. Release checks remain with the programme maintainer, so the state remains Working notes.
