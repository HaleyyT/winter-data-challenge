# Australia: material progress, social support and emotional well-being

## Purpose and recommended framing

This note provides report-ready language and a traceable hand-off for the
Australia analysis. It is deliberately separate from the shared submission
report so that the team can incorporate the material after its current edits
are complete.

The analysis addresses the following descriptive research question:

> As Australia's material conditions improved, did perceived social support and
> emotional well-being deteriorate relative to countries with the same observed
> endpoints in the supplied OECD extract?

The evidence is consistent with a material--social tension. It does not
identify a causal effect of income or employment on social support or negative
affect. The appropriate conclusion is that these outcomes moved in opposite
directions over the observed periods, and that Australia's adverse social
changes were larger than those of the typical eligible comparator.

## Data preparation and analytical scope

The analysis uses the supplied OECD Current Well-being extract without
modifying the raw file. The audited tidy data contain one observation per
country, indicator and displayed year; duplicate keys and missing observed
values are rejected before analysis. Source units and observation-status flags
are retained. No values are imputed and no absent years are interpolated.

The four pre-specified primary outcomes are:

| Domain | Outcome | Direction regarded as favourable | Comparison period |
|---|---|---:|---|
| Material conditions | Household income per person, PPP | Higher | 2010–2024 |
| Material conditions | Employment rate | Higher | 2010–2024 |
| Social connection | Lack of social support | Lower | 2008–10 to 2023–25 pooled windows |
| Emotional well-being | Negative affect | Lower | 2008–10 to 2023–25 pooled windows |

Income and employment are annual measures. The two Gallup outcomes are six
independent three-year pooled windows; their displayed annual rows are not
treated as separate yearly measurements. In figures, the pooled windows are
shown at their midpoints (2009, 2012, 2015, 2018, 2021 and 2024) but labelled
with the underlying three-year windows.

For every outcome, the broad reference group comprises only countries in the
supplied extract that report both of Australia's exact endpoints. It is
therefore described as the *supplied-country reference*, rather than as the
OECD. Its composition may vary by outcome and period. Native-unit changes are
kept for substantive interpretation. Direction-oriented changes and percentiles
are used only to make the direction of favourable change comparable across
higher-is-better and lower-is-better outcomes.

## Report-ready findings

### Material conditions improved domestically

Australia's household income per person rose from USD 44,625 in 2010 to USD
50,629 in 2024, an increase of approximately USD 6,004. Employment increased
from 75.44% to 80.26%, a gain of 4.82 percentage points. These are meaningful
domestic improvements in the material outcomes considered here.

However, the comparative evidence does not support a claim that Australia
outperformed the typical eligible country on those changes. Among countries
with the same endpoints, the median income increase was approximately USD
6,960 (31 eligible comparators), and the median employment increase was 5.68
percentage points (43 eligible comparators).

### Social support and emotional well-being deteriorated comparatively

Over the independent Gallup windows, Australia's reported lack of social
support increased from 4.93% in 2008–10 to 10.04% in 2023–25: a 5.12
percentage-point adverse change. The supplied-country median changed in the
favourable direction by 0.83 points. Australia was at approximately the ninth
favourable percentile among the 47 countries with both endpoints.

Negative affect increased from 12.24% to 14.85% over the same pooled windows,
an adverse change of 2.61 percentage points. The supplied-country median
change was close to zero (+0.05 points). Australia was at approximately the
20th favourable percentile among the 47 countries with both endpoints.

Taken together, these findings support a carefully bounded descriptive result:
Australia became materially better resourced between 2010 and 2024, while both
perceived social support and negative affect moved adversely relative to the
eligible supplied-country reference. The results should not be interpreted as
evidence that material progress caused the social and emotional changes.

## Limitations and unresolved data-quality considerations

- **Descriptive, not causal:** country-level trends cannot establish a causal
  relationship between material conditions and social or emotional well-being.
- **Changing reference composition:** the set of reporting countries can vary
  across outcomes and plotted periods, especially for income. Counts are shown
  in the figure and exact common-endpoint rules are used for the scorecard, but
  comparisons remain conditional on available data.
- **Pooled social outcomes:** the 2023–25 endpoint includes 2025 and is not an
  annual 2024 observation. Pooled windows reduce false annual precision but
  also limit the number of independent time points.
- **Construct coverage:** lack of social support is not a complete measure of
  social connection. The extract does not provide a sufficiently comparable
  Australian time series of social interaction for the primary analysis.
- **Outcome interpretation:** PPP-adjusted income per person is a
  national-accounts measure and not household disposable cash income.
  Employment measures jobholding, rather than job security, working hours, pay
  or job quality.
- **Cross-country comparability:** survey design, source systems and
  observation-status flags can differ between countries. The analysis retains
  those flags rather than silently excluding them; a normal-status-only
  sensitivity remains appropriate for the final robustness stage.
- **Scope of inference:** results apply only to countries, outcomes and periods
  available in the supplied extract. They should not be generalised to all OECD
  members or to unobserved population groups.

## Traceable results, outputs and implementation

| Item | Purpose | Location |
|---|---|---|
| Audited loading and metadata | Validates raw structure; preserves units, status flags, directions, frequencies and caveats | `src/oecd_audit.py` |
| Data audit | Documents input scope, quality checks and coverage | `notebooks/00_data_audit.ipynb` |
| Comparative exploratory figure | Recreates the four-panel Australia/reference trajectory figure with IQRs and reporting-country counts | `notebooks/04_final_visuals.ipynb` |
| Final trajectory figure | 300 dpi figure for the report/presentation | `reports/figures/material_social_trajectories.png` |
| Figure coverage table | Reporting-country count at every plotted period | `reports/tables/material_social_trajectory_coverage.csv` |
| Common-endpoint analysis | Recreates the four-outcome scorecard, direct endpoint audit and CSV round-trip check | `notebooks/02_analysis.ipynb` |
| Frozen primary results | Four-outcome, 18-column table with native changes, direction-oriented gaps, percentiles and comparator counts | `reports/tables/material_social_primary_results.csv` |
| Quarto report source | Reproduces and checks the frozen primary table at render time | `submission/australia_material_social_report.qmd` |
| Method completion evidence | Definition-of-done checklist for Methods 1 and 2 | `docs/planning/day-2/next_steps_checklist.md` |
| Automated checks | Tests for raw-data keys, pooled periods and comparative calculations | `tests/test_oecd_audit.py` |

The figure and table outputs are generated artefacts and may be ignored by Git;
they should be regenerated from the listed notebooks before final submission.
The verified Method 1–2 versions of the notebooks, report source and checklist
are on the `haley-b` branch.

## Suggested integration points for the shared report

1. Use **Purpose and recommended framing** for the research-question and
   interpretation paragraphs.
2. Use **Data preparation and analytical scope** in the data/methods section.
3. Use the two **Report-ready findings** subsections in the findings section,
   retaining the no-causality wording.
4. Add **Limitations and unresolved data-quality considerations** as a distinct
   limitations section rather than embedding caveats only in captions.
5. Use the traceability table during final team review to confirm that every
   reported number and graphic comes from a reproducible output.
