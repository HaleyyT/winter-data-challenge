"""Reproducible cleaning and coverage audit for the supplied OECD data.

The raw CSV is never modified. Run from the repository root:

    python -m src.oecd_audit

Outputs are written to ``data/processed`` and ``reports/tables``. These
generated files are ignored by Git; the implementation and interpretation
notes remain version controlled.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "OECD Data.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
TABLE_DIR = PROJECT_ROOT / "reports" / "tables"

EXPECTED_COLUMNS = {
    "REF_AREA",
    "Reference area",
    "MEASURE",
    "Measure",
    "UNIT_MEASURE",
    "Unit of measure",
    "AGE",
    "SEX",
    "EDUCATION_LEV",
    "DOMAIN",
    "Domain",
    "TIME_PERIOD",
    "OBS_VALUE",
    "OBS_STATUS",
    "Observation status",
}


@dataclass(frozen=True)
class IndicatorSpec:
    direction: str
    indicator_type: str
    frequency: str
    pdf_pages: str
    caveat: str


INDICATOR_SPECS = {
    "1_1": IndicatorSpec(
        "higher",
        "country average",
        "annual",
        "3",
        "National-accounts income includes social transfers in kind and capital consumption; PPP conversion supports level comparison but is not a cash-income measure.",
    ),
    "1_2": IndicatorSpec(
        "lower",
        "vertical inequality",
        "irregular/periodic",
        "4",
        "Household survey or administrative sources differ; both tails of the income distribution can be under-covered or under-reported.",
    ),
    "1_3": IndicatorSpec(
        "higher",
        "country average and vertical inequality",
        "irregular/periodic",
        "4-5",
        "Per-household median excludes private and occupational pensions, is not adjusted for household size, and countries use different CPI classifications.",
    ),
    "2_1": IndicatorSpec(
        "higher",
        "country average",
        "annual",
        "7",
        "Employment means at least one hour of paid work in the reference week; it measures jobholding, not hours, pay, security, or job quality.",
    ),
    "2_2": IndicatorSpec(
        "lower",
        "horizontal inequality",
        "annual/irregular",
        "7-8",
        "The unadjusted gap compares median wages of full-time employees; it does not isolate discrimination and excludes differences driven by employment participation or hours.",
    ),
    "2_7": IndicatorSpec(
        "lower",
        "deprivation",
        "annual",
        "10-11",
        "Threshold-based employee measure; working-time definitions and self-reporting can differ across labour-force surveys.",
    ),
    "3_1": IndicatorSpec(
        "lower",
        "deprivation",
        "irregular/periodic",
        "12",
        "Survey coverage differs and several countries lack information on subsidised tenants; household composition affects the overcrowding definition.",
    ),
    "3_2": IndicatorSpec(
        "higher",
        "country average",
        "annual",
        "12-13",
        "A national-accounts average including imputed owner-occupier rent; it can look stable while renters or low-income households face severe stress. Countries use different COICOP versions.",
    ),
    "4_1": IndicatorSpec(
        "higher",
        "country average",
        "irregular/periodic",
        "14",
        "Time-use surveys differ in survey year, diary design, population coverage, and treatment of simultaneous activities.",
    ),
    "4_3": IndicatorSpec(
        "lower",
        "horizontal inequality",
        "irregular/periodic",
        "14-15",
        "Derived from time-use surveys with sparse, non-aligned years; the sign and composition of paid/unpaid work gaps matter, not only magnitude.",
    ),
    "5_1": IndicatorSpec(
        "higher",
        "country average",
        "annual",
        "16",
        "Period life expectancy applies current age-specific mortality rates to a hypothetical cohort; it is not the predicted lifespan of babies born that year.",
    ),
    "5_3": IndicatorSpec(
        "lower",
        "deprivation",
        "annual",
        "17",
        "Cause-of-death coding and registration practices can differ; the combined outcome hides distinct trends in suicide, alcohol, and drugs.",
    ),
    "6_2": IndicatorSpec(
        "higher",
        "country average",
        "PISA cycle",
        "19-20",
        "PISA covers enrolled 15-year-olds, excluding school dropouts and home-schooled students; cycles are not annual and composition/testing conditions can change.",
    ),
    "7_1_DEP": IndicatorSpec(
        "lower",
        "deprivation",
        "3-year pooled survey windows",
        "21",
        "Gallup samples about 1,000 people per country per year; displayed annual rows repeat pooled 3-year estimates and must not be treated as independent yearly observations.",
    ),
    "7_2": IndicatorSpec(
        "higher",
        "country average",
        "time-use survey waves",
        "21-22",
        "Counts social interaction only when it is the primary activity; survey years and diary methods differ and simultaneous interaction is omitted.",
    ),
    "8_1_DEP": IndicatorSpec(
        "lower",
        "deprivation",
        "survey waves",
        "23",
        "OECD Trust Survey waves are sparse; this is perceived political voice, not an institutional measure of democratic quality.",
    ),
    "8_2": IndicatorSpec(
        "higher",
        "country average",
        "election-based",
        "23",
        "Years reflect different election cycles and election types; compulsory voting in Australia and several peers makes turnout levels structurally non-comparable.",
    ),
    "9_2": IndicatorSpec(
        "lower",
        "country average",
        "annual to 2020",
        "24",
        "A threshold share above 5 micrograms/m3 can saturate near 100% and conceal meaningful differences in pollution concentration.",
    ),
    "9_3": IndicatorSpec(
        "lower",
        "country average",
        "annual",
        "25",
        "Climate and geography create structural cross-country differences; annual extremes are volatile and should not be interpreted from a single year.",
    ),
    "11_1": IndicatorSpec(
        "higher",
        "country average",
        "sparse survey years",
        "26-27",
        "Question wording, scale anchors, sampled ages, and survey methods differ across countries; only two Australian observations are supplied.",
    ),
    "11_2": IndicatorSpec(
        "lower",
        "deprivation",
        "3-year pooled survey windows",
        "27-28",
        "Gallup samples about 1,000 people per country per year; displayed annual rows repeat pooled 3-year estimates and must not be treated as independent yearly observations.",
    ),
}


def pooled_period(indicator_code: str, year: int) -> str:
    """Return the independent observation window represented by a row."""
    if indicator_code not in {"7_1_DEP", "11_2"}:
        return str(year)
    if year == 2010:
        return "2008-10"
    if 2011 <= year <= 2013:
        return "2011-13"
    if 2014 <= year <= 2016:
        return "2014-16"
    if 2017 <= year <= 2019:
        return "2017-19"
    if 2020 <= year <= 2022:
        return "2020-22"
    if 2023 <= year <= 2025:
        return "2023-25"
    return str(year)


def load_clean(path: Path = RAW_FILE) -> pd.DataFrame:
    """Validate and return a tidy analysis copy without changing raw data."""
    if not path.exists():
        raise FileNotFoundError(f"Raw OECD file not found: {path}")

    raw = pd.read_csv(path)
    missing_columns = EXPECTED_COLUMNS.difference(raw.columns)
    if missing_columns:
        raise ValueError(f"Missing expected columns: {sorted(missing_columns)}")
    if raw.duplicated(["REF_AREA", "MEASURE", "TIME_PERIOD"]).any():
        raise ValueError("Duplicate country-indicator-year keys require investigation.")
    if raw["OBS_VALUE"].isna().any():
        raise ValueError("Missing observation values require investigation.")
    unknown = set(raw["MEASURE"]) - set(INDICATOR_SPECS)
    if unknown:
        raise ValueError(f"Add metadata for new indicators: {sorted(unknown)}")

    tidy = raw[
        [
            "REF_AREA",
            "Reference area",
            "MEASURE",
            "Measure",
            "DOMAIN",
            "Domain",
            "TIME_PERIOD",
            "OBS_VALUE",
            "OBS_STATUS",
            "Observation status",
            "UNIT_MEASURE",
            "Unit of measure",
            "BASE_PER",
        ]
    ].rename(
        columns={
            "REF_AREA": "country_code",
            "Reference area": "country",
            "MEASURE": "indicator_code",
            "Measure": "indicator",
            "DOMAIN": "domain_code",
            "Domain": "domain",
            "TIME_PERIOD": "year",
            "OBS_VALUE": "value",
            "OBS_STATUS": "status_code",
            "Observation status": "status",
            "UNIT_MEASURE": "unit_code",
            "Unit of measure": "unit",
            "BASE_PER": "base_period",
        }
    )
    tidy["year"] = pd.to_numeric(tidy["year"], errors="raise").astype("int16")
    tidy["value"] = pd.to_numeric(tidy["value"], errors="raise")
    tidy["is_flagged"] = tidy["status_code"].ne("A")
    tidy["better_direction"] = tidy["indicator_code"].map(
        {code: spec.direction for code, spec in INDICATOR_SPECS.items()}
    )
    tidy["independent_period"] = [
        pooled_period(code, int(year))
        for code, year in zip(tidy["indicator_code"], tidy["year"], strict=True)
    ]
    return tidy.sort_values(["country_code", "indicator_code", "year"]).reset_index(drop=True)


def build_gap_report(data: pd.DataFrame) -> pd.DataFrame:
    """Report calendar gaps without assuming all indicators should be annual."""
    rows: list[dict[str, object]] = []
    for (country_code, indicator_code), group in data.groupby(
        ["country_code", "indicator_code"], sort=True
    ):
        years = sorted(group["year"].unique().tolist())
        expected = set(range(years[0], years[-1] + 1))
        missing = sorted(expected.difference(years))
        spec = INDICATOR_SPECS[indicator_code]
        rows.append(
            {
                "country_code": country_code,
                "country": group["country"].iloc[0],
                "indicator_code": indicator_code,
                "indicator": group["indicator"].iloc[0],
                "frequency": spec.frequency,
                "first_year": years[0],
                "last_year": years[-1],
                "observed_year_count": len(years),
                "independent_period_count": group["independent_period"].nunique(),
                "calendar_gap_count": len(missing),
                "calendar_missing_years": ";".join(map(str, missing)),
                "gap_interpretation": (
                    "potential missing annual observations"
                    if spec.frequency.startswith("annual") and missing
                    else "no internal annual gaps"
                    if spec.frequency.startswith("annual")
                    else "non-annual design: blank years are not automatically missing data"
                ),
            }
        )
    return pd.DataFrame(rows)


def build_coverage_report(data: pd.DataFrame) -> pd.DataFrame:
    """Summarise each country-indicator series and its quality flags."""
    return (
        data.groupby(
            ["country_code", "country", "indicator_code", "indicator"], as_index=False
        )
        .agg(
            first_year=("year", "min"),
            last_year=("year", "max"),
            observed_year_count=("year", "nunique"),
            independent_period_count=("independent_period", "nunique"),
            distinct_value_count=("value", "nunique"),
            flagged_observation_count=("is_flagged", "sum"),
            status_codes=("status_code", lambda x: ";".join(sorted(set(x)))),
        )
        .sort_values(["country_code", "indicator_code"])
    )


def build_country_year_coverage(data: pd.DataFrame) -> pd.DataFrame:
    """Count how many distinct indicators each country reports in each year."""
    return (
        data.groupby(["country_code", "country", "year"], as_index=False)
        .agg(
            indicator_count=("indicator_code", "nunique"),
            flagged_observation_count=("is_flagged", "sum"),
        )
        .sort_values(["country_code", "year"])
    )


def build_same_year_comparisons(data: pd.DataFrame) -> pd.DataFrame:
    """Compare Australia only with countries reporting the same indicator/year."""
    rows: list[dict[str, object]] = []
    for aus_row in data.loc[data["country_code"].eq("AUS")].itertuples(index=False):
        peers = data.loc[
            data["indicator_code"].eq(aus_row.indicator_code)
            & data["year"].eq(aus_row.year)
        ].copy()
        ascending = aus_row.better_direction == "lower"
        peers["favourable_rank"] = peers["value"].rank(
            ascending=ascending, method="average"
        )
        aus_rank = float(
            peers.loc[peers["country_code"].eq("AUS"), "favourable_rank"].iloc[0]
        )
        n = len(peers)
        favourable_percentile = 100.0 if n == 1 else 100 * (n - aus_rank) / (n - 1)
        rows.append(
            {
                "indicator_code": aus_row.indicator_code,
                "indicator": aus_row.indicator,
                "domain": aus_row.domain,
                "year": aus_row.year,
                "independent_period": aus_row.independent_period,
                "australia_value": aus_row.value,
                "australia_status_code": aus_row.status_code,
                "better_direction": aus_row.better_direction,
                "same_year_country_count": n,
                "same_year_median": peers["value"].median(),
                "same_year_q25": peers["value"].quantile(0.25),
                "same_year_q75": peers["value"].quantile(0.75),
                "australia_favourable_rank": aus_rank,
                "australia_favourable_percentile": favourable_percentile,
                "comparison_is_thin": n < 20,
                "any_peer_flagged": bool(peers["is_flagged"].any()),
            }
        )
    return pd.DataFrame(rows).sort_values(["indicator_code", "year"])


def build_indicator_metadata(data: pd.DataFrame) -> pd.DataFrame:
    """Combine OECD definitions metadata with observed coverage."""
    rows: list[dict[str, object]] = []
    for code, group in data.groupby("indicator_code", sort=True):
        spec = INDICATOR_SPECS[code]
        aus = group.loc[group["country_code"].eq("AUS")]
        rows.append(
            {
                "indicator_code": code,
                "indicator": group["indicator"].iloc[0],
                "domain": group["domain"].iloc[0],
                "unit": group["unit"].iloc[0],
                "better_direction": spec.direction,
                "indicator_type": spec.indicator_type,
                "frequency": spec.frequency,
                "country_count": group["country_code"].nunique(),
                "dataset_first_year": group["year"].min(),
                "dataset_last_year": group["year"].max(),
                "australia_first_year": aus["year"].min() if len(aus) else np.nan,
                "australia_last_year": aus["year"].max() if len(aus) else np.nan,
                "australia_row_count": len(aus),
                "australia_independent_period_count": aus["independent_period"].nunique(),
                "status_codes_present": ";".join(sorted(set(group["status_code"]))),
                "definitions_pdf_pages": spec.pdf_pages,
                "comparability_caveat": spec.caveat,
            }
        )
    return pd.DataFrame(rows)


def build_australia_summary(
    data: pd.DataFrame, comparisons: pd.DataFrame, through_year: int = 2024
) -> pd.DataFrame:
    """Create an endpoint and current-position scouting table, not a causal result."""
    rows: list[dict[str, object]] = []
    aus = data.loc[data["country_code"].eq("AUS") & data["year"].le(through_year)]
    for code, group in aus.groupby("indicator_code", sort=True):
        independent = group.drop_duplicates("independent_period", keep="last").sort_values("year")
        first = independent.iloc[0]
        last = independent.iloc[-1]
        matching = comparisons.loc[
            comparisons["indicator_code"].eq(code)
            & comparisons["year"].eq(last["year"])
        ].iloc[0]
        absolute_change = last["value"] - first["value"]
        percent_change = (
            100 * absolute_change / abs(first["value"]) if first["value"] != 0 else np.nan
        )
        direction = INDICATOR_SPECS[code].direction
        favourable_change = absolute_change if direction == "higher" else -absolute_change
        rows.append(
            {
                "indicator_code": code,
                "indicator": first["indicator"],
                "domain": first["domain"],
                "frequency": INDICATOR_SPECS[code].frequency,
                "first_year": int(first["year"]),
                "last_year_through_2024": int(last["year"]),
                "first_value": first["value"],
                "last_value": last["value"],
                "absolute_change": absolute_change,
                "percent_change": percent_change,
                "change_is_favourable": bool(favourable_change > 0),
                "independent_period_count": len(independent),
                "latest_same_year_country_count": int(matching["same_year_country_count"]),
                "latest_same_year_median": matching["same_year_median"],
                "latest_favourable_percentile": matching[
                    "australia_favourable_percentile"
                ],
                "latest_comparison_is_thin": bool(matching["comparison_is_thin"]),
            }
        )
    return pd.DataFrame(rows)


def build_domain_coverage(
    data: pd.DataFrame, country_code: str | None = None, through_year: int = 2024
) -> pd.DataFrame:
    """Summarise coverage by domain without treating pooled rows as independent.

    ``observation_count`` is the number of displayed rows. In contrast,
    ``independent_observation_count`` counts unique country-indicator-period
    combinations and is the appropriate coverage measure for pooled surveys.
    """
    subset = data.loc[data["year"].le(through_year)].copy()
    if country_code is not None:
        subset = subset.loc[subset["country_code"].eq(country_code)].copy()
    if subset.empty:
        raise ValueError("No observations available for the requested domain coverage.")

    independent = subset.drop_duplicates(
        ["country_code", "indicator_code", "independent_period"]
    )
    independent_counts = (
        independent.groupby(["domain_code", "domain"])
        .size()
        .rename("independent_observation_count")
        .reset_index()
    )
    summary = (
        subset.groupby(["domain_code", "domain"], as_index=False)
        .agg(
            indicators=(
                "indicator",
                lambda x: " | ".join(sorted(pd.Series(x).dropna().unique())),
            ),
            indicator_codes=(
                "indicator_code",
                lambda x: " | ".join(sorted(pd.Series(x).dropna().unique())),
            ),
            indicator_count=("indicator_code", "nunique"),
            observation_count=("value", "size"),
            country_count=("country_code", "nunique"),
            first_year=("year", "min"),
            last_year=("year", "max"),
        )
        .merge(independent_counts, on=["domain_code", "domain"], how="left")
    )
    summary["share_of_displayed_rows_pct"] = (
        summary["observation_count"].div(len(subset)).mul(100).round(2)
    )
    summary = summary.sort_values(
        ["independent_observation_count", "domain"], ascending=[False, True]
    ).reset_index(drop=True)
    summary.insert(0, "coverage_rank", summary.index + 1)
    return summary


def write_outputs(data: pd.DataFrame) -> dict[str, Path]:
    """Build and write all auditable outputs."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)

    gaps = build_gap_report(data)
    coverage = build_coverage_report(data)
    country_year = build_country_year_coverage(data)
    comparisons = build_same_year_comparisons(data)
    metadata = build_indicator_metadata(data)
    australia = build_australia_summary(data, comparisons)
    domain_all = build_domain_coverage(data)
    domain_australia = build_domain_coverage(data, country_code="AUS")

    outputs = {
        "clean": PROCESSED_DIR / "oecd_clean.csv",
        "gaps": TABLE_DIR / "time_series_gaps.csv",
        "coverage": TABLE_DIR / "coverage_by_country_indicator.csv",
        "country_year": TABLE_DIR / "coverage_by_country_year.csv",
        "comparisons": TABLE_DIR / "same_year_australia_comparisons.csv",
        "metadata": TABLE_DIR / "indicator_metadata.csv",
        "australia": TABLE_DIR / "australia_indicator_summary.csv",
        "domain_all": TABLE_DIR / "domain_coverage_all.csv",
        "domain_australia": TABLE_DIR / "domain_coverage_australia.csv",
    }
    for frame, key in [
        (data, "clean"),
        (gaps, "gaps"),
        (coverage, "coverage"),
        (country_year, "country_year"),
        (comparisons, "comparisons"),
        (metadata, "metadata"),
        (australia, "australia"),
        (domain_all, "domain_all"),
        (domain_australia, "domain_australia"),
    ]:
        frame.to_csv(outputs[key], index=False)
    return outputs


def main() -> None:
    data = load_clean()
    outputs = write_outputs(data)
    print(
        f"Validated {len(data):,} rows, {data['country_code'].nunique()} countries, "
        f"{data['indicator_code'].nunique()} indicators, "
        f"{int(data['is_flagged'].sum())} flagged observations."
    )
    for name, path in outputs.items():
        print(f"{name:>12}: {path.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
