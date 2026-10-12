# Decisions and failed runs

2026-10-11, after the internal design freeze, before the first successful outcome run: the initial full run stopped at its replicate-weight check. The code wrongly treated missing replicate cells as an incomplete family join. All family identifiers in fact matched. There were 1,203,591 missing weight cells and the same number of missing multiplicity cells, with matching missingness patterns. The official SCF codebook, the input construction immediately after MACRO MEANIT, explicitly sets these missing values to zero because those families were not drawn in that replicate. The implementation now follows that instruction. No survey family was dropped. No result had been written by the failed run.

The saved protocol remains unchanged so its design-freeze hash is verifiable. This clarification implements the stated official sampling method; it does not change the estimand or select a favorable result.

2026-10-11, separate methods review after the first results: the reviewer identified that TPAY includes constructed payments (credit cards, buy-now-pay-later and margin debt), omits payments on the residual other-loan category, and can include mortgage escrow. The manuscript now calls TPAY a payment-burden proxy and makes the contract-policy interpretation conditional. No empirical values changed. The saved-replicate run metadata now says that the original weight join was not rerun. Influence output names its displayed cap as the first-implicate cap and states that each implicate has its own cap. The internally frozen protocol retains its earlier wording as part of the history.

## Source-package completion, 2026-10-12T06:52:22Z

The source package now retains 14 records and public evidence extracts. D3 and D4 use selected public-domain Board method passages; other prior research uses short quotes and researcher summaries. P3 and P5 remain abstract-only after blocked PDF requests. P6 was retained as original HTML at 2026-10-11T21:42:56Z, which is the retrieval cutoff. Source interpretation and review continued later. This does not retrospectively change the design-freeze timestamp.

The new acquisition script was run on 2026-10-12 into a new ignored capture directory. D1, D2 and D8 matched all pinned archive/workbook hashes before extraction. Both official workbook cells were then checked by the standalone benchmark script. The source validator checked 14 public extracts and 21 original/extracted local representations. These checks establish retained-byte consistency, not novelty or causal validity.
