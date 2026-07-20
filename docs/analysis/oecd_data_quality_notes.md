# OECD data quality and comparability notes

## What was checked

The supplied `data/raw/OECD Data.csv` contains **8,806 observations, 47 countries, 21 indicators and 10 domains**. The key `(country, indicator, year)` is unique and `OBS_VALUE` has no missing values. All rows are national totals for age, sex and education; the file therefore cannot directly study within-country subgroup inequality.

No raw rows were deleted, changed, interpolated or imputed. `src/oecd_audit.py` creates a tidy analysis copy and auditable tables for:

- country-indicator coverage and internal calendar gaps;
- independent periods for pooled survey indicators;
- indicator counts available for every country-year;
- Australia comparisons using only countries reporting the same indicator in the same year;
- OECD status flags and indicator-specific caveats.

Run it from the repository root with:

```bash
python -m src.oecd_audit
```

## Gaps and uneven timing

Australia has 187 rows across 17 of the 21 indicators. It has no observations for overcrowding, time off, the gender gap in working hours, or time spent in social interactions. Its annual series for income, employment, long hours, housing affordability, life expectancy, deaths from suicide/alcohol/drugs, air pollution and extreme temperature have no internal gaps within their observed spans.

Blank years in non-annual measures are not automatically missing data:

- income inequality: 2012, 2014, 2016, 2018 and 2020;
- median wealth: 2012, 2014, 2018 and 2020;
- PISA mathematics: 2012, 2015, 2018 and 2022;
- political voice: 2021 and 2023;
- voter turnout: election years only;
- life satisfaction: only 2019 and 2020.

Lack of social support and negative affect appear annually, but OECD defines them as pooled survey windows. Repeated values within 2011-13, 2014-16, 2017-19, 2020-22 and 2023-25 are **the same estimate**, not independent annual observations. The cleaning code collapses these to six independent Australian periods, including 2008-10 represented by the 2010 row.

The challenge describes data through 2024, but the supplied file includes 224 rows labelled 2025 and seven voter-turnout rows labelled 2026. The primary exploration is capped at 2024; later rows should be a clearly labelled sensitivity update.

## Same-year comparison rule

An Australian value is compared only with countries having the same indicator and year. Every output reports the comparison count; comparisons with fewer than 20 countries are marked thin. “Latest available by country” values must not be ranked together because they can represent different years, survey windows or elections.

The 47-country file also contains non-OECD countries. Results are therefore called **supplied-country comparisons**, not OECD rankings, unless an OECD-member list is applied explicitly.

## Status flags

There are 8,540 normal observations and 266 flagged observations: 40 time-series breaks (`B`), 45 differing definitions (`D`), 92 estimates (`E`) and 89 provisional values (`P`). All Australian rows are marked normal, but same-year peers can still be flagged. A robustness analysis should repeat comparisons after excluding all non-`A` rows.

## Indicators needing careful interpretation

| Indicator | Main comparability issue | Required handling |
|---|---|---|
| Household income | National-accounts income includes social transfers in kind; PPP-adjusted level is not household cash income | Interpret as real material resources, not wages or disposable cash alone |
| S80/S20 income ratio | Survey/administrative sources differ and both distribution tails can be under-covered | Use direction and broad effect sizes; avoid over-reading small rank differences |
| Median wealth | Per household, excludes private/occupational pensions, no household-size adjustment, sparse years | Do not treat as annual or combine mechanically with per-capita income |
| Employment rate | One hour of paid work qualifies as employed | Pair with long-hours/job-quality evidence; do not equate employment with good work |
| Gender wage gap | Unadjusted median gap for full-time employees | Describe disparity, not a causal estimate of discrimination |
| Long paid hours | Threshold and survey definitions can vary | Compare direction and magnitude, with status-flag sensitivity |
| Housing affordability | National average includes imputed owner-occupier rent and different COICOP versions | Cannot answer whether renters or low-income households face housing stress |
| Life expectancy | Hypothetical period measure based on current mortality rates | Do not call it the predicted lifespan of a birth cohort |
| Suicide/alcohol/drug deaths | Cause coding differs; three causes are combined | Treat the rise as a signal requiring decomposition, not a diagnosis |
| PISA mathematics | Enrolled 15-year-olds only; non-annual cycles and changing testing conditions | Compare common PISA years; exclude dropouts/home-schoolers from the population claim |
| Lack of social support | About 1,000 Gallup respondents per country/year; 3-year pooled estimates repeated on annual rows | Collapse to independent pooled windows; do not fit a 16-point annual trend |
| Political voice | Only two Australian Trust Survey waves | Present as suggestive, not a stable time trend |
| Voter turnout | Different election cycles/types; Australia has compulsory voting | Do not use raw turnout rank as evidence Australia is more civically engaged |
| Air-pollution exposure | Threshold measure saturates near 100% | It cannot distinguish how far concentrations exceed the threshold |
| Extreme-temperature exposure | Strong structural climate/geography differences and annual volatility | Use multi-year patterns, not a single-year country rank |
| Life satisfaction | Wording, anchors, sampled ages and survey methods differ; only two Australian rows | Unsuitable as the primary cross-country trend outcome in this extract |
| Negative affect | Gallup 3-year pooled estimates repeated on annual rows | Collapse pooled windows and interpret small differences cautiously |

The detailed machine-readable map for all 21 indicators is generated at `reports/tables/indicator_metadata.csv`. Definition pages refer to the supplied *OECD How's Life? Well-being Database: Definitions and Metadata* PDF.
