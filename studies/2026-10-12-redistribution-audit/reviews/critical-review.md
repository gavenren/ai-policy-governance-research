# Independent AI critical review of S012

Content check completed: **2026-10-12T16:56:35Z**. Reviewer: a separate AI agent in the same task. This agent wrote the earlier feasibility review and then checked the completed analysis. It did not write the study's central code or manuscript. The review was not blind. It is not human review or journal peer review.

**Decision: no remaining blocking issue in the checked content.** The paper supports a bounded, version-specific consistency audit. It does not support a new general inequality theorem, a forecast, or a general policy ranking. The manuscript states these limits. The author response, final state change and release checks were not yet present at this review cutoff; those remain release tasks.

## Content and hashes

I read the manuscript, protocol, README, data dictionary, full synthetic design, all four central code files, numerical tables and summary, source manifest, evidence record, search record and correction logs. I checked source passages in the retained PDF extractions and original TeX. I also read the relevant Cowell manuscript pages and the cited Growiec growth model. Earlier source inspection is recorded in [feasibility.md](feasibility.md).

[reviewed-hashes.json](reviewed-hashes.json) preserves the initial hashes and the final hashes of 26 study files, plus the review calculation files. Main final hashes are:

| File | SHA-256 |
|---|---|
| `paper.md` | `79e7006fdd7aa274349d8a321f379ede3884b3aba09ca5f074d1450897b828a5` |
| `code/analyze.py` | `099b791a7bb6d4950b4a251d545968552a911e8a6f2ac805e0e3c33dd2c0ed01` |
| `data/design.json` | `7aa6ee47723db5676d14e055e1ca4a8f84b254796138669a3d5b5b2d44c12c45` |
| `sources/manifest.csv` | `2a87e7ddf93a0e85b9dccb2381e9fd1f992e7402ea79eb85b610286e04061922` |

This review applies to those contents. A later edit to a main equation, result, source claim or interpretation needs a new check. A release-state update alone does not change the numerical findings checked here.

## Execution and independent calculations

The review used Python 3.12.14 for the retained validator, unit tests, separate reproduction and independent calculations. All four commands used the same bundled interpreter. The separate reproduction records its version in `reproduction.json`; the command record identifies that same interpreter for the other checks. The author's first retained analysis run used Python 3.13.7. These are distinct runs. From the study directory, I ran the commands below. The host-specific interpreter and temporary-folder paths are omitted from the public record.

```text
python3 code/validate.py --local-source-root ../..
python3 -m unittest discover -s code -p 'test_*.py' -v
python3 code/analyze.py --output <separate temporary output directory>
python3 reviews/independent_checks.py
```

The retained validator passed 10 numerical file hashes, nine planned tables, 2,620 rows, six source representation records and 12 retained original/extraction hash checks. All 15 unit tests passed. The separate output-directory run matched all nine CSV files and `summary.json` byte for byte. Its time-dependent run record was excluded from the byte comparison. [reproduction.json](reproduction.json) records the run and matching hashes.

I also wrote [independent_checks.py](independent_checks.py), which does not import the central analysis. Its [results](independent-results.json) report:

- Exact fraction calculations for all 72 affine rows. Income variance was calculated from second moments, and Gini from all ordered pairs.
- Exact Gaussian elimination for all 120 common-saving tax systems. This solves the household budgets jointly after substituting the equal rebate. It does not reuse the author's closed-form rebate implementation.
- Separate marginal-product calculations at 60-digit decimal precision for all 2,187 CES rows. These also check Euler's level identity, avoiding reliance on the central code's share-reconstruction control. They confirm 1,944 residuals above 10^−10 for the proposed log identity.
- Closed-form checks for all 24 input-path rows and exact fraction checks for all four income covariance rows.
- Exact checks of indexed equal payments and both heterogeneous-saving examples. The latter give relative variances 169/225 and 1/25, with rebates 1/3 and 3.

The largest independent discrepancy in a reported relative-variance result was about 1.33×10^−15. The largest CES output discrepancy was about 1.11×10^−15. The raw-variance comparison reached about 1.16×10^−10 on a large-tail example; this reflects floating-point rounding in a much larger quantity, not a different result. The independent file reports its tolerances and full scope.

I did not independently rebuild the random draw generator, the local finite-difference grid or the fixed log-index row. I inspected those methods and reproduced their retained outputs. The source acquisition was not repeated in this review round. I checked the reported acquisition log against the retained source hashes. I also checked the separately captured release-time history bytes and their recorded hash; that capture still showed only v1.

## Assessment of the central claims

**Equal transfers.** The paper correctly distinguishes raw variance from variance divided by the new mean squared. The two-person example, the affine formula, the indexed-payment calculation and the source's definition agree. The correction concerns the source's isolated equal-addition experiment. It does not assume that funding, prices or behavior have no policy effect. The income covariance formula is correctly retained as a positive control. The zero-component case is handled in levels, where no division by a zero component mean is needed.

