# S011 extension: benefit units and family size

State: **Protocol**. This is an addition to S011, not a new study. The plan is recorded before extension outcome calculations. The actual save time and file hash are in `logs/design-freeze.json`. It is not an external registration.

## Purpose and prior methods

The published S011 results use one transfer and one threshold per SCF family. This extension asks whether changing the payment unit changes the share below the after-payment threshold when aggregate payments are held equal. It does not introduce benefit units, equivalence scales, or budget-matched microsimulation as new ideas.

The OECD's 2013 statistical framework, Chapters 3 and 8, explains square-root scaling and its limits. It does not select a universal scale. It also warns that sharing costs can extend beyond a family economic unit. Browne and Immervoll (2018), Sections 3–4 and the discussion of individual payments on page 11, already compare benefit reforms with a common fiscal constraint and distinguish individual control of money from family needs. These methods support an explicit sensitivity analysis, not a new measure of poverty. This extension has no tax-benefit model or estimate of intra-family control.

Before this plan, the existing manuscript, protocol and code were read. The full public SCF file was obtained and only its schema, joins and member counts were checked. All 21,800 records match S011. Dependence flags reproduce reported primary-economic-unit size. No transfer outcome or policy ranking was calculated. The source record and `logs/feasibility-check.json` retain the pre-analysis checks.

## Units and population

The SCF primary economic unit (PEU), called a family here, contains the economically dominant person or couple and other financially dependent members. It can exclude independent people at the same address. Financial amounts cannot be assigned to each adult from these data. All payments are added at PEU level; full pooling within the PEU is assumed. “Per adult” identifies the payment formula, not the recipient's access to money.

Read the 12 roster positions, their ages and financial-dependence flags from the full public file. Include a roster person when the financial-dependence flag equals 1. Check reference-person inclusion and spouse/partner inclusion against X7020. Count an adult at age 18 or above. Public ages for other members combine ages 13–17 into one band and 18–25 into another. The adult boundary is retained, but the age-14 division in the modified OECD scale is not. Do not infer age-14 status or infer size from MARRIED and KIDS.

The primary population excludes X7001=12, which means 12 or more members. This excludes two families in each implicate, leaving 4,358. Their weighted share is about 0.033%–0.051% across implicates. Exclusion is fixed from the schema check, before outcomes. The main estimates apply to this covered population. A separate sensitivity includes all 4,360 families, sets size equal to the published roster count, and counts listed adults. It is a capped-roster scenario, not a bound on actual needs or adult counts. No upper bound on omitted members is assumed.

No observed family has zero adults. If a zero-adult record is encountered in a changed source, stop for investigation. Do not silently assign one adult or drop it.

## Fixed comparison

Retain only S011's wage-only resources N=max(INCOME-WAGEINC,0)/12, payment estimate D=TPAY, and original weights. Do not change the original data or results. Let n be PEU size, a its adult count and e=sqrt(n). Set each arm's total monthly payment to 2,000 dollars times the weighted number of included families.

For the three arms use v=1, v=a, or v=e. Pay each family U=c v, where c=2,000 sum(w)/sum(w v). Thus each arm has exactly the same gross payment budget within each estimation sample. This is equality of added gross payments, not fiscal neutrality after taxes, benefit offsets or administrative costs.

Use the same primary threshold F=1,000 sqrt(n) in all three arms. One person's threshold is 1,000 dollars; four people's threshold is 2,000 dollars. This is a size-adjusted policy assumption applied to the PEU, not an official poverty line or an observed needs budget. The single-person anchor remains fixed. It cannot account for disability, local prices, care costs, sharing with independent co-residents, or bargaining within families.

For a bridge to the published experiment, repeat the same three arms with F=1,000 for every family. This separates the change in the payment rule from the change in the adequacy test. Do not add further budget levels, scales, income shocks or payment-reduction grids.

## Outcomes and uncertainty

Report gross pass, after-payment pass, their paired difference, and mean monthly shortfall max(F+D-N-U,0). Report the person-weighted after-payment failure share as a supplementary statistic: every included PEU member is assigned the PEU outcome. It is not an individual consumption measure.

For the primary square-root threshold, also report the four family-level outcomes for size 1, size 2, size 3 or more, families with members under 18, and families without such members. Include sample counts and weighted denominators. Do not interpret a subgroup with fewer than 100 first-implicate families. Report payment rates per allocation unit and annual gross programme totals.

Compare all three pairs of arms, including the pair between adult and square-root payments. Compute paired differences for all five overall outcomes under each threshold. No policy is selected in advance as superior. A small, null or adverse change is a valid result. The capped-roster sensitivity repeats only the overall comparison and paired contrasts.

Use all five implicates and 999 first-implicate survey replicates. Recompute the payment coefficient c using each implicate or replicate's weights and the same population rule. Do not hold the estimated coefficient fixed when evaluating survey uncertainty. Combine sampling and imputation variance by S011's codebook formula. Also calculate paired contrasts within each replicate, retaining covariance. Confidence intervals describe survey uncertainty conditional on the specified policy formulas. They do not cover future AI effects, needs-scale error or the survey's measurement limits.

## Validation and stopping

Check one-to-one joins, five implicates, roster-size agreement, exact age-18 coding, absence of missing included ages, complete weight joins, nonnegative weights and equal programme totals in every implicate and replicate. Check gross-pass minus after-pass equals the classification gap, and after-pass cannot exceed gross-pass. Test an unequal-size synthetic population with hand-calculated coefficients, a child/adult boundary fixture, top-code exclusion, no-adult rejection, and paired variance. Reproduce the original all-family, constant-payment, constant-floor central result from unchanged inputs as a bridge.

Save the selected public roster fields, source ledger, narrow extracts, data dictionary, all point and replicate estimates, executed checks, and input hashes. Preserve the published S011 code/data/result files. Add one readable section and an estimation appendix to its manuscript, with clear extension status. Finish after this fixed comparison, evidence checks and separate critical review. Do not expand the study in response to a preferred or disappointing ranking.

