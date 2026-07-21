# Haley work already incorporated into the report

## Purpose

This file records Haley's completed implementation and the material already
incorporated into `submission/australia_material_social_report.qmd`. It is a
traceability note for team review, not a second report. The quoted passages
below reproduce the report wording exactly as it appears on `haley-b`.

## Where Haley's work appears in the report

| Report location | Haley material represented there |
|---|---|
| **Data cleaning and preprocessing → Audit safeguards for the research question** | The essential no-imputation, duplicate-key, same-year and pooled-period safeguards |
| **Exploratory analysis and question selection → Development of the research question** | Coverage-led selection of the material--social question and exclusion of life satisfaction as a primary long-run outcome |
| **Methodology → Method 1: EDA** | Same-period supplied-country reference, annual versus pooled outcomes, direction-aware interpretation and four pre-specified primary outcomes |
| **Methodology → Method 2: Primary common-endpoint comparison** | Exact common-endpoint eligibility, comparator counts, native changes, direction-oriented gaps and non-causal interpretation |
| **Analysis and results → Findings** | Material improvement, comparative underperformance on the two primary material changes, adverse social changes and the material--social synthesis |
| **Conclusion** | The bounded answer to the research question and explicit causal boundary |
| **Limitations → Limitations and claim boundaries** | Changing comparator composition, survey/source differences, quality flags, pooled-window timing and construct limitations |
| **Appendix → Audit traceability** | Detailed audit outputs, coverage limitations, quality-flag handling and the relationship between the full audit copy and primary report scope |
| **Economic comparison table and trajectory graph** | Responsive table widths, expanded interpretation column, alternating row styling and graph scaling that prevents clipping |

## Exact report text added for the cleaning audit

### Audit safeguards for the research question

The reproducible audit in `src/oecd_audit.py` revalidates the unchanged raw
file and rejects missing required values, duplicate keys and undocumented
indicators; no values are imputed. It also prevents the two main comparison
errors: countries are compared only within the same indicator and year, and 16
displayed social rows are treated as six independent pooled windows. Income and
employment have no internal Australian annual gaps. These safeguards support
the four-outcome design; detailed audit outputs and coverage limitations are in
the Appendix.

## Exact audit support moved to the Appendix

### Audit traceability

The audit copy retains all 8,806 supplied observations and adds quality flags,
favourable directions and independent-period labels. Applying the report's
2010--2024 scope yields the same 8,575 observations used by the team analysis.

| Audit control and output | How it protects the analysis |
|---|---|
| Gap and coverage tables: `time_series_gaps.csv`, `coverage_by_country_indicator.csv`, `coverage_by_country_year.csv` | Separate genuine annual gaps from scheduled non-annual measurement and report the evidence available for each series |
| `indicator_metadata.csv` | Records units, direction, frequency and comparability caveats so unlike constructs are not treated as equivalent |
| `same_year_australia_comparisons.csv` and `australia_indicator_summary.csv` | Compare Australia only with countries observed for the same indicator and year, report comparator counts and support transparent outcome selection |
| `domain_coverage_all.csv` and `domain_coverage_australia.csv` | Count unique country--indicator--period evidence; ranks indicate availability, not substantive importance |

Australia covers 17 of 21 indicators but lacks time spent in social
interactions, so lack of social support is a focused proxy rather than a
complete social-connection measure. Australian rows have normal OECD status;
peer flags remain visible for sensitivity analysis. Indicator-specific caveats
are documented in `docs/analysis/oecd_data_quality_notes.md`.

## Exact report text added for Method 1

### Method 1: EDA

The four primary outcomes were fixed after the coverage audit and before the
common-endpoint comparison. For each observed period, Australia is plotted in
native units against the median and interquartile range of all other supplied
countries reporting that outcome in the same period. Australia is excluded from
the reference summaries; no values are interpolated and no composite score is
constructed. Reference coverage is 31--36 countries for income, 44--46 for
employment and 46 for each social outcome.

