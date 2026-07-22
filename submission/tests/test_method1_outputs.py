from pathlib import Path

import pandas as pd


SUBMISSION_ROOT = Path(__file__).resolve().parents[1]
TABLE_PATH = SUBMISSION_ROOT / "report" / "tables" / "material_social_trajectory_coverage.csv"
FIGURE_PATH = SUBMISSION_ROOT / "report" / "figures" / "material_social_trajectories.png"


def test_method1_outputs_exist_and_are_nonempty() -> None:
    """The principal report visual and its coverage audit must be reproducible."""
    assert TABLE_PATH.is_file()
    assert FIGURE_PATH.is_file()
    assert FIGURE_PATH.stat().st_size > 100_000


def test_method1_coverage_uses_independent_periods_and_excludes_australia() -> None:
    """Coverage must describe comparator countries, not repeated social rows."""
    coverage = pd.read_csv(TABLE_PATH)
    expected_codes = {"1_1", "2_1", "7_1_DEP", "11_2"}

    assert set(coverage["indicator_code"]) == expected_codes
    assert len(coverage) == 42
    assert not coverage.duplicated(["indicator_code", "period"]).any()
    assert coverage["reference_country_count"].between(1, 46).all()

    social = coverage.loc[coverage["indicator_code"].isin({"7_1_DEP", "11_2"})]
    assert social.groupby("indicator_code").size().eq(6).all()
    assert set(social["period"]) == {2009, 2012, 2015, 2018, 2021, 2024}
    assert social["reference_country_count"].eq(46).all()

    latest = coverage.loc[coverage["period"].eq(2024)].set_index("indicator_code")
    assert latest.loc["1_1", "reference_country_count"] == 31
    assert latest.loc["2_1", "reference_country_count"] == 44
