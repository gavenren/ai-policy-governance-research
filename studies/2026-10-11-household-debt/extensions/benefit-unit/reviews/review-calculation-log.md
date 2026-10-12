# Independent review calculation log

The first independent run failed its comparison before saving a passing result. It used ordinary sequential floating-point sums to fit the constant family payment. In some samples, the computed amount was just below $2,000. A strict threshold comparison then misclassified exact ties. This was an error in the independent check, not a change to the paper's policy rule.

The corrected review calculation sets the family coefficient to exactly $2,000, as the budget identity requires. It uses accurate summation for the other rate coefficients. It retains strict threshold comparisons. The author implementation instead uses a $0.00000001 threshold tolerance. The second run checks whether these two independent treatments agree for every reported statistic. The initial mismatch affected 138 of 960 implicate statistics; no passing review was claimed from that run.

During review, the author added source E5 and clarified the README state. Those changes do not change analysis inputs or outcomes. The reviewed-hashes file identifies the revised snapshot used for the second run.
