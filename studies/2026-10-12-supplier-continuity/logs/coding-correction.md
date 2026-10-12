# Correction and additional analysis

Recorded 2026-10-12T12:59:31Z before the corrected analysis.

The first exploratory run used an incorrect Active code for deployment A. The web reader had displayed an older model-card rendition, but the retained D1 bytes already contained Legacy and an 8 April 2027 end-of-life date. This was a coding error, not proof of a change between captures. The linked lifecycle source D6 was then captured and read. It independently lists Sonnet 4.5 as Legacy from 8 October 2026 in named commercial regions and gives the same end date.

The first data, code, tests, results and hashes are preserved in superseded-first-run.json. They must not be used for the final results. The corrected analysis changes the descriptive lifecycle fields and adds new-buyer and combined new-buyer/horizon cases. The original model/platform stress definitions and the four selected deployment records remain unchanged. This is an exploratory protocol extension after the first run, not a prespecified hypothesis.

The added case applies the public rule that new customers cannot use a Legacy model. It does not infer account-specific access, nor treat possible access loss after 15 inactive days as inevitable. The stated model retirement dates remain current-source statements, not future guarantees.
