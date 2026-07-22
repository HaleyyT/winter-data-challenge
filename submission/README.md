# Winter Data Challenge Submission

This folder is a self-contained submission examining whether Australia's gains
in household income and employment were accompanied by comparable improvements
in perceived social support and negative affect.

The following four dependent variables are considered for evaluation:

- Household disposable income per capita
- Employment rate
- Perceived lack of social support
- Negative affect

All data, source code for analysis, tests, source and output documents for the report are contained in `submission/`.

## Author

Haley Tran (530002284)
Yilin Li (530536402)
Winnie Qiu (550720773)

## Quick start

Create the environment from the parent directory containing `submission/`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r submission/requirements.txt
```

Quarto must also be installed to render the HTML report. Execute the entire
workflow from the same parent directory with:

```bash
./submission/run_all.sh
```

This process will halt at once in case any command is not successful. This workflow will run the data audit, execute the notebooks in their order of dependency, run the tests automatically, and render the Quarto report. Copies of executed notebooks will be created in a temporary folder instead of overwriting the submitted notebooks.

The workflow stops on the first failed command. It writes executed notebook
copies to a temporary directory, leaving the submitted source notebooks clean.

## Folder structure

```text
submission/
├── OECD Data.csv
├── README.md
├── SUBMISSION_CHECKLIST.md
├── ai_acknowledgement.md
├── requirements.txt
├── run_all.sh
├── code/
├── data/
├── tests/
└── report/
    ├── australia_material_social_report.qmd
    ├── australia_material_social_report.html
    ├── references.bib
    ├── figures/
    └── tables/
