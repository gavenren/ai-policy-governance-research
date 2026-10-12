# S010 codebook and audit appendix

State: Working notes. One AI author coded this corpus. A separate AI review is complete; it found no blocking issue within the stated scope.

## Unit and case boundaries

Each row is a relation between a decision and an authority in an identified document. The sample contains three selected institutions, six dimensions per case, and nine decision routes. It is not a population sample. Alaska is a resident dividend plus an investment fund; Norway is a fiscal fund; New Zealand is pension prefunding. Their benefit promises are not equivalent.

The target is the allocation of authority described in the documents. The study does not measure service quality, actual influence, corruption, return, benefit adequacy, or court success. It does not rank countries. A missing power is **unknown in this corpus**, not legally absent.

## Dimensions

| Code | Question | Inclusion rule |
| --- | --- | --- |
| claim | Who owns or benefits from the assets? | Record the stated public owner or purpose. Do not turn that purpose into a fixed individual payment right. |
| spending | Who controls public transfers or administers payments? | Separate fund withdrawals, budget decisions, and applicant administration. An unverified withdrawal formula stays uncoded. |
| voting | Who directs investments and corporate votes? | Record the mandate and its operational allocation. Do not infer direct citizen instructions from public ownership. |
| direction | Which public body may direct the fund, and within what limit? | Distinguish appointment, mandate setting, and portfolio decisions. A pending bill is not an enacted change. |
| oversight | Who reviews conduct or receives reports? | Record audit, reporting, external assessment, and public comment separately from a personal right to reverse a decision. |
| challenge | What decision can be challenged, by whom, and with what result? | Identify the scope and power that the source establishes. Do not infer a binding investment remedy from a contact address or information appeal. |

## Coding fields

`data/coding.csv` is the immutable author-coded input for this draft. `row_id` combines the case and dimension. `source_fact` paraphrases the positive allocation or official description. `author_interpretation` states the inference. `source_ids` links the source manifest; multiple values use semicolons. `locators` gives the provision or stable heading for each claim. `evidence_level` records the descriptive basis. `limit` records what the row cannot establish.

`data/decision_routes.csv` applies the coded rows to the same three questions in each case: a lower payment or transfer, a disputed company vote, and a complaint sent to the fund. `responsible_authority` states the body whose power must be reached. `identified_route_scope` and `documented_power` are deliberately separate. `binding_requested_remedy` is `unknown` unless the specific route supports a narrower positive description. No row is coded as an unlimited right to obtain the claimant's preferred result. `unknown_further_route=yes` means the study has not exhausted every possible public-law route. It does not negate the routes positively documented here.

## Decision rules and difficult cases

1. A public purpose does not become a personal entitlement by interpretation alone. Norway's state ownership and New Zealand's Crown asset pool remain public arrangements in the coding.
2. An appeal guide can establish a defined route without proving practical access. Alaska's guide supports administrative and later court review of eligibility. The historical budget case shows that judicial access can coexist with rejection of the requested payment result.
3. A written right to seek investigation is weaker evidence than a binding corrective order. The New Zealand information letter establishes the former for that information decision. It does not establish an order to change the portfolio.
4. Public comment is a participation channel. It is not a trustee vote. The Alaska manual is coded accordingly.
5. Temporary rules can change the available action while leaving the ethical aim in place. Norway's current index and interim rules replace reliance on the earlier exclusion procedure. The coding preserves engagement, voting, and possible sales within the mandate; it does not claim a ban on every sale or divestment.
6. An institutional separation can exist alongside review. Additional court powers would not make the pension reserve the payment administrator. Such powers could, however, change any claim that a remedy is unavailable. This study makes no general absence claim.
7. The Norwegian English documents expressly reserve legal authenticity to Norwegian texts. The codes describe government-hosted English information texts. N2 also states that its translation is not official or authorised. The New Zealand codes describe current fund pages because the full current statute was not successfully obtained. Those limits apply to every relevant row.

## Evidence and interpretation trail

`sources/extracts.csv` contains short exact extracts, not complete snapshots. Its quotation budget is at most 25 words for each source across the file. The row-level locators and longer paraphrases carry the audit; an extract is an anchor, not a substitute for reading the full provision. `sources/manifest.json` hashes the bytes actually held locally. Some are downloaded originals; others are reader-produced text. The two are never treated as the same representation. `sources/instruments.csv` records version, status, and limits. `sources/captures.jsonl` also retains failed or unsuitable attempts, which are excluded from the analytic corpus.

The scanned Alaska investment policy was read visually at its cover and pages 6–7. Its text extraction contains page markers rather than usable prose. The local image hashes record which renderings were inspected. Text matching is not claimed for that manual transcription.

## Sensitivity and adverse evidence

The sensitivity exercise grants every unknown additional challenge route as a hypothetical possibility. It then retains the positive allocations in the documents. This is a logical boundary test, not an empirical estimate or a statistical robustness test. It shows which conclusion survives that permissive assumption: a complaint still has to reach the appropriate authority. It does **not** show that any disputed remedy is impossible.

The nine route records are each reported under both assumptions in `results/decision-routes.md`. `results/sensitivity.json` records the assumptions and the claims that must remain withheld. The calculation does not infer legal powers. The adverse examples also matter: Alaska's claimants obtained judicial review but lost the contested payment claim; the Universal Fund proposal permits direct voice without guaranteed investment income. Both limit a claim that a review process or voting right is sufficient for income security.

## Repeatable checks

The validation checks balanced case coverage, unique keys, complete fields, source links, locators, quote budgets, and local links. With private local sources available, it also checks byte lengths, source and extraction hashes, and short extract matches. Generated tables must match a fresh run. These checks verify file and coding consistency. They cannot verify legal interpretation, completeness of source discovery, or the practical effectiveness of a remedy.