**CES log identity.** The counterexample lies inside the source's stated nested CES form. The exact level identity and local differential are valid. The fixed-share log-index repair is also valid when it is declared as an index. The manuscript does not silently identify that index with household income. The constructed-grid residual count is descriptive, not a frequency estimate or proof by sampling. The exact counterexample provides the decisive test.

**Capital-share limit.** The stated condition S/K → infinity is correct for the specified outer CES parameters. The constant-ratio path shows that labor disappearance alone is insufficient. The manuscript correctly calls this an input path rather than a solved equilibrium. It also preserves the strongest supporting interpretation: the cited Growiec model has cognitive input proportional to A K with unbounded A. Thus this is a condition to state clearly, not a disproof of the cited model. Equal limiting growth rates need not imply a constant input ratio.

**Consumption tax.** The source specifies the equal rebate. With fixed pre-policy resources and a common saving rate, the household budgets and government budget imply the paper's reduction factor. The matching no-rebate case correctly leaves relative inequality unchanged. The heterogeneous-saving examples balance their budgets but sit outside the common-saving assumption. They are clearly presented as extensions, with no claim about realistic saving behavior or optimal rates. The appendix also distinguishes tax-exclusive resources from nominal receipts and from consumption alone.

These findings justify the four-way classification in the abstract and first table. They do not establish that every comparison in the source is correct, or that its broad preference for distributing capital rents is wrong.

## Evidence, references and corrections

The main source locators are correct: normalized variables and equation 4 on PDF page 5; income accounting on page 6; the capital limit on page 9; the UBI passage on page 11; and equations 22–24 on page 18. The PDF extraction and original TeX support the disputed expressions. Cowell's manuscript pages 18–22 correspond to PDF pages 20–24. Its definitions support the distinction between relative and absolute measures; its discussion also supports the manuscript's care about ordering invariance versus an index value that stays unchanged. Growiec's supporting limit is on author-copy PDF page 10, equations 15–17.

The evidence record publishes a short quotation, mathematical facts and original summaries. The arXiv record has a CC BY 4.0 link. Cowell's cover restricts further distribution, and permission to republish the full Growiec publisher copy was not established. Full originals stay in ignored storage. I found no need to publish them to support this audit. No legal-status claim or claimed legal endorsement appears in the paper.

The following review issues were sent to the author and then checked after correction:

| ID | Finding | Final disposition |
|---|---|---|
| R1 | The third source author's given name and reference initial were wrong. | Corrected to Maciej Szkróbka and M.; checked against the pinned PDF and arXiv metadata. |
| R2 | The dictionary said random ranges were in the protocol, but those ranges were not recorded there. | Actual ranges are now in the dictionary. The decision log states that they and the concrete component arrays were implementation choices. The earlier protocol was preserved. No false preregistration claim was added. |
| R3 | The source's cover date and arXiv submission date needed separate treatment. | Both dates are now recorded: 15 September on the cover and 13 September for submission. No explanation for the difference is invented. |
| R4 | The six-word UBI quotation was labeled as seven words. | Count corrected; wording matches the source. |
| R5 | The reported maximum budget residual used an incorrect three-significant-figure rounding. | Corrected to 2.27×10^−13; checked against the retained value. |

Code and numerical data did not change during these fixes. No new numerical run was needed to verify the text corrections. The final manifest still points to the same checked source bytes.

## Contribution, readability and remaining limits

The nearest work is the audited preprint itself. The mathematical tools are established. The search record discloses its bounded queries and missing exact times for early discovery queries. It does not claim first discovery or the absence of all earlier corrections. The paper's simple opening example, one main claim per section and separate technical appendices make the argument readable. The correct results and the limits on the critique are visible, rather than buried in a qualification at the end.

The review does not certify all citations in the original preprint, the full dynamic model of Growiec (2023), all alternative inequality measures, or general-equilibrium policy effects. It did not use visual PDF equation inspection or human expert assessment. The reviewer knew the initial hypotheses and had already written a feasibility note, so this is not an independent discovery or a blind replication. The separate implementation checks reduce one class of error; they do not guarantee correctness.

No remaining issue in the reviewed content blocks a complete-study draft. The programme still needs the issue-by-issue author response, accurate state transition and release checks. This review is not proof of GitHub publication.

## Review-record correction

At 2026-10-12T16:59:19Z, the reviewer corrected the interpreter sentence. It had incorrectly copied the author's first-run version, 3.13.7. The review's reproduction record gives 3.12.14, and the retained command invocations used the same bundled interpreter for validation, tests and independent checks. A version-only check also returned 3.12.14. No calculations were rerun for this correction. The original execution records and numerical results are unchanged.
