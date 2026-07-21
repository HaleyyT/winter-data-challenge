# Focused Eight-Hour Analysis Plan for Three People

## Summary

The external advice is mostly correct: the project needs fewer, better-connected methods. The final analysis should use:

1. Focused comparative EDA.
2. Common-endpoint comparative changes.
3. Country bootstrap and placebo-country ranking.
4. Theil–Sen trend analysis with Kendall’s tau.
5. Spearman association only if the core work finishes early.

This is rigorous enough for the judges’ “statistical analysis” criterion. A complicated predictive model is not required.

To estimate, team will work together for six hours today—approximately 18 person-hours—and two hours tomorrow—another six person-hours.

## Important model decision

### Do not prioritise the proposed fixed-effects model

A country-and-period fixed-effects model sounds sophisticated, but it is not the best use of this project’s remaining time:

- Australia is the only focal country, so the `Australia × time` estimate depends on one national trajectory.
- Social support and negative affect have only six independent pooled periods.
- Treating repeated rows as annual observations would create false precision.
- Income coverage is unbalanced: only nine countries cover every available income period.
- Reliable clustered inference is difficult when there is only one focal country.
- It introduces assumptions about linear trends without materially improving the answer.

A fixed-effects coefficient could be shown descriptively, but its apparent precision would be difficult to defend. The placebo-country distribution and country bootstrap answer “How unusual is Australia?” more transparently.

### Selected formal model

The project’s primary formal model will be the **Theil–Sen robust trend model**. It estimates the typical rate of change without being overly influenced by one unusual year.

The report should say:

> We combined common-period comparative estimates with country-level bootstrap uncertainty, placebo-country calibration and robust trend models.

## Final analytical framework

### Method 1 — Focused comparative EDA

For income, employment, lack of social support and negative affect:

- Plot Australia across time.
- Plot the same-period supplied-country median.
- Add the comparator interquartile range where readable.
- Report the number of countries contributing at each period.
- Label social observations as pooled windows.
- Use `2009, 2012, 2015, 2018, 2021, 2024` as the midpoint years of the six social windows.

Purpose:

- Establish what changed.
- Identify whether Australia diverged.
- Reveal gaps, shocks and non-linear patterns before summarising them statistically.

This is not called a model; it is the evidence foundation.

### Method 2 — Primary common-endpoint comparison

For each primary indicator, calculate:

- Australian start and endpoint values.
- Australian absolute change.
- Median change among countries with identical endpoints.
- Australia-minus-comparator change.
- Favourable percentile.
- Comparator-country count.

Outcome direction:

- Income: higher is better.
- Employment: higher is better.
- Lack of social support: lower is better.
- Negative affect: lower is better.

Maintain two versions:

- Native change for interpretation, such as dollars or percentage points.
- Oriented change for rankings, where positive always means improvement.

This is the primary answer to the research question.

### Method 3 — Bootstrap uncertainty and placebo ranking

#### Country bootstrap

For each indicator:

1. Hold Australia’s observed change fixed.
2. Resample eligible comparator countries with replacement.
3. Recalculate the comparator median.
4. Calculate Australia minus the resampled median.
5. Repeat 10,000 times with seed `20260720`.
6. Report the 95% percentile interval.

Interpretation:

- Entire interval below zero: consistently less favourable than the comparator median.
- Interval crosses zero: evidence is directionally suggestive but comparator-sensitive.
- Entire interval above zero: consistently more favourable.

Clarify that this interval captures sensitivity to the available comparison countries, not survey sampling error.

#### Placebo-country distribution

For every eligible country:

1. Treat it as the focal country.
2. Compare its change with the median of all remaining countries.
3. Repeat for every country.
4. Locate Australia in this distribution.

Report this intuitively:

> Australia’s social-support change was less favourable than X% of eligible countries.

This is preferable to forcing a regression p-value.

### Method 4 — Theil–Sen and Kendall trend robustness

For every primary indicator:

- Estimate Australia’s Theil–Sen slope.
- Calculate Kendall’s tau between time and the indicator.
- Orient slope signs so positive means favourable.
- Compare Australia’s slope with the distribution of country-level slopes where coverage permits.
- Use independent pooled-period midpoints for the two social indicators.

