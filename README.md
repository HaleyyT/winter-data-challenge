# 2026 Winter Data Analysis Challenge

Team workspace for the University of Sydney Winter Data Analysis Challenge, held online **20–22 July 2026**. The challenge runs for three days, and assesses analytical innovation, communication, critical evaluation, and understanding of the wider context.

Challenge page: <https://spds.sydney.edu.au/winter-data-analysis-challenge/>

## Reproduce the final submission

Python 3.11+ and [Quarto](https://quarto.org/docs/get-started/) are required.
Run the following commands from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest submission/tests -q
quarto render submission/report/australia_material_social_report.qmd
```

The commands above create the environment, run the automated validation suite
and rebuild the self-contained HTML report. To regenerate the processed data,
all Method 1–5 outputs, the tests and the report in dependency order, run:

```bash
./submission/run_all.sh
```

Executed notebook copies are written to a temporary directory, leaving the
submitted source notebooks unchanged. To explore interactively, start
`jupyter lab` from the activated environment.

## Project structure

```text
.
├── data/                 # Raw, external, intermediate, and analysis-ready data
├── docs/
│   ├── planning/         # Pre-challenge research and strategy notes
│   └── TEAM_WORKFLOW.md  # Three-person roles, Git workflow, and timeline
├── notebooks/            # Numbered exploratory and analytical notebooks
├── references/           # Data dictionaries and allowed reference material
├── reports/
│   ├── figures/          # Generated publication-ready figures
│   └── tables/           # Generated result tables
├── src/                  # Reusable loading, cleaning, features, and plotting code
├── submission/           # Final report/presentation sources and checklist
└── tests/                # Tests for reusable or high-risk transformations
```

## Reproducible workflow

1. Preserve supplied files in `data/raw/`; never edit them in place.
2. Explore with small, numbered notebooks. Move shared logic into `src/`.
3. Write temporary cleaned files to `data/interim/` and final analysis-ready files to `data/processed/`.
4. Generate final charts and tables into `reports/`, not by manual copy/paste.
5. Record decisions, assumptions, limitations, and external sources as the analysis evolves.
6. Run `python -m pytest` before the final submission when tests exist.

For the released OECD dataset, run `python -m src.oecd_audit` to validate the raw file and regenerate the cleaned data, coverage audit, time-series gaps, same-year Australia comparisons, and indicator metadata. See [the data-quality notes](docs/analysis/oecd_data_quality_notes.md) and [the initial findings and question direction](docs/analysis/oecd_exploration_and_questions.md).

Suggested notebook names are `00_data_audit.ipynb`, `01_eda.ipynb`, `02_analysis.ipynb`, and `03_final_visuals.ipynb`. Avoid committing notebook outputs containing sensitive data or very large embedded plots.

## Reproduce the report

The full commands are given in **Reproduce the final submission** above and in
[`submission/README.md`](submission/README.md). For report-only regeneration
after all tables and figures already exist, run:

```bash
source .venv/bin/activate
quarto render submission/report/australia_material_social_report.qmd
```

The rendered output is
`submission/report/australia_material_social_report.html`.

## Team workflow

See [docs/TEAM_WORKFLOW.md](docs/TEAM_WORKFLOW.md). Agree on names and ownership before kickoff, use short-lived feature branches, and require another teammate to review conclusions as well as code.

## Current status

The reproducible submission package is implemented. It contains the frozen
research question, audited data workflow, Methods 1–5, automated validation,
Quarto source and rendered HTML report. The full workflow currently passes 20
tests. The final under-three-minute video remains a manual portal deliverable.
