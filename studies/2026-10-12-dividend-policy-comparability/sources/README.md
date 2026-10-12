# Source record and rights

This is the evidence package for S018. It is not a claim that the research or numerical review is complete. The [manifest](manifest.csv) records the exact retained bytes, original download times, versions, read scope and rights. JSON contains the same rows.

The source under audit is Robert DeMaria's *The Four Pillars: A Comprehensive Economic Framework for Universal Basic Income in the Age of Automation*, Working Paper v2.0, April 2026. The pinned repository revision is `d0e84f01f7970c6161da874051aafffaefe77f1f`. The commit date is April 20, 2026. That date does not replace the dates printed inside individual documents. The source is a proposal and public working paper, not enacted policy. The repository's own descriptions do not prove external peer review.

The evidence cutoff is **2026-10-12T19:00:03Z**. It means the original bytes used here had been acquired by that time. Some local reading, ledger preparation and migration occurred later. The independent reviewer checked the live main revision at 18:58:28 UTC and obtained the same revision. A later status check must be logged separately. Pinned evidence does not change if the live branch changes.

## Retained evidence

The whitepaper is retained unchanged in `snapshots/`. Its stated licence is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), as specified in the unchanged `LICENSE-DOCS.md`. Attribution is to Rob DeMaria / The Four Pillars Project. No changes were made to the retained whitepaper. No endorsement is implied. The source's root and code licence notices are also retained unchanged.

The two numerical scripts are retained unchanged in `../vendor/four-pillars/`, with their MIT notice and an origin README. Only these source scripts are part of the selected numerical audit. The other five scripts were downloaded to private reference storage. The manifest distinguishes files read in part from files acquired but not read. Downloading a file does not establish its correctness.

The April 19 post-launch note is outside the directory scopes of the specific document and code licences. A root MIT licence is present, but this package does not rely on it to publish that complete note. A short extract, its pinned URL and its full private hash are available. The note already acknowledges a discrepancy in the reported surplus probabilities. It must be discussed in any critique.

Hoynes and Rothstein (2019) and the OECD (2017) technical note are retained privately with extraction metadata. Only short quotations are public. The Wenger repository README is also retained privately. It is prior model documentation; its claims were not independently validated here. Its code was not run.

The quote ledger is `../evidence/short-quotes.csv`. It contains small exact quotations with source locations. It is not a substitute for the read-scope record. All other discussion is original analysis or paraphrase. A failed direct OECD web request and a failed first local TLS request are logged as access limits. Neither was bypassed by disabling certificate checks.

## Check the package

From the repository root:

```text
python3 studies/2026-10-12-dividend-policy-comparability/code/check_sources.py
python3 studies/2026-10-12-dividend-policy-comparability/code/check_sources.py --local
```

The first command checks public source copies, licence files and quote metadata. The second also checks retained private bytes and quotation text. The private check requires the ignored local reference folders. A public reader can download the exact pinned URLs, compare SHA-256 values, and read the original texts. Network acquisition is separate from these checks. The checks do not run a model or validate a forecast.
