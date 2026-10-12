# S016: Reconciling two measures of AI output

State: Protocol. Recorded: 2026-10-12T18:11:56.681399+00:00. No numerical execution for this study preceded this file.

## Question and bounded contribution

How much do two accounting choices affect the public power-based replication of Korinek and McKelvey's *Measuring the AI Economy*: (i) training volume measured by fixed-rental-price compute services or by physical operations, and (ii) monthly electricity extrapolated from the first two annual observations or constrained to each stated annual total?

The contribution is a source-specific reconciliation, conditional on the original inputs and assumptions. The price-volume identity and Fisher index are established methods. Bell's June 2026 sensitivity audit already varies training and inference deflators and the training share; his separate review distinguishes capacity, output, welfare and revenue. Our independent feasibility reader read both full eight-page papers. The proposed increment is to connect the two published training quantities, preserve a favorable interpretation of both, and trace an annual electricity accounting discrepancy through the same source pipeline. It is not a new index theory, an estimate of actual welfare, or evidence that AI already displaces all work. Source and closest-work evidence records will precede the manuscript's complete status.

## Prior knowledge and sequence

Selection is exploratory. Before this protocol, the root author read the main paper, the relevant appendix sections and source functions. A separate agent read the full closest audits and relevant OECD price-volume account. The root made informal hand estimates from rounded tables: physical compute divided by the algorithm ratio is larger than nominal spending divided by that ratio. Those hand estimates are not study results. Static code inspection found that the monthly power routine uses the first two totals to determine growth and only warns about later totals. No source/model function, numerical grid or formal output was run. The reviewer also identified the favorable fixed-rental-price interpretation before the protocol. These observations motivate the tests and are not preregistered discoveries.

Freeze the primary source ZIP at SHA-256 `85bf1b23a99f606abf3ab87b39ed9d3bc69a6d53a27d50ee31ff20d1f974ff8c`. Main paper B1 and author-hosted appendix B2 are retained in `.local-sources/ai-measurement-screen/`; the independent feasibility package also retains the publisher appendix and relevant prior work. Record each version and any differences. Keep unlicensed source code/data/PDF bytes out of the public study. Do not treat source inputs as newly verified empirical observations.

## Measures and hypotheses

Let V_t be nominal training spending and X_t be physical training operations under a common fixed training share. Let a be the annual algorithmic compute requirement ratio. The source's GDP calculation implies training volume growth (V_t/V_(t-1))/a. Its QA training series uses (X_t/X_(t-1))/a. They coincide only if spending and physical operations have the same growth. Because GPU-specific rental prices are constant but GPU composition changes, both can be coherent volume conventions: rental-service weighting and operations weighting. No empirical claim that the second is better is planned.

If the operations convention is chosen for the GDP training component, its coherent price ratio is a times (V_t/V_(t-1))/(X_t/X_(t-1)). Alternatively, retain the source GDP convention and report a training production series based on rental-service spending. Report both implied training growth rates and their ratio. Do not call the bridge an unconditional correction or infer actual price inflation from changes in average spending per operation.

For electricity, compare the source function's generated annual sums to all three listed totals before interpreting any alternative. Holding its within-year monthly pattern fixed, multiply each year's monthly values by the stated total divided by that generated year's sum. This enforces the annual inputs but does not recover observed monthly loads. Keep the source's listed annual electricity costs in all four main cases. A separate transparent ledger will show the alternative cost of charging the source-generated annual energy, without expanding to another policy grid.

## Fixed four-case design

1. Released monthly electricity rule and released training GDP deflator (positive control).
2. Released electricity rule and operations-consistent training GDP deflator.
3. Annual-total-preserving electricity rule and released training GDP deflator.
4. Annual-total-preserving electricity rule and operations-consistent training GDP deflator.

Retain source allocation, GPU characteristics, rental prices, inference price ratio (2.2/35), algorithm ratio (0.5^(12/8)), half inference share, service markup, labor treatment, electricity prices and AI-island boundary. No tuning to reproduce rounded table cells, no updated data, and no large sensitivity grid. Do not run the separate chip-sales or inference-index pipelines unless needed to resolve a source reproduction discrepancy; log such a deviation prospectively.

