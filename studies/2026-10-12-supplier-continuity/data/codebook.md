# Data dictionary and coding record

State: Working notes. Coded by the authoring AI agent from retained primary text. No independent recoding has yet occurred.

Each CSV row is one named model deployment in an official product document. The four cases were chosen before coding because discovery showed variation in model and platform labels. They are not a sample of market share, government use, or all available deployments.

| Field | Meaning |
|---|---|
| deployment_id | Local key A–D. No ordering or quality rank. |
| model_label | Named model class in the product document. Shared labels do not establish identical weights, training data, configurations, or error behavior. |
| developer_label | Model maker named by the source. This is not necessarily the seller or operator. |
| platform_label | Documented API service boundary, grouped as Amazon Bedrock or Google Cloud. It does not certify independent infrastructure. |
| source_model_id | Identifier as displayed in the source. The Google Claude card omits the date suffix used in the AWS identifier. They are grouped only at the named Sonnet 4.5 label. |
| documented_stage | Source's lifecycle or launch-stage label; not a successful API call. Active and GA are different source categories and are not made equivalent measures. |
| exact_support_retirement_date | Exact announced support-end date where present. `unknown` means no exact date established in the audited card. A “no sooner than” date is a lower bound, not an exact end date or a continuing guarantee. |
| source_id; source_locator | Link to sources/manifest.json and the source section. |
| task_qualified | Whether this hypothetical essential task meets an independently established quality threshold; unknown for every row. |
| reserved_capacity | Whether a named authority has purchased and tested sufficient backup capacity; unknown. |
| tested_switching | Whether a switch completes within the service tolerance; unknown. |
| service_data_access | Whether the backup can access necessary current records; unknown. |
| permission_for_hypothetical_use | Whether contracts, law, policy, and credentials permit the proposed use; unknown. No legal conclusion. |
| other_infrastructure_independence | Whether identity, network, orchestration, power, or other dependencies have been checked; unknown. |

Source records D1–D4 are the primary coding evidence. D5 distinguishes the model maker from the Bedrock deployment operator. D6 corroborates the Legacy state, the 8 April 2027 end date, and the new-customer restriction for A. Its regional scope includes us-east-1 and the other commercial regions listed in its Sonnet 4.5 row; no inference is made for unlisted regions. No authenticated regional API call was made. The two Claude cards give different knowledge-cutoff fields (April 2025 and July 2025); that difference is retained as a warning against assuming full implementation identity. Neither field is used to assess quality.

The six readiness fields produce 24 explicitly unknown cells. No value is inferred from silence. There is no missing deployment ID, model label, platform label, source link, or lifecycle label in this selected corpus. Two exact support-end dates remain unknown. Product pages and supplier offers cannot establish actual reserved capacity for a hypothetical buyer.

The stress test deliberately excludes every record with one named model or platform label. This defines the shock. It is not an empirical estimate of correlated failure. A regulator's instruction to stop using a model could fit the first stress; a platform-wide denial of access could fit the second. Neither event is asserted to have occurred.

The later-date scenario removes D because its document announces retirement of support on 20 October 2026. It does not predict a physical endpoint shutdown or apply the date to Google's separate consumer/developer API. Unknown end dates are retained as candidates, not certified to remain supported.

No model output, bill, load test, contract award, private agreement, or public-benefit data was collected.

The incumbent benchmark assumes an existing buyer retains A access. The new-buyer case applies to an A deployment in a commercial region listed in D6, such as us-east-1. It excludes A under the documented Legacy rule. The region is a condition of this scenario, not a claim that every A deployment has the same state. The other rows merely lack this identified exclusion; they are not proven accessible to a new buyer. Possible loss of legacy access after 15 days of inactivity is reported as a condition for further checking, not coded as certain loss. Each run keeps all six pairs, including those with a removed candidate.

