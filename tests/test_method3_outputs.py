from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP_PATH = ROOT / "reports" / "tables" / "material_social_bootstrap_results.csv"
PLACEBO_PATH = ROOT / "reports" / "tables" / "material_social_placebo_results.csv"
PRIMARY_PATH = ROOT / "reports" / "tables" / "material_social_primary_results.csv"
FIGURE_PATH = ROOT / "reports" / "figures" / "material_social_comparative_gaps.png"
ORDER = ["1_1", "2_1", "7_1_DEP", "11_2"]
COUNTS = [31, 43, 46, 46]


def load_outputs():
    return (
        pd.read_csv(BOOTSTRAP_PATH),
        pd.read_csv(PLACEBO_PATH),
        pd.read_csv(PRIMARY_PATH),
    )


def test_method3_outputs_exist_with_one_row_per_prespecified_outcome():
    assert BOOTSTRAP_PATH.exists()
    assert PLACEBO_PATH.exists()
    assert FIGURE_PATH.exists() and FIGURE_PATH.stat().st_size > 0

    bootstrap, placebo, _ = load_outputs()
    for table in (bootstrap, placebo):
        assert table["indicator_code"].tolist() == ORDER
        assert table["indicator_code"].is_unique
        assert table["eligible_comparator_country_count"].tolist() == COUNTS


def test_bootstrap_design_and_oriented_gaps_reconcile_with_method2():
    bootstrap, _, primary = load_outputs()
    assert bootstrap["bootstrap_replicates"].eq(10_000).all()
    assert bootstrap["random_seed"].eq(20260720).all()

    expected_gaps = np.array([-956.0, -0.864, -4.290870, -2.662420])
    np.testing.assert_allclose(
        bootstrap["observed_oriented_gap"], expected_gaps, atol=1e-5
    )
    merged = bootstrap.merge(
        primary[["indicator_code", "australia_minus_comparator_median_oriented"]],
        on="indicator_code",
        validate="one_to_one",
    )
    np.testing.assert_allclose(
        merged["observed_oriented_gap"],
        merged["australia_minus_comparator_median_oriented"],
    )

    social = bootstrap.loc[bootstrap["indicator_code"].isin(["7_1_DEP", "11_2"])]
    assert social["australia_oriented_change"].lt(0).all()


def test_bootstrap_intervals_and_sensitivity_labels_follow_the_prespecified_rule():
    bootstrap, _, _ = load_outputs()
    expected_bootstrap = np.array([
        [-956.000000, -2610.000000, 1164.000000],
        [-0.864000, -2.065000, 0.173000],
        [-4.290870, -5.435042, -2.787553],
        [-2.662420, -3.772186, -1.249916],
    ])
    np.testing.assert_allclose(
        bootstrap[["bootstrap_gap_median", "bootstrap_ci_lower", "bootstrap_ci_upper"]],
        expected_bootstrap,
        atol=1e-6,
    )
    assert (bootstrap["bootstrap_ci_lower"] <= bootstrap["bootstrap_gap_median"]).all()
    assert (bootstrap["bootstrap_gap_median"] <= bootstrap["bootstrap_ci_upper"]).all()
    expected_crosses_zero = (
        bootstrap["bootstrap_ci_lower"].le(0) & bootstrap["bootstrap_ci_upper"].ge(0)
    )
    assert bootstrap["interval_crosses_zero"].tolist() == expected_crosses_zero.tolist()
    expected_labels = np.where(expected_crosses_zero, "comparator-sensitive", "comparatively stable")
    assert bootstrap["sensitivity_label"].tolist() == expected_labels.tolist()


def test_placebo_counts_and_percentiles_are_consistent_with_method2():
    _, placebo, primary = load_outputs()
    assert placebo["australia_favourable_percentile"].between(0, 100).all()
    counted = (
        placebo["more_favourable_country_count"]
        + placebo["less_favourable_country_count"]
        + placebo["tied_country_count"]
    )
    assert counted.tolist() == placebo["eligible_comparator_country_count"].tolist()

    merged = placebo.merge(
        primary[["indicator_code", "australia_favourable_percentile"]],
        on="indicator_code",
        validate="one_to_one",
        suffixes=("_placebo", "_method2"),
    )
    np.testing.assert_allclose(
        merged["australia_favourable_percentile_placebo"],
        merged["australia_favourable_percentile_method2"],
    )
