# Development decisions

- 2026-10-11, development session: S005 selected to test finite-horizon liquidity rather than repeat S004's static consumption floor.
- 2026-10-11T21:03:17Z, recorded retrospectively: closest prior work narrowed novelty to a specific audit method and application. No broad originality claim retained.
- Base run: 45 policy environments; 11,979 family/path rows; exact rational arithmetic. Cash-only, early-sale, late-sale, and alternative income-rights results retained.
- Counterexample: with receipt in period 4, immediate loss of fund income makes every positive sale worse than no sale for the main uncertainty set.
- Counterexample to that penalty: retaining income until settlement removes the increase in early reserve need. The early gap remains.
- Ten tests executed and passed. No failed model result was discarded. No statistical inference or measured success probability is claimed.
- Study remains Working notes until separate AI review and release gates are complete. No GitHub mutation was performed by the author agent.