Report:

- Slope in native units per year.
- Favourable slope direction.
- Kendall’s tau.
- Raw and Holm-adjusted p-value.
- Number of independent observations.

For social outcomes, focus on direction and agreement with the endpoint result. Six observations are too few for strong significance claims.

### Optional Method 5 — Spearman material–social association

Start only if the four core methods and both final figures are stable by the end of Hour 4.

Ask:

> Across countries, was greater material improvement associated with improving or worsening social outcomes?

Test four pre-specified pairs:

- Income and social support.
- Income and negative affect.
- Employment and social support.
- Employment and negative affect.

Requirements:

- At least 25 complete countries for each pair.
- Report all four results.
- Use country-bootstrap confidence intervals.
- Apply Holm correction across four tests.
- Describe the analysis as exploratory and ecological.

Do not add robust regression, composite indices or additional associations today.

## Reliability and data controls

### Controls already established and retained

- Raw OECD data remain unchanged.
- Duplicate country–indicator–year keys cause an error.
- Repeated pooled social rows are counted once.
- Countries are compared only at common periods.
- Missing years are not interpolated.
- Directionality is stored and checked for each indicator.
- Comparator counts accompany rankings.
- Flagged OECD observations can be excluded.
- The supplied-country group is not incorrectly labelled as “OECD countries.”

### Required sensitivity analyses

For the four primary outcomes:

1. All supplied countries with common endpoints.
2. Normal-status observations only.
3. English-speaking peers.
4. Leave-one-peer-out.
5. Social start changed from `2008–10` to `2011–13`.
6. Social endpoint changed from `2023–25` to `2020–22`.
7. Endpoint change compared with the Theil–Sen trend direction.

Use a simple robustness classification:

- **Robust:** direction remains unchanged across the main reasonable specifications.
- **Sensitive:** direction remains, but magnitude or rank changes materially.
- **Unsupported:** direction reverses or coverage becomes inadequate.

### Methods not needed

- No train/test split or cross-validation: there is no prediction task.
- No hyperparameter tuning: selected methods have no meaningful tuning process.
- No synthetic data augmentation.
- No annual interpolation of pooled social data.
- No Random Forest, XGBoost, neural network or forecasting.
- No causal language, difference-in-differences or synthetic control.
- No arbitrary material or well-being composite score.

External Australian evidence can provide context but should not be merged into the OECD analysis unless definitions and periods genuinely match.

## Six-hour team plan for today

### Hour 0:00–0:30 — Joint analysis freeze

All three members confirm:

- Exact research question.
- Four primary indicators.
- Endpoint periods.
- Primary comparator group.
- Indicator directionality.
- Bootstrap settings.
- Required final tables and figures.

Create a shared claim table with:

| Claim | Indicator | Period | Statistic required | Limitation |
|---|---|---|---|---|

No primary outcome or endpoint changes after this meeting.

### Hour 0:30–2:30 — Parallel implementation

#### Haley: primary estimates and uncertainty

Work in `notebooks/02_analysis.ipynb`.

- Combine all four primary indicators in one result table.
- Calculate common-endpoint changes and favourable percentiles.
- Implement the 10,000-resample country bootstrap.
- Implement the placebo-country distribution.
- Write reproducible result tables.

Deliver:

- `material_social_primary_results.csv`
- `material_social_bootstrap_results.csv`
- `material_social_placebo_results.csv`

#### Yilin: sensitivity and independent data verification

Work in `notebooks/03_robustness.ipynb`.

- Independently reproduce the four Australian endpoint changes.
- Verify independent pooled periods.
- Run normal-status-only comparisons.
- Run English-peer and leave-one-peer-out checks.
- Run alternative social start and endpoint checks.
- Record comparator counts and missing countries.

Deliver:

- `material_social_robustness_results.csv`
- A completed claim–evidence–limitation table.

#### Winnie: robust trends and definitions

Work in `notebooks/05_health_social_wellbeing.ipynb`.

