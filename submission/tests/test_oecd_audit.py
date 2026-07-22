import pandas as pd

from submission.code.oecd_audit import (
    build_gap_report,
    build_domain_coverage,
    build_same_year_comparisons,
    load_clean,
    pooled_period,
)


def test_pooled_periods_are_collapsed() -> None:
    assert pooled_period("7_1_DEP", 2011) == "2011-13"
    assert pooled_period("7_1_DEP", 2013) == "2011-13"
    assert pooled_period("11_2", 2024) == "2023-25"
    assert pooled_period("2_1", 2024) == "2024"


def test_raw_file_has_unique_keys_and_expected_scope() -> None:
    data = load_clean()
    assert len(data) == 8_806
    assert data["country_code"].nunique() == 47
    assert data["indicator_code"].nunique() == 21
    assert not data.duplicated(["country_code", "indicator_code", "year"]).any()


def test_nonannual_blank_years_are_not_labelled_missing() -> None:
    data = load_clean()
    gaps = build_gap_report(data)
    pisa_aus = gaps.loc[
        gaps["country_code"].eq("AUS") & gaps["indicator_code"].eq("6_2")
    ].iloc[0]
    assert pisa_aus["calendar_gap_count"] > 0
    assert pisa_aus["gap_interpretation"].startswith("non-annual design")


def test_australia_comparisons_are_same_indicator_and_year() -> None:
    data = load_clean()
    comparisons = build_same_year_comparisons(data)
    row = comparisons.loc[
        comparisons["indicator_code"].eq("1_1") & comparisons["year"].eq(2024)
    ].iloc[0]
    expected = data.loc[data["indicator_code"].eq("1_1") & data["year"].eq(2024)]
    assert row["same_year_country_count"] == expected["country_code"].nunique()
    assert row["same_year_median"] == expected["value"].median()
    assert pd.notna(row["australia_favourable_percentile"])


def test_domain_coverage_does_not_overcount_pooled_rows() -> None:
    data = load_clean()
    coverage = build_domain_coverage(data, country_code="AUS", through_year=2024)
    social = coverage.loc[coverage["domain"].eq("Social connections")].iloc[0]
    subjective = coverage.loc[coverage["domain"].eq("Subjective well-being")].iloc[0]
    assert social["observation_count"] == 15
    assert social["independent_observation_count"] == 6
    assert subjective["observation_count"] == 17
    assert subjective["independent_observation_count"] == 8
