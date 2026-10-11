# Editorial revision record

**Date:** 2026-10-11T21:26:02Z. **Scope:** paper.md only. This is an editorial revision, not new analysis or a replacement for the independent critical review.

## Purpose and changes

The user requested clear research prose for policy readers. The article now starts with the economic problem and an existing worked example. The main discussion explains the results before the technical detail. Proofs and replication details are in appendices. Economic notation uses inline math rather than code formatting. The AI disclosure appears in one place.

- Original Section 1 is rewritten as an introduction with the existing three-period cash-gap example.
- Original Sections 2 and 3 remain the literature and model. Section references are updated.
- Original Section 4 is divided between a prose explanation in Section 4 and definitions and proofs in Appendix A. The reserve formula remains in the main text.
- Original Sections 5 and 6 are combined as Section 5, with all path counts, numerical tables, adverse cases, and sensitivity results retained.
- Original Sections 7 and 8 become the connected policy discussion and limitations. A conclusion states the same timing result.
- Original Section 9 becomes Appendix B and the research disclosure.

## Claim-preservation checks

The revision preserves the loss of income rights at commitment, the settlement alternative, the precommitted sale, the three uncertainty sets, all 45 environments, 11,979 retained rows, all base optima and binding constraints, the late-sale result, and the disposal-cost sensitivity. The finite horizon is still distinct from permanent solvency. All seven reference entries and all displayed equations are retained; only their location and prose context change. No code, data, numerical output, source record, or earlier review file was changed. Release hashes must be refreshed for the revised manuscript.

- Manuscript before SHA-256: `b10eb2da81e17a42d6a894e057e0d633c4a6cb33371125e533750babc0c596c2`.
- Manuscript after SHA-256: `b9887e5ff14b8710cc9fec182e759e739440a4da3e63092caa7f0dbd60c6ae4a`.
- Words before: 3877; words after: 4231.

## Mechanical checks

Compared the revised manuscript with the prior Git version. The multiset of displayed equations is unchanged. All numerical table rows, including row order and values, are retained. All local Markdown links resolve. The manuscript passes the whitespace check. These checks support the editorial review; they do not independently validate the model.

## Review status

The separate editorial review is complete. See [editorial-independent-review.md](editorial-independent-review.md) for the final manuscript hash, checks, and limits. The coordinating agent accepted the revision for release.

Coordinating edit: removed one duplicated explanation identified by the separate editorial reviewer.
