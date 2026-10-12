# Buying Backup AI for Essential Public Services
## A case audit of model choice, platform access, and the limits of supplier counts

> **State:** Complete-study draft. **Study:** S013. **Date:** 12 October 2026.
> **Evidence cutoff:** 2026-10-12T13:50:17Z. This covers the retained primary sources used for coding and the last retained prior-work PDF. Current product statements can change.
> **Current-fact recheck:** The five pivotal product/access texts were captured again by 2026-10-12T16:56:31Z. Their extracted text was unchanged; the separate recheck log retains both HTML versions where bytes differed.
> **Disclosure:** AI-assisted research draft. No human review or journal peer review is claimed. Separate AI critical review and independent enumeration are complete.

## Abstract

An income guarantee can depend on an AI service even when its public funding is secure. If households cannot replace a delayed payment with earnings, the availability of a usable backup becomes an economic governance question. This paper audits four deliberately selected model deployments on two cloud platforms. It separates a model's name, its platform, the buyer's access conditions, and evidence that it can perform an essential task. The full comparison covers six possible pairs. In an incumbent-buyer benchmark, three pairs retain a candidate after each named model or platform is excluded. A documented restriction on new access to a legacy model reduces that set to two. Under a separate scenario that applies an announced support-retirement date, one pair remains. These counts describe the selected records and stated exclusions; they do not estimate reliability. All four records lack buyer-specific evidence on six conditions needed for actual service continuity. A public procurement offer and official public-sector case reports show why those conditions cannot be supplied by catalog labels. The contribution is a reproducible case audit of the difference between purchasing variety and establishing a usable fallback.

## 1. The economic problem behind a backup contract

Consider an authority that uses AI to check documents before it authorizes a recurring public benefit. The money is available. The eligible households have been promised payment. A problem with the AI service prevents some checks from completing before the payment deadline. The authority has a second supplier, but that supplier provides the same named model through another cloud. That arrangement can offer an alternative when one platform is unavailable. It cannot meet a rule that prohibits use of that model for the task.

The authority could instead choose two models on one platform. That changes which failure it can address. It does not necessarily improve every aspect of the plan. If the platform becomes inaccessible, both models may be excluded by the stress condition. A third choice is to use different models on different platforms. Even then, the second model may be unavailable to a new customer, approaching the end of support, unable to complete the task, or short of capacity at the time it is needed.

These distinctions matter in the economic setting examined by this research programme. Suppose that AI outcompetes human labor across fields, so competitive wages no longer provide a reliable source of household income. A public payment or essential service then becomes harder to replace through work. This is a conditional premise, not a forecast about technology or employment. It raises the cost of an interruption without proving that every public service should use AI.

The question is narrower than whether public AI ownership, more competition, or additional cloud suppliers improves welfare. It asks what a small set of public documents allows an authority to conclude about specific backup choices. A funding decision and a purchase order establish different things. Funding can pay for a service. A contract can establish access rights and obligations. Neither alone proves that an alternative system can deliver the required service within its deadline.

The worked example is hypothetical. We do not claim that an authority uses any of the four audited products to decide benefits, or that the products are suitable for that purpose. The benefit deadline supplies the reason for testing continuity. The documents supply the candidate relationships and access constraints. The stress cases specify the exclusions.

## 2. What this audit adds to existing work