Income and employment are annual. Lack of social support and negative affect
are six independent three-year Gallup windows labelled by their full periods.
The per-period reference composition may change with reporting availability, so
Method 1 establishes patterns and coverage rather than a fixed-panel estimate.
The supplied extract includes non-members and is therefore described as the
*supplied-country reference*, not as an OECD ranking.

## Exact report text added for Method 2

### Method 2: Primary common-endpoint comparison

For each outcome, a country is eligible only if it reports both of Australia's
exact endpoints. The native change is
$\Delta_c = y_{c,\mathrm{end}}-y_{c,\mathrm{start}}$. The primary comparative
estimand is $G=s(\Delta_{AUS}-\operatorname{median}(\Delta_c))$, where
$s=1$ for higher-is-better outcomes and $s=-1$ for lower-is-better outcomes.
Thus, positive $G$ always indicates a more favourable Australian change. The
median limits sensitivity to extreme country changes, while native units retain
substantive meaning.

The scorecard also reports the eligible-country count and Australia's
direction-aware percentile, using average ranks for ties. Percentiles describe
relative position; they are not probabilities or significance tests. Rendering
stops if these results differ from the independently generated Method 2 table.
Methods 3--4 assess uncertainty and trend robustness separately.

## Exact primary finding refinements

- Household income per person rose **USD 6,004** from 2010 to 2024. This is a
  substantial domestic gain, but **USD 956 below** the median rise of USD 6,960
  among 31 eligible comparators (about the **45th favourable percentile**).
- Employment increased **4.82 percentage points**, below the broad-reference
  median rise of 5.68 points by **0.86 points** among 43 eligible comparators
  (about the **37th favourable percentile**).
- Lack of social support rose from **4.93%** in 2008–10 to **10.04%** in the
  2023–25 pooled window: a **5.12-point adverse change**. The broad-reference
  median also worsened, but by only 0.83 points. Australia therefore
  deteriorated **4.29 points more** and placed at about the **9th favourable
  percentile** of 47 common-endpoint countries.
- Negative affect rose from **12.24%** to **14.85%** across the same windows:
  a **2.61-point adverse change**. The broad-reference median slightly improved
  by 0.05 points, so Australia deteriorated **2.66 points more** and placed at
  about the **20th favourable percentile**.

## Exact report synthesis added after the primary findings

Australia improved materially, but less than the typical eligible comparator
on the two primary material changes. Both social outcomes deteriorated more
than their comparator medians. This supports a descriptive material--social
tension, not a causal effect.

## Exact conclusion added to the report

Household income and employment increased, but by less than the median changes
among countries with the same endpoints. Meanwhile, perceived lack of social
support and negative affect worsened more than their typical eligible
comparators. Within the supplied data, Australia therefore became materially
better resourced while its measured social and emotional outcomes deteriorated
comparatively. This is a descriptive conclusion; causal explanations require a
different design.

## Exact limitations added to the report

- The eligible reference group changes across outcomes and plotted periods as
  reporting coverage changes. All comparisons are therefore conditional on the
  countries observed at the required endpoints, rather than a fixed OECD panel.
- Survey design, source systems and observation-status flags may differ across
  countries. These flags are retained for transparent sensitivity analysis,
  but they limit claims of perfect cross-country comparability.

## Earlier Haley analysis already represented in the shared report

The following report components were already present when the final traceability
pass was made. They originate from, or directly implement, Haley's earlier
analysis hand-off in commit `5b7e90a` and the Method 1--2 implementation on
`haley-b`:

- the focused material--social research question;
- the distinction between annual economic data and six independent pooled
  social survey windows;
- the same-period supplied-country reference rather than an unsupported
  blanket "OECD ranking" label;
- the four primary outcomes: household income, employment, lack of social
  support and negative affect;
