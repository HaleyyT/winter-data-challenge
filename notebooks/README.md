# Notebooks

Use numbered notebooks in execution order. Keep each notebook focused. The relevant implementation is included directly in the implemented notebooks so teammates and judges can read each workflow in one place. The matching code in `src/oecd_audit.py` remains the canonical, tested command-line version; update both copies together when logic changes.

Implemented starter sequence:

- `00_data_audit.ipynb`
- `01_eda.ipynb`
- `02_analysis.ipynb`
- `03_robustness.ipynb`
- `04_final_visuals.ipynb`

The merge also preserves `yilin_data_cleaning_reference.ipynb`, Yilin's original tidy-data, category-summary, and domain-count workflow. It is kept as a companion reference so both implementations remain reviewable; `00_data_audit.ipynb` is the canonical shared audit workflow.

Each notebook should state its purpose, inputs, outputs, assumptions, author, and last successful run date near the top.

The audit notebook now implements the OECD cleaning, gap, pooled-period, comparability, same-year comparison, and coverage checks. The EDA notebook implements the initial economic/social exploration and recommended question direction. The analysis, robustness, and final-visual notebooks remain explicit placeholders until the team locks the primary research protocol.
