# Protocol: Model and platform diversity in essential AI services

Primary state: **Working notes**. Record time: 2026-10-12T10:55:59Z.

## Question and intended contribution

When an essential public service depends on an AI model, do rules that count cloud platforms or model families admit the same pairs of deployments as a rule that requires a remaining candidate after one named model or platform is removed? How does a documented retirement date change those pairs?

This is a purposive document audit and deterministic stress test. It is not a new theory of resilience, an estimate of failure probability, a procurement recommendation, or an experiment on task performance. The economic setting is conditional: households depend on public income or essential provision because human labor cannot earn a competitive wage. The audited products are current examples, not evidence that this setting will occur.

## Prior evidence and exploratory decisions

Discovery has already shown four useful examples: Claude Sonnet 4.5 on Amazon Bedrock and Google Cloud; Amazon Nova Pro on Bedrock; Gemini 2.5 Pro on Google Cloud. It has also revealed a 20 October 2026 retirement notice for the Gemini deployment. The crossed structure and this notice motivated case selection. Therefore the design is exploratory, not a confirmatory test selected without knowledge of the outcome.

Langer and Haag (2026), DOI 10.1007/s11115-026-01021-4, already proposes governance-based routing, provider audit, and sovereign fallback in the public sector. Shelby (2026), arXiv:2607.07359v1, already distinguishes service criticality, substitutability, tested fallback, and concentration. Their full papers were retained and the relevant framework and implementation sections were read. Tan (2026), Zenodo 22918523, already proposes a capacity-constrained economic model; its landing page was read, but the first full-PDF capture failed. Tomlin (2006), DOI 10.1287/mnsc.1060.0515, already studies sourcing and contingency capacity; two full-PDF attempts were denied. Read access limits must remain explicit. The Bank of England's April 2025 AI report supplies institutional context, not proof of this audit's results. No claim of globally new dependency mapping is permitted.

## Corpus and stopping rule

Use exactly the four discovered model/platform deployments. They were chosen for variation in the two visible dimensions, not to represent the market. Include the official model card for each, a platform document when necessary to distinguish the model developer from the service operator, and primary lifecycle material for ambiguous dates. No inference from a missing search result to a missing deployment.

Stop the primary corpus at these four deployment records. Do not add a product because it improves a result. Any later broader sample requires a separate dated plan. Retain failed source acquisitions and discovery-only work. No private contracts, customer accounts, API credentials, or paid inference calls.

## Coding

Unit: a documented deployment of one named model release on one cloud service. Store model label, model developer, platform label, source model identifier, textual lifecycle description, an exact announced retirement date if present, and source passage links. Model equivalence is label-level equivalence; there is no comparison of weights or runtime configurations.

Never use distinct developer or platform labels as proof of statistical independence. Never use shared model identity as measured common failure. No hidden dependency is coded as absent. Task qualification, data access, legal permission for the hypothetical public service, reserved capacity, switching time, and independence of other infrastructure are all unknown. The coding records documentation, not successful deployment.

## Analysis fixed before implementation

Enumerate all unordered pairs from the four records. Evaluate: (a) at least two platform labels; (b) at least two named model labels; (c) at least one surviving candidate under each single-platform exclusion; (d) the same under each single-model exclusion; (e) both classes together. Scenarios deliberately remove every record carrying the named label. These are explicit stress assumptions, not estimated consequences of an incident.

Repeat the candidate calculation after excluding the deployment whose retirement date is at or before 21 October 2026, assuming the announcement is implemented as written and no replacement is installed. The future date is an announced-policy scenario, not an observation of retirement. Report the complete six-pair table, not just favorable cases.

Report structural pass/fail separately from operational continuity, which remains unverified for every pair. Show a sensitivity case in which only the two Claude deployments qualify for the essential task. Also show that a common non-model dependency, if imposed, can defeat every pair. These are assumptions, not empirical findings.

No market share, outage probability, cost calibration, statistical test, welfare total, or superiority estimate will be fitted. A worked benefit-delivery example will explain why a structural pass matters and why it is insufficient.

## Reproduction and review

Separate acquisition from offline enumeration. Retain source bytes privately under the ignored .local-sources/supplier-continuity directory. Publish provenance, hashes, short extracts, coding, exact commands, tests, run metadata, and complete results. Use standard-library Python for offline analysis. A separate AI reviewer must challenge source coding, date interpretation, prior-work overlap, and the main claim before complete-study status.

This document is prospective only for the coding and enumeration not yet done. It does not turn the discovery process into a preregistered experiment.

