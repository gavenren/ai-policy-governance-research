# Variables and units

All inputs are synthetic. Population is normalized to one. A period is one year.

| JSON key / result | Meaning | Unit |
| --- | --- | --- |
| n | Recipient population share | Fraction of total residents |
| alpha, beta | Recipient and owner essential expenditure shares | Fraction |
| pi | Reproducible output after operating and replacement costs | Annual reproducible units per total resident |
| q | Essential service supply | Annual essential units per total resident |
| g | Other public uses; includes investment or financing cost when stated | Annual reproducible units per total resident |
| s | Public share of claims on pi | Fraction |
| tau | Tax rate on private claims | Fraction |
| e | Fraction of assessed tax collected | Fraction |
| h, b | Essential and reproducible floors | Annual units per recipient |
| phi | Effective public capture | Fraction of pi |
| revenue | Net transfer budget R | Annual reproducible units per total resident |
| transfer | d=R/n when R is positive | Annual reproducible units per recipient |
| price | Essential price in reproducible units | Reproducible units per essential unit |
| essential, reproducible | x and z | Annual units per recipient |
| essential_total, reproducible_total | Market-clearing checks; second includes g | Annual units per total resident |
| required_capture | Analytic threshold; infinity if impossible | Fraction, may exceed one |
| investment | Additional annual public cost I | Reproducible units per total resident |
| eta | Extra annual essential capacity per annual investment unit | Essential units per reproducible unit |

All rows are retained. There is no sampling, imputation, or missing empirical data. If R is nonpositive, price and market totals are blank because no positive-consumption equilibrium is evaluated. Such a row fails the floor test. Grid counts are not probabilities. The construction-delay rows charge the investment cost with no current capacity gain. They are separate policy states, not a simulated time series.
