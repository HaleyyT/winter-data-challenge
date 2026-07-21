# Australia: economic observations

## Research question

> **Did Australia’s material progress from 2010 to 2024 exceed that of
> comparable countries, and was it accompanied by better labour-market
> conditions?**

This question separates three ideas that should not be conflated: improvement
within Australia, Australia’s latest international position, and whether its
*change* was unusually strong. The analysis is descriptive; it cannot identify
the policies or events that caused the observed changes.

## Method in brief

The economic analysis is implemented directly in
`notebooks/02_analysis.ipynb`, with sensitivity checks in
`notebooks/03_robustness.ipynb`.

- Australia is compared only with countries reporting the same indicator at
  the same exact endpoints.
- The primary period is 2010–24. Income inequality is analysed separately over
  its observed Australian endpoints, 2012–20, because it is periodic rather
  than annual.
- Canada, New Zealand, the United Kingdom and the United States form an
  interpretable English-speaking sensitivity group. All countries in the
  supplied extract with common endpoints form the broad benchmark; this is not
  called an OECD benchmark because the extract includes non-members.
- For lower-is-better outcomes, improvement is sign-oriented for ranking, but
  native-unit changes remain visible.
- Robustness checks use the broad benchmark, normal-status observations only,
  and leave-one-English-speaking-peer-out results. No values are interpolated.

## Main observations

| Indicator | Australia’s change | English-speaking reference | Broad supplied-country reference | Interpretation |
|---|---:|---:|---:|---|
| Household income per person, PPP | +USD 6,004 | +USD 5,218 median (3 peers) | +USD 6,960 median (31 countries) | A substantial domestic gain. It exceeds the small-peer median but not the broad median; the small-peer result changes when individual peers are omitted. |
| Employment rate | +4.82 pp | +5.17 pp median (4 peers) | +5.68 pp median (43 countries) | Employment improved in Australia, but its improvement was not faster than either reference median. |
| Gender wage gap | -3.37 pp | -2.60 pp median (4 peers) | -3.23 pp median (29 countries) | A favourable reduction, with broadly middle-of-the-distribution comparative change. |
| Long-hours share | -3.81 pp | -1.80 pp median (4 peers) | -2.01 pp median (39 countries) | Australia’s improvement is stronger than both benchmarks. Its 2024 level remains above the English-speaking-peer median: 10.18% versus 9.20%. |
| S80/S20 income inequality, 2012–20 | +0.04 | — | — | Essentially flat to slightly worse; the supplied data do not show that average gains were more equally shared. |

## Interpretation

Australia made real material and labour-market progress. The clearest relative
strength is the reduction in long working hours, while the gender wage gap also
narrowed. However, income and employment growth were not consistently stronger
than the broad reference group, and the sparse inequality evidence does not
support a claim that gains were broadly shared.

The most defensible economic headline is therefore:

> **Australia improved materially, with stronger labour-condition progress
> than broad-based economic outperformance.**

## Claim boundaries

- Household income is a national-accounts, PPP-adjusted material-resource
  measure; it is not equivalent to household disposable cash income or wages.
- Employment counts people with at least one hour of paid work, so it does not
  measure job security, job quality, pay, or hours on its own.
- The gender wage gap is unadjusted among full-time employees; it should not be
  interpreted as a causal estimate of discrimination.
- The housing-affordability average is not used as evidence about renter or
  low-income housing stress because it includes imputed owner-occupier rent.
- These comparisons are not causal estimates and should not be reported as
  statistically significant treatment effects.

## Best next step

Use this economic result as the material side of the stronger integrated
question documented in `docs/analysis/health_social_wellbeing_question_assessment.md`:
whether Australia’s material progress coincided with worsening perceived social
support and negative affect relative to comparable countries.
