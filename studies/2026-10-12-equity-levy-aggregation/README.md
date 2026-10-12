# S015 — How Much Would an AI Equity Levy Collect?

**State: Complete-study draft.** Numerical analysis, separate AI critical review and reproduction are complete. See the [review](reviews/critical-review.md), [response](reviews/author-response.md) and [completion record](logs/completion.md). This is a short robustness note about the information in one public scenario model, not an empirical revenue forecast.

Read the [paper](paper.md), [prospective numerical protocol](protocol.md), [separate feasibility review](reviews/feasibility.md), and [source guide](sources/README.md).

The source already discloses that Figure 3 uses group sales patterns. Conditional on interpreting those patterns as equity-value-weighted means, the note derives the collections compatible with unknown firm variation. It preserves the source's valid accounting results. The source's group total is the conditional upper bound; individual country points need not be their respective upper bounds. Full membership fixes total collection, given unchanged values and compliance.

## Reproduction

Use Python 3.12 or later and NumPy. The recorded analysis used Python 3.12.14 and NumPy 2.3.5. The core model and unit tests use only the standard library; NumPy executes the unchanged source functions as a positive replication. No paid service or network access is needed for analysis. Run from the repository root:

```text
python3 studies/2026-10-12-equity-levy-aggregation/code/check_sources.py
python3 -m unittest discover -s studies/2026-10-12-equity-levy-aggregation/code -p test_model.py -v
python3 studies/2026-10-12-equity-levy-aggregation/code/analyze.py --output /tmp/s015-rerun
```

Compare the seven deterministic result files with `results/`; `run.json` records actual execution time and software versions and should differ between runs. Its input, central-code, source-code and output hashes permit exact comparison. Do not execute vendor rendering or treat its partial checkout as the complete upstream project. The full source model is at the pinned URL in the ledger.

For source-byte checks on the author's machine, add `--repository .` to `check_sources.py`. This also checks ignored original captures. Those full captures are deliberately absent from the public package, so this optional mode needs a separately acquired matching corpus. The ordinary public-source check and model reproduction do not need them.

## Inputs and output schema

`data/raw/inputs.json` independently transcribes the source code's two universes, six destinations, decimal values and sales rows. Decimal strings and exact fractions avoid binary rounding in the new calculations. The broad values total 126.71 trillion dollars; the source documentation's finer 126.693 trillion anchor is not silently substituted. The unused zero-value tech rows use exact sixths. All rows are checked against the unchanged source code.

| File | Rows / object | Meaning |
| --- | --- | --- |
| `results/configurations.csv` | 384 | Two separate universes × three caps × all 64 member sets; total lower bound, source point, upper bound and full charge. |
| `results/groups.csv` | 2,304 | Every configuration × six source groups, including zero-value groups. |
| `results/members.csv` | 1,152 | Members only; each country's separate lower and upper bound and the source point. Upper endpoints need not coexist. |
| `results/entry.csv` | 2,304 | Every possible one-member addition under each configuration and two fixed populations; before/after totals, new member receipts and incumbent loss. |
| `results/witnesses.json` | Two populations | US-listed group and US–EU membership at cap three; one population attains each member's separate upper bound. Full means are preserved. |
| `results/summary.json` | Selected tables and counts | All prespecified five-club/cap-three summaries, cap sensitivity for the coalition without China/Hong Kong, and US–EU member results. |
| `results/source-checks.txt` | Source transcript | Unchanged upstream internal checks executed without rendering. |
| `results/run.json` | Execution metadata | Time, software, hashes and exit status. |

`mask` uses bit positions 0–5 for US, EU, UK, JKT, CN and RoW. `members` expands that set. `group` identifies a source listed-market row; `country` denotes one participating destination group. `cap` is a dimensionless multiple. Fields ending `_exact_T` are exact rational values in trillions of US dollars per levy year. Fields ending `_billion_USD` express the same values in billions with nine decimal places for checking, not as an empirical precision claim. For all configuration rows, `point` equals `upper`; that need not hold for member rows. Entry fields refer to the same population before and after entry. `destination_only` attains the total lower bounds; `homogeneous` attains total upper bounds.

The run checked 4,608 coalition-endpoint populations, 6,912 member-upper populations, 13,824 source collection cells and 2,304 source ledger cells. It rejects infeasible simultaneous upper endpoints. The complete set has one constraint system per group and coalition; the marginal country table is not a joint allocation set. There is no sampling distribution, fitted likelihood or real-world failure rate in these files.

## Evidence, rights and limits

Source-capture cutoff: **2026-10-12T17:46:29.147619Z**. The separate bounded feasibility search ended at 17:48:45Z. The separate review ran at 18:02:32–47Z. A later source check at 18:03:24–25Z confirmed the same pinned repository revision and identical essay bytes; API metadata bytes differed. See `logs/prepublication-source-check.json`. Source citations and actual read scope appear in the [manifest](sources/manifest.json). Financial anchors, company filings and legal enforceability were not independently validated. The sales weighting condition is explicit and materially limits interpretation.

The eight unchanged files in `sources/vendor/` retain Copyright (c) 2026 Silviu Pitis and their upstream MIT licence. This does not select a licence for new study material. Full nonlicensed originals remain in ignored storage; only metadata and narrow evidence are published. No raw private or personal data were used.

Codex authored the central analysis and manuscript. A separate AI agent prepared the source package and feasibility assessment, but did not author the central model or execute it before critical review. During critical review it reproduced the analysis and wrote a separate check that imports neither the author nor vendor model. The review had shared context and was not blind; its exact scope and content hashes are public. No human review, journal acceptance, institutional endorsement, actual collection or paid research is claimed.
