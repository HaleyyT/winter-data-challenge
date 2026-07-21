from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS = pd.read_csv(ROOT / "reports/tables/material_social_trend_results.csv")
SLOPES = pd.read_csv(ROOT / "reports/tables/method4_country_slope_distribution.csv")
PRIMARY = pd.read_csv(ROOT / "reports/tables/material_social_primary_results.csv")


def test_method4_contains_the_four_prespecified_outcomes_once():
    expected = {"1_1", "2_1", "7_1_DEP", "11_2"}

    assert set(RESULTS["indicator_code"]) == expected
    assert RESULTS["indicator_code"].is_unique
    assert RESULTS["slope_endpoint_agree"].all()


def test_country_comparisons_enforce_coverage_and_common_endpoints():
    assert (SLOPES["n_independent"] >= SLOPES["required_n_independent"]).all()

    for _, group in SLOPES.groupby("indicator_code"):
        australia = group.loc[group["country_code"].eq("AUS")].squeeze()
        assert group["first_time"].eq(australia["first_time"]).all()
        assert group["last_time"].eq(australia["last_time"]).all()


def test_method4_endpoint_changes_match_the_frozen_primary_analysis():
    joined = RESULTS.merge(
        PRIMARY[["indicator_code", "australia_native_change"]],
        on="indicator_code",
        validate="one_to_one",
    )

    np.testing.assert_allclose(
        joined["endpoint_native_change"], joined["australia_native_change"]
    )


def test_inference_and_comparator_percentiles_are_internally_consistent():
    assert RESULTS["kendall_p_raw"].between(0, 1).all()
    assert RESULTS["kendall_p_holm"].between(0, 1).all()
    assert (RESULTS["kendall_p_holm"] >= RESULTS["kendall_p_raw"]).all()

    for _, result in RESULTS.iterrows():
        group = SLOPES.loc[SLOPES["indicator_code"].eq(result["indicator_code"])]
        australia = group.loc[group["country_code"].eq("AUS")].squeeze()
        comparators = group.loc[
            ~group["country_code"].eq("AUS"), "favourable_slope_per_year"
        ]
        percentile = 100 * (
            comparators.lt(australia["favourable_slope_per_year"]).sum()
            + 0.5 * comparators.eq(australia["favourable_slope_per_year"]).sum()
        ) / len(comparators)

        assert len(comparators) == result["n_comparator_countries"]
        assert np.isclose(percentile, result["australia_favourable_slope_percentile"])