Report all years 2023–2025; annual spending, physical operations, labor, electricity quantities/costs; both training-volume series; component price ratios; nominal AI GDP; Laspeyres, Paasche and chained Fisher indexes; annual real growth; and the effect of each change. Use full-precision source outputs for calculations. Compare with every relevant printed cell at its displayed precision, retain failures and quantify differences. The source ZIP has an older README title; do not assume it exactly matches all paper tables. Results are conditional model calculations, not uncertainty bounds or corrected official national GDP. Do not re-estimate whole-US GDP.

## Execution and reproduction

Inspect code for network and filesystem effects before an offline run. Use a private fresh extraction of the frozen ZIP, with dependencies recorded. Prefer the unchanged power pipeline as the positive control. If an unavailable plotting dependency prevents this, install the free dependency in the local ignored tools directory, or document a narrower function-level run; do not pretend either is an unchanged full run. Preserve original source hashes and original output logs privately. Publish original reconstruction code, acquisition instructions, aggregate numerical input/output ledgers and source-byte checks, not third-party implementation or microdata without rights.

The four cases may call unchanged source functions through a documented adapter. The public analysis must also reconstruct the component ledger and Fisher index independently from aggregate inputs, with a check against the original baseline. Preserve any monkeypatch or parameter replacement explicitly in the adapter and metadata. Hash all source members used, scripts, inputs and deterministic outputs. A second run must reproduce deterministic results.

## Checks that can reject or narrow the result

- Match the released source's default training and GDP outputs before attributing a difference to our choices; report source warnings and reproduction failures.
- Verify that annual power matching changes no within-year composition or relative monthly profile, and sums to all listed totals.
- Independently confirm price times volume equals nominal spending for both conventions.
- Positive control: unchanged spending per operation gives identical conventions; a common rescaling of currency or physical-operation units leaves growth comparisons unchanged.
- Positive control: geometrically consistent annual electricity totals are preserved by the source rule and by the alternative.
- Counterexample: GPU mix can change spending per operation even with every GPU-specific rental price fixed; do not interpret the bridge as pure rental-price change.
- Verify finite positive nominal value added and both Fisher factors/denominators before reporting any real index. A nonpositive case is reported as undefined rather than coerced.
- Check signed output-minus-import accounting, unchanged nominal GDP under a training-price-only change, and the separation of level and growth effects.
- Compare the source function and an independent formula for all four cases, not only headline cells.
- Do not fit confidence intervals to deterministic cases. Printed rounding tolerances are presentation checks, not sampling uncertainty.

Stop after the fixed design, necessary debugging and review. Extra cases require a dated reason before execution. If an essential input or source match fails, publish only the narrower verified claim or leave working notes; never silently discard a contrary result.

## Writing, review and policy scope

Use a concrete opening example and normal connected academic prose. Put detailed identities in an appendix. State the favorable interpretation prominently, report null results and link every table to outputs. Tie the analysis to the interpretation of monitoring indicators for an economy with less human work. Do not infer tax capacity, household income or an optimal policy from a quality-adjusted output index; acknowledge that this caution already appears in the closest review.

A separate AI reviewer who did not author the central analysis will inspect the frozen manuscript, sources, code, inputs and all main results. Its earlier static feasibility role and shared conversation context must be disclosed; this is not blind or human peer review. Record hashes, actual checks, limitations and an author response. Complete-study status requires the repository protocol's gates, a fresh pivotal-source version check, publication to the authorized repository and exact-byte remote verification. No original-work licence, paid service or author contact is authorized.

## Analytical addendum: 2026-10-12T18:14:29.195237+00:00

Before any numerical results were received by the root author, a directional check was derived from the stated Fisher formula. With nominal components fixed, write its square as (Y_t/Y_previous) times (V_training,t / pi + B)/(V_training,previous * pi + C). If both required factors are positive, lowering the training price ratio pi strictly raises the Fisher factor. Thus choosing the operations convention raises this factor when physical operations grow faster than spending. This adds an explanation and a check of existing cases; it adds no cases, fitted parameters or result-selection rule. The numerical agent may already be setting up the source run; this addendum is not a claim of independent preregistration.

## Terminology note: 2026-10-12T18:17:12.342926+00:00

The opening question says first two annual observations. These are the source model’s stated annual electricity assumptions, derived from projections, not newly verified observations. This wording correction changes no input or case. The original source run has now occurred; its results remain subject to independent reconstruction and review.
