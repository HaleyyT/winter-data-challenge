# Data directory

Data files are intentionally excluded from Git. Preserve provenance and keep raw inputs immutable.

| Folder | Purpose |
|---|---|
| `raw/` | Original challenge files, unchanged |
| `external/` | Third-party datasets used for context or enrichment |
| `interim/` | Temporary cleaned or joined files |
| `processed/` | Final analysis-ready datasets |

For every input, record: filename, source URL/provider, retrieval date and timezone, licence/access conditions, checksum if practical, row/column count, and a short description. Document every transformation in code.

