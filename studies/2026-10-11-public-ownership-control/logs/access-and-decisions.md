# Access attempts, exclusions, and revisions

The source capture log is a transport record. A successful response there does not mean that the response was suitable evidence. Inclusion and source status are set by the manifest and instrument ledger.

| Capture | Decision | Reason |
| --- | --- | --- |
| AK1, AK4 | Exclude | Legislative statute index returned, without the requested substantive provisions. |
| AK3 | Exclude | Small request-rejection body, initially stored as a successful response. Replaced by identified primary-page reader capture A1. |
| NZ1 | Exclude | Empty body, initially stored as a successful response. Later acquisition guard rejects empty or short responses. |
| AK6 | Exclude from current claims | Download was the 2020 statute extract despite the exploratory request title. It does not verify 2026 law. |
| AK7, AK10 | Exclude | Guessed paths returned 404. Current Alaska policies were later found through the official governance page and downloaded as AK11 and AK12. |
| NO1–NO7 | Direct acquisition failed | HTTP 403. Verified-TLS direct attempts also failed. The current linked framework was read through the primary-page reader, whose output is hashed as its own representation. |
| NZ2, NZ5, NZ8 | Substantive statute unavailable | Official whole-text and PDF requests returned empty or blocked responses. The code therefore uses narrower official fund descriptions. NZ8 was a separate empty command-line response, not an analytic source. |
| AK2, AK8 | Discovery/corroboration only | Used to locate the current governance documents. Main claims cite the documents themselves. |
| NZ7 | Not coded | Independent review acquired, but no fund-performance claim was retained. |
| L5 | Discovery only | Recent article's publisher search text screened; direct full article and PDF returned 403. No result or legal claim depends on it. |
| NZV | Discovery only | Official version heading and amendment heading found, but no complete amendment list or whole current statute verified. |

The first reader captures were saved as combined text. Their request seconds were not retained. The six institutional pages were therefore fetched again in a measured request sequence from **2026-10-11T21:34:27Z to 21:34:32Z**. Their manifest entries now identify separate reader files, exact request start and completion times, and source URLs. Earlier captures remain in the ignored local source directory. No hash of reader output is presented as a PDF hash.

The following revisions occurred before review:

- The Norwegian case was changed to the September 2026 mandate and the November 2025 interim ethical rules. The earlier formal exclusion route was not carried forward as if unchanged.
- The Alaska investment policy was read visually after its text extraction failed to yield prose. Its amendment and effective dates are reported exactly as printed, with no claim about retroactive effect.
- The Alaska public-comment locator was corrected to bylaws Article III section 2, page 8. Section 10 concerns political activities and was an erroneous draft locator.
- The captured New Zealand ownership page supported the use of voting and proxy guidelines, but did not contain the more specific voting-execution statement initially considered. The manuscript was narrowed to the captured text.
- The latest Norwegian mandate expressly calls its English text unofficial and unauthorised. The manuscript and instrument ledger now preserve that limit.
- The proposed novelty statement was narrowed after reading Stout and Gramitto. Their design already combines income and ownership voice. The paper retains an application about remedy scope and a conditional argument against withholding subsistence for non-participation.

These are evidence and scope corrections, not changes in observed fund performance. No source conflict was resolved by silently discarding a contrary result.
