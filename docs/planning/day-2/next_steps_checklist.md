Day 2 — Remaining methods checklist

## Scope already fixed

**Research question:** As Australia's material conditions improved, did

perceived social support and emotional well-being deteriorate relative to

comparable countries?

**Primary outcomes:** household income, employment, lack of social support and

negative affect.

Do not redo the data audit or cleaning. Do not add another primary outcome,

fixed-effects model, causal analysis, composite index or external-data merge.

## Method 1 — Focused comparative EDA

**Status:** Complete and verified on 21 July 2026. `notebooks/04_final_visuals.ipynb`
regenerates the final figure and coverage table directly from the audited raw
data. It executed from a fresh kernel; its period/coverage assertions passed;
the exported PNG was visually inspected; and the repository test suite passed.

- [x]  Move or reproduce the report's four-panel trajectory code in
    
    `notebooks/04_final_visuals.ipynb` so the designated visual notebook creates
    
    the final figure.
    
- [x]  Keep four panels only: household income, employment, lack of social
    
    support and negative affect.
    
- [x]  Show Australia, the same-period supplied-country median and comparator
    
    IQR in every panel.
    
- [x]  Calculate and retain the comparator-country count at each plotted period.
- [x]  Add endpoint counts to the panels or state the full count range in each
    
    caption.
    
- [x]  Use annual years for income and employment.
- [x]  Use pooled-window midpoints `2009, 2012, 2015, 2018, 2021, 2024` for the
    
    social outcomes and label them as three-year pooled windows.
    
- [x]  Keep native units rather than indexing all outcomes to 100.
- [x]  Disclose that the reference composition can change across periods,
    
    particularly for income.
    
- [x]  Export `reports/figures/material_social_trajectories.png` at 300 dpi.
- [x]  Verify the exported figure against the underlying table and inspect it at
    
    the size used in the report and video.
    

**Done when:** the four-panel figure reruns from a fresh kernel, includes honest

period labels and coverage information, and contains no manually entered data.

## Method 2 — Common-endpoint comparative change

**Status:** Complete and verified. The four-outcome
workflow enforces exact common displayed endpoints and reports Australia’s
native change, comparator median native change, direction-oriented comparative
gap, favourable percentile, and eligible-country count. Native and oriented
quantities are explicitly labelled, annual and pooled endpoints are verified,
and a direct audited-data recalculation reconciles every Australian value. The
validated table is exported to `reports/tables/material_social_primary_results.csv`;
the Quarto report independently reproduces it from the immutable input and
fails its render if the two tables diverge.

- [x]  Add all four primary outcomes to one common-endpoint workflow in
    
    `notebooks/02_analysis.ipynb`.
    
- [x]  For each outcome, require Australia and every comparator to share the
    
    exact start and endpoint periods.
    
- [x]  Report Australia's start value, endpoint value and native-unit change.
- [x]  Report the comparator median native-unit change.
- [x]  Calculate an oriented Australia-minus-comparator-median gap where positive
    
    always means more favourable.
    
- [x]  Report the favourable percentile and eligible comparator-country count.
- [x]  Preserve the natural sign in native changes; sign-flip only oriented gaps,
    
    slopes and ranks for lower-is-better outcomes.
    
- [x]  Use `2010–2024` for income and employment and label the social comparison
    
    `2008–10 to 2023–25 pooled windows`.
    
- [x]  Independently recalculate all Australian values directly from the audited
    
    tidy data and resolve any discrepancy.
    
- [x]  Write `reports/tables/material_social_primary_results.csv`.
- [x]  Update the report to read or reproduce exactly the frozen primary table.

**Done when:** one traceable table directly answers the research question for

all four outcomes with periods, units, comparator counts and favourable

directions. Verified by a clean-kernel notebook execution, a CSV round-trip
comparison, a Quarto render-time table comparison, and `5 passed` tests.

## Method 3 — Country bootstrap and placebo-country ranking

**Status:** Not implemented.

### Country bootstrap

- [ ]  Hold Australia's observed endpoint change fixed.
- [ ]  Resample eligible comparator countries with replacement.
- [ ]  Recalculate the comparator median and Australia's oriented gap in every
    
    replicate.
    
- [ ]  Run 10,000 replicates with seed `20260720` separately for each outcome.
- [ ]  Report the bootstrap median, 2.5th percentile and 97.5th percentile.
- [ ]  Describe the interval as comparator-country sensitivity, not OECD survey
    
    sampling uncertainty.
    
- [ ]  Label a result comparator-sensitive when its interval crosses zero.
- [ ]  Write `reports/tables/material_social_bootstrap_results.csv`.

### Placebo-country ranking

- [ ]  Treat each eligible country as the focal country once.
- [ ]  Exclude the focal country from its own comparison median.
- [ ]  Calculate its oriented focal-minus-median gap.
- [ ]  Locate Australia in the full focal-country distribution.
- [ ]  Report Australia's favourable percentile and the number of countries with
    
    more- and less-favourable changes.
    
