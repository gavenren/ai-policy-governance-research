# Editorial revision record

**Date:** 2026-10-11T21:28:01Z. **Scope:** paper.md only. This is an editorial revision, not new analysis or a replacement for the independent critical review.

## Purpose and changes

The user requested clear research prose for policy readers. The article now starts with the economic problem and an existing worked example. The main discussion explains the results before the technical detail. Proofs and replication details are in appendices. Economic notation uses inline math rather than code formatting. The AI disclosure appears in one place.

- Original Sections 1–2 become a connected introduction and literature discussion. The stable-backlog example introduces the problem without changing its values.
- Original Sections 3–4 remain the model and cash accounts. Their proofs move to Appendix A; the formulas and their limits remain in the main text.
- Original Sections 5–6 remain the stable-queue result and complete numerical results.
- Original Sections 7–8 become a connected policy discussion and limitations. Test details move to Appendix B.
- Disclosure is consolidated. A conventional reference list is generated from the seven existing source-ledger records; no new source was collected.

## Claim-preservation checks

The revision preserves the full eligible-funding assumption, all three payment rules, fractional proportional service, review accuracy, immediate partial recovery, both settlement orders, the difference between due-date and two-period delay measures, and the restricted meaning of measured timeliness. All formulas, all seven numerical table rows, the 567-path counts, and the period-thirty reserve failure are retained. References remain linked beside the same factual claims. The new bibliography uses only existing ledger metadata, including unknown dates and version limits. No code, data, numerical output, source record, or earlier review file was changed. Release hashes must be refreshed for the revised manuscript.

- Manuscript before SHA-256: `553af9fd388d2c77dcc9e33827175bb5633fefb2a5f80c55fe90308903daa804`.
- Manuscript after SHA-256: `8680c230747010703faab708c633e12529e71f2de2a4c05e253dd0f4532e852a`.
- Words before: 3608; words after: 4281.

## Mechanical checks

Compared the revised manuscript with the prior Git version. The multiset of displayed equations is unchanged. All numerical table rows, including row order and values, are retained. All local Markdown links resolve. The manuscript passes the whitespace check. These checks support the editorial review; they do not independently validate the model.

## Review status

The separate editorial review is complete. See [editorial-independent-review.md](editorial-independent-review.md) for the final manuscript hash, checks, and limits. The coordinating agent accepted the revision for release.

Coordinating edit: removed one duplicated explanation identified by the separate editorial reviewer.
