# Haley work already incorporated into the report

## Purpose

This file records Haley's completed implementation and the material already
incorporated into `submission/australia_material_social_report.qmd`. It is a
traceability note for team review, not a second report. The quoted passages
below reproduce the report wording exactly as it appears on `haley-b`.

## Where Haley's work appears in the report

| Report location | Haley material represented there |
|---|---|
| **Data cleaning and preprocessing → Independent audit supporting the research question** | Validation rules, immutable raw data, audit scope, missing-year handling, pooled-period handling, same-year comparisons, indicator metadata, quality flags and coverage outputs |
| **Exploratory analysis and question selection → Development of the research question** | Coverage-led selection of the material--social question and exclusion of life satisfaction as a primary long-run outcome |
| **Methodology → Method 1: EDA** | Same-period supplied-country reference, annual versus pooled outcomes, direction-aware interpretation and four pre-specified primary outcomes |
| **Methodology → Method 2: Primary common-endpoint comparison** | Exact common-endpoint eligibility, comparator counts, native changes, direction-oriented gaps and non-causal interpretation |
| **Analysis and results → Findings** | Material improvement, comparative underperformance on the two primary material changes, adverse social changes and the material--social synthesis |
| **Conclusion** | The bounded answer to the research question and explicit causal boundary |
| **Limitations → Limitations and claim boundaries** | Changing comparator composition, survey/source differences, quality flags, pooled-window timing and construct limitations |
| **Economic comparison table and trajectory graph** | Responsive table widths, expanded interpretation column, alternating row styling and graph scaling that prevents clipping |

## Exact report text added for the cleaning audit

### Independent audit supporting the research question

An additional reproducible audit was implemented in `src/oecd_audit.py` and
documented in `notebooks/00_data_audit.ipynb`. It begins from the unchanged raw
file and stops if required columns or observation values are missing, if a
country--indicator--year key is duplicated, or if an indicator lacks documented
metadata. No observations are interpolated or imputed. The resulting
`data/processed/oecd_clean.csv` retains all 8,806 supplied observations and adds
quality flags, favourable directions and independent-period labels. Restricting
this validated copy to the report's 2010--2024 scope yields 8,575 observations,
consistent with the team-prepared analysis dataset; later supplied rows are
retained for auditability but excluded from the primary analysis.

The audit outputs have distinct roles in protecting the analysis from common
comparison errors:

| Audit output | What and how | Why it supports the research question |
|---|---|---|
| `time_series_gaps.csv`, `coverage_by_country_indicator.csv` and `coverage_by_country_year.csv` | Record observed years, independent periods, quality flags and country-year indicator availability | Distinguish genuine annual gaps from intentionally periodic measurement and show where trend evidence is sufficiently complete |
| `indicator_metadata.csv` | Records each indicator's unit, favourable direction, frequency, definition pages and comparability caveat | Prevents unlike constructs from being interpreted as equivalent and ensures adverse social changes are oriented correctly |
| `same_year_australia_comparisons.csv` | Compares Australia only with countries reporting the same indicator in the same displayed year and reports the contributing-country count | Prevents a country measured in one period from being ranked against another measured in a different period |
| `australia_indicator_summary.csv` | Summarises Australia's independent-period change and latest same-year international position | Supports transparent scouting of indicators before fixing the four primary outcomes |
| `domain_coverage_all.csv` and `domain_coverage_australia.csv` | Rank domains by unique country--indicator--period evidence rather than repeated displayed rows | Guides question selection by evidential coverage; these ranks measure data availability, not substantive importance |

These checks directly shaped the final design. Australia's income and
employment series contain no internal annual gaps within their observed spans.
In contrast, lack of social support and negative affect each contain 16
displayed Australian rows but only six independent three-year pooled windows;
the repeated rows are therefore never treated as 16 independent observations.
Australia reports 17 of the 21 indicators, with no observations for
overcrowding, time off, the gender gap in working hours, or time spent in social
interactions. Consequently, lack of social support is used as a focused proxy
rather than a complete measure of social connection. All Australian rows carry
normal OECD status, although flagged peer observations remain visible for
sensitivity analysis. Detailed interpretations are provided in
`docs/analysis/oecd_data_quality_notes.md`, and the exploratory rationale is
recorded in `docs/analysis/oecd_exploration_and_questions.md`.

## Exact report text added for Method 2

### Method 2: Primary common-endpoint comparison

For each primary outcome, Australia was compared only with countries reporting
both of the same endpoints. This avoids attributing differences caused by
unequal observation periods to country performance. Because data availability
varies across outcomes, the eligible comparator set and its size are reported
separately for every comparison.

Changes are retained in their original units for interpretation. A
direction-oriented version is used only for comparative gaps and percentiles,
so that a positive value consistently represents a more favourable change.
This distinction is essential for lack of social support and negative affect,
where lower values indicate better outcomes. The analysis is descriptive and
does not estimate a causal effect of material conditions on social or emotional
well-being.

## Exact report synthesis added after the primary findings

Together, these results indicate that Australia's material conditions improved
in absolute terms, but not more rapidly than the typical eligible comparator
for the two primary material outcomes. Over the observed pooled windows, both
social outcomes moved in an adverse direction and deteriorated more than their
respective comparator medians. This pattern supports a descriptive
material--social tension; it does not establish that material progress caused
the changes in social support or emotional well-being.

## Exact conclusion added to the report

Australia's performance cannot be characterised adequately by a single
economic measure. Household income and employment both increased over the
study period, demonstrating meaningful domestic material progress. However,
Australia's gains in these outcomes were below the median changes among
countries with the same observed endpoints.

At the same time, perceived lack of social support and negative affect worsened
across the six independent pooled survey windows. Australia's adverse changes
were larger than those of the typical eligible comparator. Within the scope of
the supplied data, the evidence therefore supports a carefully bounded
conclusion: Australia became materially better resourced while its measured
social and emotional outcomes deteriorated comparatively. Further analysis may
test the robustness of this pattern, but causal explanations require different
data and a dedicated causal design.

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

.trajectory-figure .cell-output-display img {
  display: block;
  width: 100%;
  max-width: 100%;
  height: auto;
  margin: 0 auto;
}
```

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