- [ ]  Explain that the placebo rank and endpoint percentile are alternative
    
    presentations of the same comparative data, not independent evidence.
    
- [ ]  Write `reports/tables/material_social_placebo_results.csv`.

### Final Method 3 output

- [ ]  Build a four-row effect figure with the oriented Australian gap, bootstrap
    
    interval, zero reference line, placebo percentile and comparator count.
    
- [ ]  Separate or clearly annotate native units so dollars and percentage points
    
    are not visually treated as commensurate effect sizes.
    
- [ ]  Export `reports/figures/material_social_comparative_gaps.png` at 300 dpi.

**Done when:** all four outcomes have reproducible bootstrap intervals and

placebo positions, with interpretation calibrated to whether the interval

crosses zero.

## Method 4 — Theil–Sen trend and Kendall's tau

**Status:** Implemented and independently verified on `code-review`. The
notebook exports robust slopes, exploratory trend diagnostics, international
slope positions and endpoint-agreement evidence used by the report.

- [x]  Estimate Australia's native-unit Theil–Sen slope for each primary
    
    outcome.
    
- [x]  Calculate an oriented slope where positive always means favourable.
- [x]  Use annual years from 2010 through 2024 for income and employment.
- [x]  Use the six independent pooled-window midpoints for social support and
    
    negative affect.
    
- [x]  Calculate Kendall's tau, raw p-value and independent-observation count for
    
    each Australian series.
    
- [x]  Apply Holm adjustment across the four pre-specified Kendall tests.
- [x]  For country-level slope comparisons, require the same start and endpoint
    
    and at least 80% of the focal outcome's independent periods.
    
- [x]  Report Australia's favourable slope percentile among eligible countries
    
    and the eligible-country count.
    
- [x]  Compare the sign of each robust slope with its common-endpoint result.
- [x]  Flag disagreement as sensitivity rather than selecting the preferred
    
    result.
    
- [x]  Emphasise direction, magnitude and agreement for the social outcomes;
    
    avoid strong significance claims from six periods.
    
- [x]  Write `reports/tables/material_social_trend_results.csv`.
- [x]  Add a concise endpoint-versus-trend agreement table to the robustness
    
    section of the report.
    

**Done when:** every outcome has a native and oriented robust slope, Kendall

result, observation count, international slope position and an explicit

agreement or disagreement statement.

## Method 5 — Optional Spearman material–social association

**Status:** Implementation verified on 21 July 2026. The notebook passes a
fresh-kernel run, creates the four-row table and 300 dpi diagnostic figure, and
passes its coverage, orientation, bootstrap, permutation, sensitivity and
round-trip assertions. It is **not final-method complete** and is not eligible
for report integration: Methods 3 and 4, the final figures and the primary
report must first be frozen, after which a non-owner must independently verify
the four estimates and Australia’s plotted direction pattern.

**Start rule:** begin only after Methods 1–4, both final figures and the report's

primary results are stable. Drop this method first if time is limited.

- [x]  Confirm that each pre-specified pair has at least 25 countries with all
    
    required common-endpoint changes.
    
- [x]  Test only four pairs: income–social support, income–negative affect,
    
    employment–social support and employment–negative affect.
    
- [x]  Use oriented changes so positive means improvement in every variable.
- [x]  Report Spearman's rho, eligible-country count and a country-bootstrap 95%
    
    interval for every pair.
    
- [x]  Apply Holm adjustment across the four tests if p-values are reported.
- [x]  Display all four results, including null or contradictory associations.
- [x]  State that this is an exploratory ecological association and cannot show
    
    that material change caused social or emotional change.
    
- [x]  Write `reports/tables/material_social_spearman_results.csv` only if the
    
    method passes the coverage rule and adds a clear secondary finding.
    

**Final completion gate (not yet met):** either the full pre-specified
four-pair analysis is reported with appropriate caveats after Methods 1–4 are
frozen and independently checked, or the team records that Method 5 was
intentionally omitted to protect the quality of the primary analysis.

## Final cross-method completion gate

- [ ]  Methods 1–4 rerun from fresh kernels without manual edits.
- [ ]  All generated tables and figures use the same frozen outcome definitions,
    
    periods and comparator rules.
    
- [ ]  Normal-status-only, English-peer, leave-one-peer-out and alternative
    
    social-window sensitivities are recorded in
    
    `reports/tables/material_social_robustness_results.csv`.
    
- [ ]  Classify each headline conclusion as **robust**,
    
    **comparator-sensitive** or **unsupported**.
    
- [ ]  Remove or rewrite any claim that is not supported by the frozen results.
- [ ]  Every report and video number is traceable to a generated table.
- [ ]  Render the Quarto report and run `python -m pytest`.
- [ ]  Have a non-owner verify each headline number, figure and caption.