```

## Files in the submission root

| File | Purpose |
|---|---|
| `OECD Data.csv` | Original supplied OECD dataset. The analysis treats this as an immutable raw input. |
| `README.md` | Guide to the submission structure, execution order and outputs. |
| `SUBMISSION_CHECKLIST.md` | Final technical and manual checks before portal upload. |
| `ai_acknowledgement.md` | Required acknowledgement describing the use of AI assistance. |
| `requirements.txt` | Python environment specification for notebooks, tests and report code. |
| `run_all.sh` | Executes the complete analysis, tests and report build in the required order. |
| `.gitignore` | Excludes local caches and other runtime artefacts that should not be submitted. |

## Analysis code: `submission/code/`

The notebooks are designed to run from either the repository root or the
`submission/code/` directory. All paths are resolved relative to
`submission/`, not to a user's absolute filesystem path.

### `oecd_audit.py`

A shared audit/cleaning module used by both the notebooks and tests. This module:

- checks the integrity of the structure and key of the raw dataset;
- keeps observation status and comparability notes;
- finds the independent time periods for the pool of three years of social data;
- sets the indicator direction and metadata;
- creates the coverage, gap, comparison, and Australian-specific tables; and
- generates the cleaned dataset and audit tables.

This can be executed independently of the repository root:

```bash
python -m submission.code.oecd_audit
```

### Notebook execution order

| Order | Notebook | Purpose | Principal outputs |
|---:|---|---|---|
| 1 | `data_audit.ipynb` | Inspects the supplied file, validates fields and values, cleans the data, documents quality flags, and creates domain summaries. | Files in `submission/data/` and general audit tables in `submission/report/tables/`. |
| 2 | `method1_eda.ipynb` | Exploratory analysis of coverage, Australian changes, same-year comparisons and selected material/social outcomes. It excludes Australia from reference distributions and counts social windows independently. | `material_social_trajectories.png` and `material_social_trajectory_coverage.csv`. |
| 3 | `method02_primary_same_endpoint.ipynb` | Primary exact-endpoint comparison. A comparator is eligible only when it reports both of Australia's required endpoints. Native changes are retained, while direction-oriented changes support rankings. | `material_social_primary_results.csv`. |
| 4 | `method03_comparator_bootstrap_placebo.ipynb` | Holds Australia's endpoint change fixed, resamples eligible comparator countries, and calculates placebo rankings. The interval measures comparator-composition sensitivity rather than survey-sampling uncertainty. | `material_social_bootstrap_results.csv`, `material_social_placebo_results.csv`, and `material_social_comparative_gaps.png`. |
| 5 | `method4_theilsen_kendall.ipynb` | Tests trend robustness using independent observations, Theil–Sen slopes and Kendall statistics. It also compares Australia's slope with same-span country slope distributions. | Method 4 result tables and two Method 4 figures. |
| 6 | `method5_spearman_association.ipynb` | Examines exploratory country-level rank associations between material change and social change using Spearman correlations, bootstrap intervals and permutation tests. | `material_social_spearman_results.csv` and `material_social_spearman_associations.png`. |
| 7 | `final_visuals.ipynb` | Visualization-only collection of the figures for Methods 03–05. Method 02 is skipped because it exports a table rather than a figure. | Displays plots in the notebook only; it deliberately contains no `savefig()` or CSV export calls. |

Method 02 needs to be executed before the execution of methods 03 to 05 because these methods verify their results from the frozen primary result table.

## Processed data: `submission/data/`

| File | Purpose |
|---|---|
| `OECD_cleaned_version.csv` | Cleaned 2010–2024 analysis copy produced by the notebook audit workflow, including quality-status fields. |
| `OECD_categories.csv` | Dataset composition by OECD well-being domain, including indicators, units, coverage and observation counts. |
| `OECD_domain_counts.csv` | Ranked domain-level observation counts for all supplied countries. |
| `AU_domain_counts.csv` | Ranked domain-level observation counts for Australia. |
| `oecd_clean.csv` | Canonical tidy analysis dataset produced by `oecd_audit.py`. It retains flags, direction metadata and independent-period labels and is used by the main analyses. |

Original file `OECD Data.csv` is present in the submission directory. Workflow does not overwrite any of the input files.

## Automated tests: `submission/tests/`

Run all tests from the repository root with:

```bash
python -m pytest submission/tests -q
```

| Test file | Coverage |
|---|---|
| `test_oecd_audit.py` | Raw-data validation, cleaning, pooled-period handling, coverage calculations and audit output invariants. |
| `test_method3_outputs.py` | Method 03 output existence, comparator counts, deterministic bootstrap results, placebo ranks and reconciliation with Method 02. |
| `test_method4_outputs.py` | Method 04 outcome coverage, common endpoints, trend results, inference fields and comparator percentiles. |
| `test_method5_spearman.py` | Method 05 endpoint changes, pair counts, Spearman estimates, bootstrap and permutation calculations, and reconciliation with primary results. |


## Report: `submission/report/`

| File | Purpose |
|---|---|
| `australia_material_social_report.qmd` | Reproducible Quarto source for the written submission. It reads the supplied data and validated result tables, runs embedded checks, inserts figures and builds the final report. |
| `australia_material_social_report.html` | Rendered, self-contained HTML report. |
| `references.bib` | BibTeX bibliography used by the Quarto report. Because it is in the same directory as the QMD file, the report uses `bibliography: references.bib`. |

Rebuild the report independently with:

```bash
quarto render submission/report/australia_material_social_report.qmd
```

### Figures: `submission/report/figures/`

| Figure | Purpose |
|---|---|
| `material_social_trajectories.png` | Australia and same-period supplied-country distributions for the four main material/social outcomes. This is a tracked report asset used for the trajectory discussion. |
| `material_social_comparative_gaps.png` | Method 03 comparator-composition bootstrap intervals with placebo-ranking information. |
| `method4_australia_theilsen_trends.png` | Method 04 Australian observations and fitted Theil–Sen trends. |
| `method4_country_slope_distributions.png` | Method 04 comparison of Australia's favourable-oriented slope with eligible country slopes. |
| `material_social_spearman_associations.png` | Method 05 scatterplots for the four pre-specified material/social change pairs. |

`final_visuals.ipynb` rebuilds Method 03-05 visuals for review but does not save
anything to this directory. The principal Method 01 trajectory figure is
generated by `method1_eda.ipynb`.

### Main analysis tables: `submission/report/tables/`

| Table | Purpose |
|---|---|
| `material_social_primary_results.csv` | Method 02 exact-endpoint Australian changes, comparator medians, oriented gaps, percentiles and eligible-country counts. |
| `material_social_bootstrap_results.csv` | Method 03 comparator-resampling estimates, intervals and sensitivity classifications. |
| `material_social_placebo_results.csv` | Method 03 placebo ranks, percentiles and country counts. |
| `material_social_trend_results.csv` | Method 04 Australian slopes, confidence intervals, Kendall statistics, endpoint agreement and comparator position. |
| `method4_country_slope_distribution.csv` | Country-level Method 04 slopes used to locate Australia within eligible same-span distributions. |
| `method4_country_slope_summary.csv` | Compact Method 04 comparator distribution summary for each primary outcome. |
| `method4_independent_social_observations.csv` | Independent pooled social observations used in Method 04 rather than repeated annual display rows. |
| `material_social_spearman_results.csv` | Method 05 Spearman estimates, bootstrap intervals, permutation results and sensitivity diagnostics. |
| `material_social_trajectory_coverage.csv` | Country counts supporting each point in the material/social trajectory figure. |

### Audit and coverage tables

| Table | Purpose |
|---|---|
| `time_series_gaps.csv` | Calendar-gap audit with frequency-aware interpretation. Non-annual blank years are not automatically classified as missing data. |
| `coverage_by_country_indicator.csv` | Coverage, independent-period counts, distinct values and status flags for every country–indicator series. |
| `coverage_by_country_year.csv` | Number of indicators and flagged observations available for each country and year. |
| `same_year_australia_comparisons.csv` | Australia compared only with countries reporting the same indicator in the same year. |
| `indicator_metadata.csv` | Indicator direction, type, frequency, coverage, definitions pages and comparability caveats. |
| `australia_indicator_summary.csv` | Australian endpoint changes and latest same-year comparative positions through 2024. |
| `domain_coverage_all.csv` | Domain coverage for the full supplied-country dataset. |
| `domain_coverage_australia.csv` | Domain coverage restricted to Australia. |

### Retained exploratory tables

Below are the tables containing earlier attempts at exploration of sensitivity towards economics and English-speaking peers. These have been kept for transparency purposes, but they are not part of the main outputs from Method 02–05, and therefore they will not be re-created using the split Method 02 and Method 03 notebooks:

- `economic_change_scorecard_all_countries.csv`;
- `economic_change_scorecard_english_peers.csv`;
- `economic_change_scorecard_normal_values.csv`;
- `economic_leave_one_out.csv`;
- `income_inequality_change_scorecard.csv`;
- `income_relative_trend_english_peers.csv`;
- `employment_relative_trend_english_peers.csv`; and
- `long_hours_relative_trend_english_peers.csv`.

## Reproducibility notes

- All random processes are done with known seeds which are stated in the tables of results.
- Social-support and negative-affect lines with the same repeated pooled three-year numbers are converted to independent pools whenever necessary.
- Results which follow the lower-is-better principle are only multiplied by `-1` in favor-oriented comparisons; native results are left with their own signs and measurements.
- This study is descriptive and comparative; no causal relationship is inferred.
- Intervals for Method 03 reflect the sensitivity to the collection of comparator countries, not the original survey data uncertainty.
- Australia is shown in Method 05 graphs but excluded from comparator association estimates.
