# Benefit-unit extension completion

State: Complete-study draft extension. Transition at 2026-10-12T17:38:47.769698Z. This updates S011; it does not create a new study. The original analysis and evidence remain unchanged. No human or journal peer review is claimed.

## Completed gates

1. **Contribution:** `protocol.md` preceded the first outcome run. OECD scale guidance and Browne–Immervoll's common-budget microsimulation were read. The contribution is the matched-budget application to the debt diagnostic and its outcome-dependent ordering, not a new equivalence scale.
2. **Evidence:** `sources/manifest.json` identifies five sources and actual retrievals. The selected roster is derived from the public Federal Reserve data with public-domain attribution. Source E5 was added during review; its tool-text capture and failed original-HTML request are explicit. No fresh legal assertion is made.
3. **Execution:** the original 52 files pass the preservation check. The author source/data check was run again by root before release and passed: 192 estimands, 999 replicates, five source records, four short quotes and eight local source files. The separate review independently rebuilt the roster and all 192,768 estimates, paired uncertainty and 6,024 budget comparisons. Its ten author tests passed.
4. **Inference:** equal gross payments are not equal net fiscal cost or welfare. The person outcome assigns a pooled PEU result to members. Top-code exclusions, capped-roster sensitivity, needs assumptions and fixed debt obligations remain explicit. The original classification gap is not a general policy objective.
5. **Review:** `reviews/critical-review.md` records two findings; both are resolved in the author response. Original reviewed manuscript SHA-256 was `b5ca8684984462a745ecf029c3382b3e29292a13cf9225d1086aec7052056e10`. Root verified all 36 frozen files against `logs/review-ready.json` before release edits.
6. **Disclosure:** AI drafting and separate AI review remain visible. No affiliation, funding, human endorsement or research participation was invented.
7. **Release:** root read the full extension, changed only completion language in the scientific manuscript and study READMEs, and inspected selected files for private paths and unrelated material. The exact closure changes are in `reviews/release-only.patch`. Source data and numerical outputs are unchanged. Staged whitespace and exact remote-byte checks are separate release actions; their actual results are saved in the final release record or external receipt.

The independent review script pins the working snapshot. To reproduce its original hash gate in a separate checkout, reverse `reviews/release-only.patch` with `git apply -R` before running it. Do not reverse the patch in a shared active checkout. No numerical result changes with these closure edits.

The initial default whitespace check reported existing extra final blank lines in eight reviewed files, and single-space context lines that are required by the generated unified patch. Reviewed input bytes were preserved. The final check uses `core.whitespace=cr-at-eol,-blank-at-eof` and excludes only `reviews/release-only.patch`; no other whitespace alert is accepted. `git apply --reverse --check` confirms that the closure patch can recover the reviewed files.