- the common-endpoint results for Australia and eligible comparators;
- the material findings for income and employment;
- the adverse social findings for lack of social support and negative affect;
- the exclusion of life satisfaction as a primary long-run outcome because
  Australia has only two observations;
- the descriptive-not-causal framing and primary construct limitations.

## Haley implementation inventory

### Main implementation

| File | Completed purpose |
|---|---|
| `src/oecd_audit.py` | Validates the supplied raw schema and keys; creates the tidy audit copy; assigns favourable direction, quality flags and independent periods; builds all gap, coverage, metadata, comparison and Australia-summary outputs |
| `tests/test_oecd_audit.py` | Automated checks for raw-data keys, pooled periods and comparative calculations |
| `notebooks/00_data_audit.ipynb` | Self-contained cleaning and data-quality notebook, with Yilin's work retained before Haley's labelled audit section |
| `notebooks/01_eda.ipynb` | Economic and social exploration used to scope the main question and interpret indicator direction correctly |
| `notebooks/02_analysis.ipynb` | Reproducible four-outcome common-endpoint analysis and frozen Method 2 result export |
| `notebooks/04_final_visuals.ipynb` | Reproducible Method 1 trajectory figure and coverage export |

### Cleaning and audit outputs

| File | Completed purpose |
|---|---|
| `data/processed/oecd_clean.csv` | Cleaned, validated analysis copy with direction, quality and independent-period fields |
| `reports/tables/time_series_gaps.csv` | Identifies internal calendar gaps while distinguishing annual gaps from non-annual designs |
| `reports/tables/coverage_by_country_indicator.csv` | Summarises years, independent periods, distinct values and quality flags for every country-indicator series |
| `reports/tables/coverage_by_country_year.csv` | Counts available indicators and flagged observations for every country-year |
| `reports/tables/indicator_metadata.csv` | Documents definitions, direction, frequency, coverage and comparability limitations for all 21 indicators |
| `reports/tables/same_year_australia_comparisons.csv` | Compares Australia with countries reporting the same indicator in the same displayed year |
| `reports/tables/australia_indicator_summary.csv` | Summarises Australia's independent-period change and latest same-year international position |
| `reports/tables/domain_coverage_all.csv` | Ranks domains by available independent evidence across the supplied data, not by importance |
| `reports/tables/domain_coverage_australia.csv` | Reports Australian domain coverage without overcounting repeated pooled estimates |

### Method 1--2 outputs

| File | Completed purpose |
|---|---|
| `reports/figures/material_social_trajectories.png` | Four-panel Australia/reference trajectory figure with reference medians, interquartile ranges, reporting-country counts and pooled-window labels |
| `reports/tables/material_social_trajectory_coverage.csv` | Exact contributing-country count for every plotted indicator-period |
| `reports/tables/material_social_primary_results.csv` | Frozen four-outcome Method 2 table containing native changes, oriented gaps, favourable percentiles and comparator counts |

### Interpretation and planning documents

| File | Completed purpose |
|---|---|
| `docs/analysis/oecd_data_quality_notes.md` | Human-readable treatment of gaps, pooled periods, status flags and indicator-specific comparability caveats |
| `docs/analysis/oecd_exploration_and_questions.md` | Evidence summary, research-question selection and appropriately bounded interpretation |
| `docs/planning/day-2/next_steps_checklist.md` | Definition-of-done record for the completed Method 1 and Method 2 tasks |
| `submission/australia_material_social_report.qmd` | Reproducible source containing the integrated Haley methodology, evidence and limitations |
| `submission/australia_material_social_report.html` | Rendered team report containing the same integrated material |

## Presentation implementation already applied

- The economics comparison table is constrained to the report text column and
  cannot overflow horizontally.
- The table allocates 42% of its width to interpretation and compresses columns
  containing shorter numerical comparisons.
- Numeric comparison columns are right-aligned, cells use consistent spacing,
  and alternating rows receive subtle shading.
