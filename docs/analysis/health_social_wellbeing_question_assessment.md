# Health, social connection and well-being: evidence assessment

## Decision rule

We assess a candidate question on whether the supplied data directly measure
the construct, coverage and independent observations, an interpretable
comparison, and whether it changes a substantive conclusion. All results are
country-level descriptive comparisons, not causal estimates.

## Results at a glance

| Domain | Australian change | Broad supplied-country comparison | Evidential reading |
|---|---:|---:|---|
| Life expectancy, 2010–23 | +1.3 years | +2.0 years median; ~28th favourable percentile of 46 common-endpoint countries | Australia remains long-lived, but its longevity gain was slower than the broad median. |
| Deaths from suicide, alcohol and drugs, 2010–24 | +7.28 per 100,000 | +3.38 median; ~12th favourable percentile of 18 common-endpoint countries | Serious adverse signal, but thin comparison and combined causes. |
| Lack of social support, 2008–10 to 2023–25 pooled window | +5.12 pp | -0.83 pp median; ~9th favourable percentile of 47 countries | Strong comparative deterioration. |
| Negative affect, 2008–10 to 2023–25 pooled window | +2.61 pp | +0.05 pp median; ~20th favourable percentile of 47 countries | Worsening is materially larger than the typical supplied-country change. |

The social and affect series are six independent three-year Gallup windows.
The final displayed 2024 row represents **2023–25**—it is not an annual 2024
estimate and should not be described as a fully observed post-2024 outcome.

## Candidate research questions

### 1. Recommended: material progress, social connection and affect

> **As Australia’s material conditions improved, did social connection and
> emotional well-being deteriorate relative to comparable countries?**

This is the best final question. It extends the economic analysis with two
outcomes that have complete country coverage and a coherent tension: household
income and employment increased while lack of support more than doubled and
negative affect rose. Australia's deterioration is worse than the broad
reference median for both outcomes.

Use the annual-material protocol for economic indicators and one observation
per pooled social/well-being window; report same-year values, common-window
change, English-speaking peers, all supplied countries, normal-value-only data
and leave-one-peer-out checks. Do not regress six pooled windows as 16 annual
observations or claim that income caused the social outcomes.

### 2. Strong but narrower: a health paradox

> **Did Australia maintain strong longevity while mortality from suicide,
> alcohol and drugs deteriorated relative to comparable countries?**

This is memorable and supported by annual data, but must be a **signal requiring
decomposition**, not a diagnosis: the adverse measure combines three causes and
has only 18 common-endpoint countries. It is a credible secondary figure unless
consistent cause-specific external data are added.

### 3. Social connection alone

> **Has Australia diverged from comparable countries in perceived social
> support?**

This is the cleanest single-outcome social question. Australia has no supplied
time-use observation for social interaction, however, so it measures perceived
support—not social connection in its full behavioural sense. Pairing it with
negative affect strengthens the contribution without asserting causation.

### 4. Subjective well-being alone

> **Has negative affect in Australia risen unusually relative to comparable
> countries?**

Technically sound for negative affect but less compelling alone. Life
satisfaction has only two Australian values (2019 and 2020), so it cannot
triangulate a long-run well-being claim. Use it only alongside social support.

## What the data cannot answer

- They cannot establish material conditions caused social or emotional change.
- They cannot identify which component of suicide/alcohol/drug mortality drove
  the health result.
- They cannot generalise perceived support to loneliness or all social contact.
- They cannot treat life satisfaction as a time trend.

## Reproducible implementation

`notebooks/05_health_social_wellbeing.ipynb` writes auditable health/social/
well-being scorecards and same-year relative trends. It keeps all new analysis
code beside the protocol and interpretation, while reusing the audited loader.