- Implement Theil–Sen and Kendall analysis.
- Use independent pooled-window midpoints.
- Compare endpoint direction with trend direction.
- Verify OECD definitions and lower-is-better indicators.
- Prepare no more than three contextual observations from external Australian evidence.

Deliver:

- `material_social_trend_results.csv`
- A short interpretation note that avoids causal claims.

Each person edits a different notebook to prevent merge conflicts.

### Hour 2:30–3:00 — Integration checkpoint

Together:

- Compare independently calculated Australian values.
- Check directionality and units.
- Review bootstrap intervals.
- Review endpoint-versus-trend agreement.
- Resolve any discrepancy before making figures.

Approve one frozen primary results table.

### Hour 3:00–4:30 — Final figures

#### Winnie

Build the primary trajectory figure in `notebooks/04_final_visuals.ipynb`:

- Four panels.
- Australia, comparator median and comparator IQR.
- Honest pooled-window labels.
- Comparator counts in caption or secondary labels.

#### Haley

Build the comparative-effect figure:

- One row per primary indicator.
- Australia-minus-comparator gap.
- Bootstrap 95% interval.
- Favourable direction consistently shown.
- Native-unit values included in labels or an adjacent table.

#### Yilin

Perform figure QA:

- Verify every plotted value against a generated CSV.
- Check axes, units, periods, colours and indicator directions.
- Confirm figures regenerate from a fresh kernel.

Do not start Spearman analysis unless these figures and tables are stable.

### Hour 4:30–5:30 — Report drafting

#### Haley

Write:

- Statistical methods.
- Primary comparative results.
- Bootstrap and placebo interpretation.

#### Yilin

Write:

- Data preparation.
- Comparability controls.
- Robustness and reproducibility.

#### Winnie

Write:

- Motivation and research question.
- EDA interpretation.
- Wider context and limitations.

The main conclusion must be calibrated to the uncertainty:

- Strong evidence: “worsened relative to the typical comparator.”
- Comparator-sensitive: “showed a less favourable change, although uncertainty included no difference.”
- Unsupported: report the inconsistency plainly.

### Hour 5:30–6:00 — Results freeze

Together:

- Verify every headline number.
- Freeze two final figures.
- Freeze the primary results table.
- Decide whether the optional Spearman analysis adds enough value for tomorrow.
- Record unresolved tasks.
- Commit work in separate, descriptive commits.

No new models begin after this point.

## Two-hour plan for tomorrow

### Hour 0:00–0:30 — Reproducibility run

Yilin runs the complete workflow from fresh kernels.

Haley and Winnie compare regenerated figures and tables against the frozen results.

Required:

- All tests pass.
- All notebooks complete.
- Bootstrap results reproduce with the fixed seed.
- No manual edits are required to create final outputs.

### Hour 0:30–1:15 — Final report refinement

- Tighten the answer to the research question.
- Add the two final figures.
- Include null or sensitive findings.
- Finalise methods, limitations and external context.
- Verify team names and SIDs.
- Render the source report.

If the core report is already complete, this block may instead be used for the pre-specified Spearman analysis. Stop it after 30 minutes if it does not produce a clear, defensible contribution.

### Hour 1:15–2:00 — Video and submission readiness

- Convert the report into a 2:50–2:55 narrative.
- Use the same two figures as the report.
- Verify every spoken number.
- Confirm source report, rendered report and video requirements.
- Complete an independent final checklist.

## Acceptance criteria

The analysis is complete when:

- Four primary indicators have common-period comparative estimates.
- Bootstrap intervals and placebo rankings are available.
- Endpoint and robust-trend conclusions are compared.
- All sensitivity analyses are documented.
- Two final figures regenerate automatically.
- Every headline claim names its period and comparison population.
- Null and contradictory results are retained.
- No pooled social estimate is treated as an annual independent observation.
- No causal relationship is claimed.
- Another teammate can reproduce the outputs without guidance.

## Assumptions

- The six hours today are shared working hours for all three members.
- Existing EDA, endpoint analysis and audit code will be extended rather than rewritten.
- The optional association analysis is the first item dropped if time becomes constrained.
- This updated plan will replace the current method section in `local_notes/material_social_project_plan.md`.