- The four-panel trajectory graph is scaled to 100% of the report column while
  retaining its aspect ratio, so no right-hand panel is clipped or covered.

Exact presentation CSS in the report:

```css
.economic-comparison {
  margin: 1.25rem 0 1.75rem;
  width: 100%;
  max-width: 100%;
}

.economic-comparison table {
  width: 100%;
  table-layout: fixed;
  font-size: 0.88rem;
}

.economic-comparison th,
.economic-comparison td {
  padding: 0.8rem 0.7rem;
  vertical-align: top;
  line-height: 1.45;
}

.economic-comparison th {
  border-bottom: 2px solid #6c757d;
  font-weight: 650;
}

.economic-comparison tbody tr:nth-child(even) {
  background-color: #f6f8fa;
}

.economic-comparison th:nth-child(1),
.economic-comparison td:nth-child(1) { width: 16%; }
.economic-comparison th:nth-child(2),
.economic-comparison td:nth-child(2) { width: 11%; text-align: right; }
.economic-comparison th:nth-child(3),
.economic-comparison td:nth-child(3) { width: 16%; text-align: right; }
.economic-comparison th:nth-child(4),
.economic-comparison td:nth-child(4) { width: 17%; text-align: right; }
.economic-comparison th:nth-child(5),
.economic-comparison td:nth-child(5) { width: 40%; text-align: left; }

.economic-comparison col:nth-child(1) { width: 15% !important; }
.economic-comparison col:nth-child(2) { width: 12% !important; }
.economic-comparison col:nth-child(3) { width: 15% !important; }
.economic-comparison col:nth-child(4) { width: 16% !important; }
.economic-comparison col:nth-child(5) { width: 42% !important; }

.trajectory-figure img {
  display: block;
  width: 100%;
  max-width: 100%;
  height: auto;
  margin: 0 auto;
}

.primary-scorecard table {
  width: 100%;
  table-layout: fixed;
  font-size: 0.82rem;
}

.primary-scorecard th,
.primary-scorecard td {
  padding: 0.5rem 0.45rem;
  vertical-align: top;
  white-space: normal;
}

.primary-scorecard th:first-child,
.primary-scorecard td:first-child { width: 24%; text-align: left; }

.primary-scorecard th:not(:first-child),
.primary-scorecard td:not(:first-child) { text-align: right; }
```

## Method 1--2 report verification added in this pass

- The Method 2 scorecard is recomputed from the cleaned data during rendering
  and checked against `material_social_primary_results.csv` for both endpoints,
  Australia's native change, the comparator median, the direction-oriented gap,
  favourable percentile and eligible-comparator count.
- Rendering stops when the frozen Method 2 output is absent or any checked
  value differs, preventing stale narrative metrics from entering the report.
- The trajectory figure is loaded from the executed Method 1 visual notebook;
  rendering verifies 15 annual periods for both material outcomes and six
  independent pooled periods for both social outcomes.
- The compact scorecard removes row indices, labels its native-unit scale and
  retains the six fields needed to assess magnitude, direction and coverage.

## Verification record

- Audit pipeline result: **8,806 rows, 47 countries, 21 indicators and 266
  flagged observations validated**.
- Primary report scope: **8,575 observations through 2024**, including 8,321
  normal and 254 flagged observations.
- Automated tests: **5 passed**.
- Quarto report: **rendered successfully**.
- Visual layout check at a 1280-pixel viewport: table aligned left and right
  with the text column, no table overflow, and the trajectory image fully
  contained within its report column.

## Relevant commits on `haley-b`

- `34ba9a3` — `fix: make primary analysis reproducible and report-ready`
- `826ddf3` — `docs: integrate Haley analysis into team report`
- `bb077ca` — `docs: connect audit evidence to the research design`
- `24f1647` — `style: align report table and trajectory figure`

Methods 3 and 4 are not implemented by Haley in these commits; their report
headings remain available for the teammates responsible for those methods.
