# Notebooks

Use numbered notebooks in execution order. Keep each notebook focused. The relevant implementation is included directly in the implemented notebooks so teammates and judges can read each workflow in one place. The matching code in `src/oecd_audit.py` remains the canonical, tested command-line version; update both copies together when logic changes.

Implemented starter sequence:

- `00_data_audit.ipynb`
- `01_eda.ipynb`
- `02_analysis.ipynb`
- `03_robustness.ipynb`
- `04_final_visuals.ipynb`
- `05_health_social_wellbeing.ipynb`
- `method4_theilsen_kendall.ipynb`

`00_data_audit.ipynb` keeps both implementations in one place and in team order: Yilin's original tidy-data, category-summary, and domain-count workflow appears first exactly as merged, followed by Haley's validated audit and comparison workflow.

Each notebook should state its purpose, inputs, outputs, assumptions, author, and last successful run date near the top.

The audit notebook implements the OECD cleaning, gap, pooled-period, comparability, same-year comparison, and coverage checks. The EDA notebook implements the initial economic/social exploration and recommended question direction. The analysis and robustness notebooks implement exact common endpoints, same-year gaps, broad supplied-country comparisons, normal-value-only comparisons, and leave-one-peer-out checks. The Method 4 notebook adds Theil--Sen slopes, direction-aware Kendall diagnostics, 80%-coverage international slope comparisons and endpoint-agreement checks. The health/social/well-being notebook applies the data safeguards with pooled-window timing, and the final-visual notebook creates the primary trajectory figure.
