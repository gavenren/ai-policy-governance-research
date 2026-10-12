# Four Pillars: separate feasibility check

Recorded 2026-10-12T18:59:34.380095+00:00. This is a source screen, not a completed study or numerical review. The reviewer is a separate AI agent with shared context. No source model was imported or executed.

## Gate decision

A short replication comment is justified **if** it reconciles the source's reported probabilities with its actual payment rules and reports a matched-path comparison. Do not treat another demonstration that higher benefits cost more as new research. Do not expand this into a verdict on UBI, taxation, retirement or the source author's conduct. If the result is only the already acknowledged table mismatch, a brief correction note is sufficient.

The source is [Robert DeMaria's Four Pillars project](https://github.com/saccasolutions/fourpillarsproject/tree/d0e84f01f7970c6161da874051aafffaefe77f1f), pinned at `d0e84f01f7970c6161da874051aafffaefe77f1f`. A fresh official repository API check at 18:58:28 UTC returned that same main-branch commit. File hashes and exact read limits are in [the source record](feasibility-source-record.json).

## What is already clear without execution

The whitepaper's Section 2.1 explicitly makes payment increases discretionary and says the floor is not indexed. The strongest favorable reading is therefore that a longer forecast intentionally holds the initial nominal floor fixed. Such a policy is coherent within this model. Section 6.4's statement about unchanged parameter distributions can also be literally true: the common growth draws use the same distributions. It does not establish that the payment rule is unchanged.

The two implementations differ on that rule. In `models/monte_carlo_tax.py`, lines 154–163, each year starts with the base floor cost. After year 5 a revenue test can apply a 12% increase, and after year 8 another test can apply a 20% increase. The second test uses the floor value left by the first test. The code resets the floor each year; it does not carry an earlier increase forward as a permanent entitlement. In `models/extended_monte_carlo.py`, lines 100–108, the floor remains at base cost. Extending the horizon alone does not describe this difference.

There is also a direct internal result problem. The whitepaper abstract and Section 6.2 place a negative year 10 median gap beside a surplus probability above 50%. The released code defines these as the median of that year's gap array and the share of strictly positive gaps in that same array. Those summaries cannot both hold for that array. Section 6.4 instead lists a positive year 10 median with 55.7%. Execution is needed to assign each printed value to a particular implementation; this note does not yet make that assignment.

The source itself already notices a discrepancy. The full post-launch note's section on whitepaper updates contrasts the older roughly 34% figure with 55.7% and asks for reconciliation. Thus, an audit must acknowledge that disclosure. It should not claim to discover that the authors were unaware of the conflicting numbers. What remains absent from the inspected discussion is a clear attribution to different benefit rules, together with a comparison holding the random paths fixed.

## What a bounded design must control

1. Preserve and run both pinned source scripts unchanged as baseline reproduction. Report any mismatch with their printed tables. Neither run alone isolates a policy effect.
2. Define surplus as positive annual gap, distinct from first passage, cumulative fiscal balance, financing feasibility or long-run solvency. The code's probabilities are conditional simulation shares, not empirical confidence in a national policy.
3. Use the same economic paths for fixed-floor and conditional-floor calculations. Both scripts seed the generator with 42, but a 20-year simulation consumes more random draws before the next simulation starts. Thus the same seed does not pair their 2,000 paths.
4. Preserve the source's exact annual reset, strict inequalities, sequence of the two tests, and denominator terms. Do not silently repair those choices or call the rule a permanent ratchet. The declared stochastic floor-threshold parameter in the ten-year dictionary is not used by the rule.
5. Report the joint payment/budget comparison: the share receiving each modeled floor level, paired annual gaps, and the share whose annual surplus classification changes. Show periods before any increase can occur as a control. Do not replace payment protection with a fiscal-success count alone.
6. Keep the source's revenue assumptions fixed for the narrow comparison. The source spending boost does not respond to the size of the added floor in these two scripts. A matched result is therefore an accounting effect inside that model, not an estimated general-equilibrium response. Broad flaws in revenue calibration, benefit phase-out, price units and retirement transition require other work and should not be silently absorbed into this exercise.

The protocol must record these choices before model execution. The source's first ten annual displacement formulas agree in distribution; changing the ten-year script's horizon constant by itself would change its interpolation denominator. That would not be a valid horizon-only adaptation.

## Closest prior work and limits

The [OECD 2017 technical note](https://www.oecd.org/els/soc/Basic-Income-Policy-Option-2017-Brackground-Technical-Note.pdf), Sections 1 and4, already makes fiscal policy comparisons by changing either basic-income amounts or tax rates to achieve a fixed budget condition. Its explicit scenario construction and distinction between hypothetical-family and population models preclude a novelty claim based on benefit generosity versus fiscal cost. It also shows why a financial comparison must name what is held fixed. This is static microsimulation prior work, not a direct audit of these scripts. No source estimate was reproduced here.

Within this programme, S004 and S005 already study real support and fiscal constraints. The potential increment here is a specific source-result reconciliation and matched-path account of a policy-rule change. That is narrower than a new strategy for post-labor public finance. The source lead is checking the broader UBI prior work separately. This bounded screen is not an exhaustive literature search.

Code is marked MIT; documents under `docs/` are marked CC BY 4.0. These labels do not automatically resolve rights for every other directory. Source originals remain private for this screen. No licence for new research is selected. No full paper, central implementation or simulated result has been created by this reviewer.