Multiple models and public fallback capacity are established ideas. Langer and Haag propose a public-sector framework that routes tasks under governance rules. It includes provider assessment, output evaluation, and possible sovereign or on-premises alternatives. We read its framework and implementation sections. The present paper does not introduce that policy menu. It examines a small set of product and procurement records to show what remains to be established before such a menu yields a usable choice. [P1](https://doi.org/10.1007/s11115-026-01021-4)

Shelby's resilience framework distinguishes critical services from the substitutability of their AI components. It treats a fallback as a capability that must be resourced and tested, and identifies shared providers as a concentration concern. We use this distinction to keep the audit's structural results separate from claims about service continuity. We do not infer that a second API is a tested substitute. [P2](https://arxiv.org/abs/2607.07359)

The economic literature also limits the novelty claim. Korinek and Vipra discuss upstream and downstream integration in foundation-model markets, including benefits as well as risks. Their policy discussion includes access and interoperability. We read the November 2024 working-paper sections on integration and policy remedies, rather than treating a later journal citation as evidence of a version we had inspected. That analysis is a reason to distinguish model makers, cloud services, and downstream sellers. It is not a current measurement of the firms audited here. [P6](https://www.nber.org/system/files/working_papers/w33139/w33139.pdf)

Two further leads were screened with access limits. Tomlin's 2006 supplier-risk paper already studies mitigation, rerouting, and capacity. Tan's 2026 portability paper explicitly studies scarce recovery capacity. We obtained their abstracts or repository descriptions but not their full papers in this run: the Tomlin PDF requests were denied and the Tan requests timed out. We make no claim to have checked their proofs. No new economic result about optimal backup capacity is claimed here. [Tomlin](https://doi.org/10.1287/mnsc.1060.0515), [P3](https://zenodo.org/records/22918523)

There is a direct institutional reason for the question. The Bank of England's April 2025 AI report discusses reliance on outside model, data, and cloud services. It identifies a possible transmission from model disruption to time-critical payments. It also distinguishes risks faced by individual firms from those affecting the system. We use that analysis to motivate attention to service delivery; we do not extend financial-sector rules to a hypothetical benefit authority. [P5](https://www.bankofengland.co.uk/financial-stability-in-focus/2025/april-2025)

The contribution is therefore a bounded case audit. It joins named deployment relationships to documented access conditions and reports the entire resulting choice set. It is distinct from this programme's benefit-access study, S007, which holds the payment mechanism available and compares review queues and advance payments. Here the question is whether a proposed AI alternative is still a candidate for use. The audit does not claim that the difference between supplier count and shared dependence is a new theoretical discovery.

## 3. Evidence and selection

The four deployments were chosen during discovery because they vary along the model and platform dimensions. Two list Claude Sonnet 4.5 on different platforms. The other two list a different model on each platform. This is intentional case selection after seeing the relevant structure. It is not a random sample, a complete market inventory, or a selection made without knowledge of the expected counterexample.

The protocol was written before coding and enumeration. A later correction and analysis extension are public. The first run mistakenly coded the AWS Claude record from an older web-reader display. A check of the retained source bytes showed that the card already said Legacy. The linked lifecycle page confirmed the relevant state and access restriction. We corrected the record, preserved the initial run as superseded, and added a new-buyer case. This was a coding error found through source verification, not evidence that the product changed between our two readings.

| Record | Named model | Documented platform | Stage in retained source | Exact end date established |
|---|---|---|---|---|
| A | Claude Sonnet 4.5 | Amazon Bedrock | Legacy | 8 April 2027 |
| B | Claude Sonnet 4.5 | Google Cloud | Generally available | None established |
| C | Nova Pro | Amazon Bedrock | Active | None established |
| D | Gemini 2.5 Pro | Google Cloud | Generally available | Support retirement announced for 20 October 2026 |

Sources: A, [D1](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-4-5.html) and [D6](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html); B, [D2](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/sonnet-4-5); C, [D3](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-pro.html); D, [D4](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro).

The stage labels have different meanings in the source systems. We preserve them instead of treating Active and generally available as equivalent guarantees. For B and C, an earliest possible retirement date does not establish an exact end date. For D, the source footnote concerns support on the Google Cloud platform. We do not apply it to Google's separate Gemini API. The Google URLs redirected to documentation under the Gemini Enterprise Agent Platform name; the original and final URLs are both retained.

A shared model label is also a limited observation. The AWS identifier contains a dated release suffix; the Google card uses a shorter identifier. The cards give different knowledge-cutoff fields. We did not inspect weights or runtime settings. The model-loss stress below therefore removes a named model class by assumption. It does not assert that the two implementations produce identical errors.

The primary sources are retained as original bytes and separate text extractions. The public ledger supplies the retrieval times, hashes, locations, rights notes, and short extracts. Full originals remain in an ignored local directory where full redistribution rights were not established or full publication was unnecessary. The audit uses no private contract, customer account, personal benefit record, or paid API call.

## 4. The public purchase record

A supplier-authored G-Cloud listing makes the institutional distinction concrete. Its seller is Softcat. Its service offers Anthropic's Claude through AWS Bedrock. The listing describes AWS as the service operator and assigns operator access controls to AWS. It also distinguishes shared standard capacity from reserved capacity. These are statements in a public offer, not evidence of a signed call-off contract or verified performance. The listing does not establish that a particular authority has enabled Sonnet 4.5 or secured the capacity needed for a payment deadline. [I1](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/244333610722828)

AWS's own explanation separately states that the Bedrock service team operates model deployment accounts. This supports coding the model developer and deployment operator as different roles. It does not prove that all other inputs are independent of the developer, or that a regional or provider-wide disruption has any particular probability. [D5](https://repost.aws/knowledge-center/amazon-bedrock-model-data-use)

Official public-sector reports also show why a locally controlled alternative cannot simply be assumed to work. The UK AI Playbook describes an NHS user-research tool whose early in-house model did not meet the required output quality within the available development time. A separate NHS review-moderation example describes tests of load, throughput, and startup behavior. These reports concern different tasks; they provide no performance estimate for our four candidates. Their relevance is methodological: task quality and the ability to handle demand require evidence separate from ownership or a product listing. [I2](https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html)

The public record thus supports a distinction between several questions. Who sells the service? Who develops the model? Who operates the deployment? Can this buyer obtain and retain access? Can the deployment complete the essential task with sufficient capacity and within the required time? The audit answers only the parts supported by its documents.

## 5. A complete test of the six choices

With four records, there are six unordered pairs. We evaluate all six. No cost or performance rank is attached to their letters.

The first test asks whether a pair retains at least one candidate when every deployment on one named platform is excluded. The second asks the same question when every deployment carrying one named model label is excluded. A pair passes the combined test only if it passes each single exclusion in both classes.

For example, AB places the same named model on two platforms. It retains a candidate if the stress removes either platform. It retains none if the stress removes Claude Sonnet 4.5. AC has two named models on Bedrock. It passes each single-model exclusion but fails the Bedrock exclusion. These are logical consequences of the stated stress cases. They are not estimates of observed joint failures.

The incumbent benchmark initially includes all four records. This assumes that an existing buyer retains A access. It also leaves task qualification unverified. The result is a candidate screen, not an approval to operate.

| Pair | Two platform labels | Two model labels | Passes each platform exclusion | Passes each model exclusion | Passes both classes |
|---|---:|---:|---:|---:|---:|
| AB | Yes | No | Yes | No | No |
| AC | No | Yes | No | Yes | No |
| AD | Yes | Yes | Yes | Yes | Yes |
| BC | Yes | Yes | Yes | Yes | Yes |
| BD | No | Yes | No | Yes | No |
| CD | Yes | Yes | Yes | Yes | Yes |

Source: executed enumeration in `results/pairs.csv`, incumbent candidate benchmark.

The sets are not interchangeable. Four pairs have two platform labels, while five have two model labels. Three meet both structural conditions. There is no empirical probability attached to any count. Six is the denominator because the selected case contains four records, not because it exhausts the choices facing a real authority.

The difference can reverse a narrow ordering. AB passes the platform-loss test that AC fails. AC passes the model-loss test that AB fails. A buyer cannot rank them by a single count without first specifying the service threat. Once both classes are required, neither passes. This is a comparison of constraint satisfaction, not a welfare or cost ranking.

## 6. Access and the procurement horizon

The documented lifecycle rules change the candidate set before any outage occurs. The retained AWS policy says that new customers cannot use Legacy models. It also states that existing customers may lose access after 15 days of inactivity and that new Provisioned Throughput cannot be created for such models. Its Sonnet 4.5 row identifies affected commercial regions, including us-east-1. We do not infer the same state for unlisted regions or claim to have checked an account through an authenticated API. [D6](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html)

This matters for a backup held mostly unused. Continued appearance in documentation is not enough to establish retained access for an inactive incumbent, and an old working integration is not evidence that a new authority can purchase the same arrangement. The word “may” is material: we do not code inactivity as a certain loss or propose a usage pattern that guarantees continued access.

The new-buyer case applies to an A deployment in a commercial region listed in D6, such as us-east-1. It therefore removes A under the documented rule. The other records are only free of this particular identified exclusion. They are not proven accessible to every new buyer. Two of the six original pairs, BC and CD, pass the combined structural test after that removal.

A second case applies D's announced support-retirement date. It asks which candidates remain on 21 October 2026 if the notice takes effect and the authority requires continued support. It assumes no replacement has been added. This is a procurement-horizon condition, not a prediction that the endpoint will physically stop responding. Under that condition, BC is the only original pair to pass both classes of exclusion.

| Case | Candidates retained by the documentary rule | Pairs passing both exclusion classes |
|---|---|---|
| Incumbent candidate benchmark | A, B, C, D | AD, BC, CD |
| New buyer under the Legacy rule | B, C, D | BC, CD |
| Continued-support scenario for 21 October | A, B, C | BC |
| New buyer and continued-support scenario | B, C | BC |

The full six-pair results remain available for every case, including pairs with an excluded record. Two unknown end dates are not interpreted as perpetual support. The last row therefore identifies a pair that is not excluded by the audited dates and rules; it does not certify a supported contract term or recommend those models for benefits.

## 7. What could overturn the apparent choice

Structural screening is useful because it can reject a proposed arrangement. It cannot supply missing operational evidence. We record six readiness questions for every deployment: task qualification, sufficient reserved capacity, tested switching time, access to current service records, permission for the hypothetical use, and independence of other required infrastructure. All 24 cells are unknown.

The first sensitivity test assumes that only the two Claude deployments meet the essential task's quality threshold. This is not an observed performance result. It shows why the apparently stronger crossed pairs cannot be treated as solutions before testing. Under that assumption, no pair passes both model and platform exclusions. AB still passes the platform test in the incumbent benchmark, but it provides no alternative to the excluded named model.

The second test assumes that every candidate depends on a common service that is lost. It could be a shared identity system, payment-authorisation record, network route, or orchestration layer. No such common dependency is asserted for the four records. Under the imposed condition, every pair fails. The point is that unobserved dependencies cannot be coded as absent merely because platform logos differ.

Capacity is a separate limit. A backup can remain technically reachable while being unable to complete the required workload. The offer's distinction between standard and reserved service does not tell us what an authority bought, what other users demand during stress, or whether priority survives the same event. We therefore estimate neither the number of payments a pair can protect nor an optimal reserve of computation.

Public ownership changes some questions but does not remove these limits. A public fallback could reduce dependence on an outside seller's access decision. It would still need a suitable model, legally usable inputs, functioning computation, maintained records, and tested capacity. A public model on the same cloud can remain exposed to the same platform exclusion. A locally hosted instance of the same model can remain exposed to a decision that rules out that model for the task. These are design implications of the stress definitions, not measurements of public alternatives.

## 8. Implications for an economy without a wage fallback

The relevant economic object is continued access to an entitlement or essential service. The number of purchase relationships is only an intermediate fact. An authority can maintain two invoices while leaving the same decisive dependency in both paths. Conversely, it can retain two technically different paths without establishing that either meets the task's legal and operational requirements.

In the worked benefit example, a failed document check can delay household purchasing power even though the budget has sufficient funds. A household with other liquid assets may bridge that delay. A household that relies on the payment may not. The audit does not estimate those losses, but the difference explains why public buyers should define an acceptable service outcome before choosing a supplier-diversity rule.

The findings support a limited change in procurement assessment. The buyer can ask for a named, versioned alternative and identify the condition under which it must still be available. It can then check access eligibility for the actual buyer and the required support period. Only after those checks does a task and capacity trial answer whether the remaining candidate is a fallback. This sequence avoids treating an untested alternative as evidence that a payment commitment is protected.

There can be real costs. Maintaining several qualified systems uses funds, staff attention, data controls, and computation. Different models may require different validation and can produce different decisions. A broader backup requirement might exclude a cheaper or better-performing single-platform service. It might also be infeasible when only one model meets the task. The present audit provides no basis for assigning those costs a value or requiring maximum variety in every public system.

For governance, an empty validated set should remain visible. It indicates that the proposed service design has no demonstrated fallback under the chosen requirement. It is not a reason to relabel an unknown backup as sufficient. The authority must then change the requirement, redesign the dependence, retain another authorized delivery process, or accept the exposure through a transparent decision. Which response is justified depends on harms, feasibility, and democratic authority beyond this paper's evidence.

## 9. Limits and conclusion

This is a selected four-record audit. Its contribution is the traceable connection between product identity, buyer access, a support horizon, and the limits of the public purchase evidence. It does not establish market-wide concentration, current use by a public authority, failure dependence, cost effectiveness, or a general superiority of public provision.

The source conflict is also a result about method. A web-reader display and retained source bytes can disagree. The incorrect first coding is preserved, and the corrected result uses the retained primary records. Product notices should be checked again for an actual procurement. Their current wording is evidence about the documented offer, not a promise that the same conditions will apply in the future.

Under the audit's explicit assumptions, counting platforms and counting models admit different choices. Documented access and support conditions then reduce the selected set further. None of these screens establishes operational resilience. For an economy in which households depend on public provision instead of wages, the policy task is to connect the service promise to an accessible, qualified, and tested delivery path.

## Reproducibility and responsibility

The package contains the protocol, search and correction logs, source ledger, short evidence extracts, coded records, full scenario outputs, and offline reproduction instructions. Acquisition and analysis are separate. Ten local tests passed after the correction. The superseded first run is retained and labeled unusable as final evidence.

The authoring work, coding, and prose were produced with an AI assistant. No human participant, interview, expert endorsement, affiliation, funding source, or conflict declaration is invented. Responsibility for any later public use or policy decision is not transferred to the tool. A separate AI reviewer checked the source coding and independently enumerated all 36 pair/scenario rows. Both requested revisions were resolved without changing the numerical results. The [critical review](reviews/critical-review.md), [author response](reviews/author-response.md), [final disposition](reviews/review-disposition.md), and [release check](reviews/parent-release.md) state the exact reviewed contents and limits. No human review is claimed.

