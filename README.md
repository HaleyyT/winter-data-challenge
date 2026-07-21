# 2026 Winter Data Analysis Challenge

Team workspace for the University of Sydney Winter Data Analysis Challenge, held online **20–22 July 2026**. The challenge runs for three days, and assesses analytical innovation, communication, critical evaluation, and understanding of the wider context.

Challenge page: <https://spds.sydney.edu.au/winter-data-analysis-challenge/>

## Quick start

Requires Python 3.11+.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Always start Jupyter from the activated environment (or run `.venv/bin/jupyter lab`) so notebooks use the project dependencies. Verify the workspace with `python -m pytest` and regenerate the OECD audit with `python -m src.oecd_audit`.

When the dataset is released, place the original, unchanged files in `data/raw/`. Do not commit restricted or large data files. Record their source, download time, licence, and any access conditions in `data/README.md`.

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

```bash
.venv/bin/jupyter nbconvert --to notebook --execute notebooks/02_analysis.ipynb \
  --output /tmp/02_analysis.executed.ipynb --ExecutePreprocessor.timeout=300
.venv/bin/jupyter nbconvert --to notebook --execute notebooks/03_robustness.ipynb \
  --output /tmp/03_robustness.executed.ipynb --ExecutePreprocessor.timeout=300
.venv/bin/jupyter nbconvert --to notebook --execute notebooks/04_final_visuals.ipynb \
  --output /tmp/04_final_visuals.executed.ipynb --ExecutePreprocessor.timeout=300
.venv/bin/jupyter nbconvert --to notebook --execute notebooks/05_health_social_wellbeing.ipynb \
  --output /tmp/05_health_social_wellbeing.executed.ipynb --ExecutePreprocessor.timeout=300
quarto render submission/australia_material_social_report.qmd
```

The notebooks regenerate the reviewable final tables and figures before Quarto
checks and embeds them. Run the commands from the repository root.

## Team workflow

See [docs/TEAM_WORKFLOW.md](docs/TEAM_WORKFLOW.md). Agree on names and ownership before kickoff, use short-lived feature branches, and require another teammate to review conclusions as well as code.

## Current status

The released OECD dataset audit and initial economic/social exploration are implemented. The team still needs to lock the primary question, comparison group, statistical protocol, robustness checks, and final submission format.
