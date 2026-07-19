# Team workflow

## Roles

Assign one primary owner to each stream, but cross-review all important decisions.

| Role | Primary focus | Cross-review |
|---|---|---|
| Data lead | Data audit, cleaning, joins, reproducible pipeline | Checks model inputs and data limitations |
| Analysis lead | Research questions, statistics/modelling, robustness | Reviews cleaning assumptions and interpretation |
| Story lead | Context research, visual design, report/presentation | Challenges claims and checks every result is traceable |

Also nominate one submission owner and one backup. Names, contact details, and private credentials should stay outside Git.

## Git conventions

- Protect `main` as the always-runnable branch.
- Use short branches such as `data/audit`, `analysis/baseline`, or `story/final-figures`.
- Pull before starting, commit small coherent changes, and merge frequently.
- Do not commit raw datasets, secrets, generated exports, or undocumented external data.
- Before merging: clear noisy notebook output, rerun affected work top-to-bottom, and ask one teammate to review.
- Avoid having two people edit the same notebook at once; shared logic belongs in `src/`.

## Three-day cadence

### Day 1 — understand and choose

- Read the full brief together and copy exact requirements into the submission checklist.
- Audit data quality, provenance, units, coverage, missingness, and bias.
- Brainstorm multiple focused questions; score them for value, feasibility, originality, and communicability.
- Select one main question and one fallback after quick prototypes.
- Produce a reproducible baseline and draft the story outline.

### Day 2 — analyse and challenge

- Complete the main analysis and external-data integration.
- Quantify uncertainty and run sensitivity or robustness checks.
- Review assumptions, alternative explanations, leakage, and limitations.
- Freeze the central question and begin final figures/report early.

### Day 3 — communicate and verify

- Stop adding major scope unless it fixes a clear weakness.
- Finalise the narrative, figures, captions, methods, limitations, and recommendations.
- Have a non-owner reproduce key results and verify every number in the submission.
- Export early, test files on another device, and submit ahead of the deadline.

## Decision log

Keep a simple dated log in the team’s shared notes:

| Date/time | Decision | Evidence/reason | Owner | Revisit? |
|---|---|---|---|---|
| | | | | |

