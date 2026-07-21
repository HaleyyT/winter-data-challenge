from pathlib import Path

import numpy as np
import pandas as pd

from src.oecd_audit import INDICATOR_SPECS, load_clean


ROOT = Path(__file__).resolve().parents[1]
AUSTRALIA = "AUS"
BASE_SEED = 20260721
BOOTSTRAP_REPLICATES = 10_000
PERMUTATIONS = 19_999
MIN_COUNTRIES = 25
ENDPOINTS = {
    "1_1": (2010, 2024, "2010-2024"),
    "2_1": (2010, 2024, "2010-2024"),
    "7_1_DEP": (2010, 2024, "2008-10 to 2023-25 pooled windows"),
    "11_2": (2010, 2024, "2008-10 to 2023-25 pooled windows"),
}
PAIR_SPECS = [
    (
        "income_social_support",
        "1_1",
        "7_1_DEP",
        "Income per person",
        "Lack of social support",
    ),
    (
        "income_negative_affect",
        "1_1",
        "11_2",
        "Income per person",
        "Negative affect",
    ),
    (
        "employment_social_support",
        "2_1",
        "7_1_DEP",
        "Employment rate",
        "Lack of social support",
    ),
    (
        "employment_negative_affect",
        "2_1",
        "11_2",
        "Employment rate",
        "Negative affect",
    ),
]
EXPECTED_PAIR_COUNTS = [31, 31, 43, 43]

DATA = load_clean()
TRACKED_RESULTS = pd.read_csv(ROOT / "reports/tables/material_social_spearman_results.csv")
PRIMARY = pd.read_csv(ROOT / "reports/tables/material_social_primary_results.csv")


def exact_endpoint_changes(frame: pd.DataFrame, code: str) -> pd.DataFrame:
    start, end, period_label = ENDPOINTS[code]
    subset = frame.loc[
        frame.indicator_code.eq(code) & frame.year.isin([start, end])
    ].copy()
    subset = subset.sort_values(["country_code", "year"])
    subset = subset.drop_duplicates(
        ["country_code", "independent_period"], keep="last"
    )
    wide = (
        subset.pivot(index="country_code", columns="year", values="value")
        .reindex(columns=[start, end])
        .dropna()
        .reset_index()
    )
    wide = wide.rename(columns={start: "start_value", end: "end_value"})
    wide["native_change"] = wide.end_value - wide.start_value
    sign = 1 if INDICATOR_SPECS[code].direction == "higher" else -1
    wide["oriented_change"] = wide.native_change * sign
    wide["indicator_code"] = code
    wide["endpoint_period"] = period_label
    return wide


def build_changes() -> dict[str, pd.DataFrame]:
    return {code: exact_endpoint_changes(DATA, code) for code in ENDPOINTS}


def spearman_rho(x: np.ndarray, y: np.ndarray) -> float:
    x_rank = pd.Series(x).rank(method="average").to_numpy()
    y_rank = pd.Series(y).rank(method="average").to_numpy()
    if np.std(x_rank) == 0 or np.std(y_rank) == 0:
        return np.nan
    return float(np.corrcoef(x_rank, y_rank)[0, 1])


def bootstrap_interval(
    x: np.ndarray, y: np.ndarray, rng: np.random.Generator
) -> tuple[float, float, int]:
    estimates = np.empty(BOOTSTRAP_REPLICATES)
    estimates.fill(np.nan)
    for replicate in range(BOOTSTRAP_REPLICATES):
        indices = rng.integers(0, len(x), size=len(x))
        estimates[replicate] = spearman_rho(x[indices], y[indices])
    valid = estimates[np.isfinite(estimates)]
    lower, upper = np.quantile(valid, [0.025, 0.975])
    return float(lower), float(upper), int(len(valid))


def permutation_pvalue(
    x: np.ndarray, y: np.ndarray, observed: float, rng: np.random.Generator
) -> float:
    x_rank = pd.Series(x).rank(method="average").to_numpy()
    y_rank = pd.Series(y).rank(method="average").to_numpy()
    extreme = 0
    for _ in range(PERMUTATIONS):
        permuted = float(np.corrcoef(x_rank, rng.permutation(y_rank))[0, 1])
        extreme += abs(permuted) >= abs(observed) - 1e-12
    return float((extreme + 1) / (PERMUTATIONS + 1))


def holm_adjust(pvalues: pd.Series) -> np.ndarray:
    values = np.asarray(pvalues, dtype=float)
    order = np.argsort(values)
    adjusted_sorted = np.maximum.accumulate(
        (len(values) - np.arange(len(values))) * values[order]
    )
    adjusted = np.empty_like(values)
    adjusted[order] = np.minimum(adjusted_sorted, 1.0)
    return adjusted


def pairwise_changes(
    changes_by_code: dict[str, pd.DataFrame],
    material_code: str,
    social_code: str,
) -> pd.DataFrame:
    material = changes_by_code[material_code][
        ["country_code", "oriented_change"]
    ].rename(columns={"oriented_change": "material_oriented_change"})
    social = changes_by_code[social_code][["country_code", "oriented_change"]].rename(
        columns={"oriented_change": "social_oriented_change"}
    )
    paired = material.merge(social, on="country_code", validate="one_to_one")
    return paired.loc[paired.country_code.ne(AUSTRALIA)].reset_index(drop=True)


def recompute_method5() -> pd.DataFrame:
    changes_by_code = build_changes()
    all_common = None
    for code, changes in changes_by_code.items():
        column = changes[["country_code", "oriented_change"]].rename(
            columns={"oriented_change": code}
        )
        column = column.loc[column.country_code.ne(AUSTRALIA)]
        all_common = (
            column
            if all_common is None
            else all_common.merge(column, on="country_code", validate="one_to_one")
        )
    assert len(all_common) == 31

    seed_sequences = np.random.SeedSequence(BASE_SEED).spawn(2 * len(PAIR_SPECS))
    rows = []
    for pair_index, (
        pair_id,
        material_code,
        social_code,
        material_label,
        social_label,
    ) in enumerate(PAIR_SPECS):
        paired = pairwise_changes(changes_by_code, material_code, social_code)
        x = paired.material_oriented_change.to_numpy()
        y = paired.social_oriented_change.to_numpy()
        rho = spearman_rho(x, y)
        ci_lower, ci_upper, valid_bootstrap = bootstrap_interval(
            x, y, np.random.default_rng(seed_sequences[2 * pair_index])
        )
        raw_p = permutation_pvalue(
            x, y, rho, np.random.default_rng(seed_sequences[2 * pair_index + 1])
        )
        leave_one_out = np.array(
            [spearman_rho(np.delete(x, i), np.delete(y, i)) for i in range(len(x))]
        )
        fixed = all_common[["country_code", material_code, social_code]].dropna()
        fixed_rho = spearman_rho(
            fixed[material_code].to_numpy(), fixed[social_code].to_numpy()
        )
        australia_material = changes_by_code[material_code].loc[
            changes_by_code[material_code].country_code.eq(AUSTRALIA),
            "oriented_change",
        ].iloc[0]
        australia_social = changes_by_code[social_code].loc[
            changes_by_code[social_code].country_code.eq(AUSTRALIA),
            "oriented_change",
        ].iloc[0]
        pattern = (
            "material improved; social outcome deteriorated"
            if australia_material > 0 and australia_social < 0
            else "other direction pattern"
        )
        rows.append(
            {
                "pair_id": pair_id,
                "material_indicator_code": material_code,
                "social_indicator_code": social_code,
                "material_outcome": material_label,
                "social_outcome": social_label,
                "material_endpoint_period": ENDPOINTS[material_code][2],
                "social_endpoint_period": ENDPOINTS[social_code][2],
                "comparator_country_count": len(paired),
                "spearman_rho": rho,
                "bootstrap_ci_lower": ci_lower,
                "bootstrap_ci_upper": ci_upper,
                "bootstrap_valid_replicates": valid_bootstrap,
                "bootstrap_valid_rate": valid_bootstrap / BOOTSTRAP_REPLICATES,
                "permutation_p_raw": raw_p,
                "fixed_common_panel_count": len(fixed),
                "fixed_common_panel_rho": fixed_rho,
                "leave_one_out_rho_min": float(np.nanmin(leave_one_out)),
                "leave_one_out_rho_max": float(np.nanmax(leave_one_out)),
                "leave_one_out_sign_stable": bool(
                    np.all(np.sign(leave_one_out) == np.sign(rho))
                ),
                "australia_material_oriented_change": australia_material,
                "australia_social_oriented_change": australia_social,
                "australia_direction_pattern": pattern,
            }
        )
    results = pd.DataFrame(rows)
    results["permutation_p_holm"] = holm_adjust(results.permutation_p_raw)
    return results[TRACKED_RESULTS.columns]


def test_method5_uses_prespecified_endpoints_and_orientations():
    changes_by_code = build_changes()

    assert set(changes_by_code) == {"1_1", "2_1", "7_1_DEP", "11_2"}
    for code, changes in changes_by_code.items():
        assert changes.country_code.is_unique
        assert changes.start_value.notna().all()
        assert changes.end_value.notna().all()
        sign = 1 if INDICATOR_SPECS[code].direction == "higher" else -1
        np.testing.assert_allclose(changes.oriented_change, sign * changes.native_change)


def test_method5_excludes_australia_and_has_expected_country_counts():
    changes_by_code = build_changes()

    counts = []
    for _, material_code, social_code, _, _ in PAIR_SPECS:
        paired = pairwise_changes(changes_by_code, material_code, social_code)
        assert AUSTRALIA not in paired.country_code.values
        assert paired.country_code.is_unique
        assert paired.material_oriented_change.notna().all()
        assert paired.social_oriented_change.notna().all()
        counts.append(len(paired))

    assert counts == EXPECTED_PAIR_COUNTS


def test_method5_matches_method2_australia_endpoints():
    changes_by_code = build_changes()

    for code, changes in changes_by_code.items():
        australia = changes.loc[changes.country_code.eq(AUSTRALIA)].iloc[0]
        primary = PRIMARY.loc[PRIMARY.indicator_code.eq(code)].iloc[0]
        assert np.isclose(australia.start_value, primary.australia_start_value)
        assert np.isclose(australia.end_value, primary.australia_end_value)
        assert np.isclose(australia.native_change, primary.australia_native_change)


def test_method5_results_bounds_holm_and_interpretation_flags():
    assert TRACKED_RESULTS.pair_id.tolist() == [spec[0] for spec in PAIR_SPECS]
    assert TRACKED_RESULTS.comparator_country_count.tolist() == EXPECTED_PAIR_COUNTS
    assert TRACKED_RESULTS.comparator_country_count.ge(MIN_COUNTRIES).all()
    assert TRACKED_RESULTS.fixed_common_panel_count.tolist() == [31, 31, 31, 31]
    assert TRACKED_RESULTS.spearman_rho.between(-1, 1).all()
    assert TRACKED_RESULTS.bootstrap_ci_lower.between(-1, 1).all()
    assert TRACKED_RESULTS.bootstrap_ci_upper.between(-1, 1).all()
    assert (
        TRACKED_RESULTS.bootstrap_ci_lower <= TRACKED_RESULTS.bootstrap_ci_upper
    ).all()
    assert TRACKED_RESULTS.permutation_p_raw.between(0, 1).all()
    assert TRACKED_RESULTS.permutation_p_holm.between(0, 1).all()
    assert (TRACKED_RESULTS.permutation_p_holm >= TRACKED_RESULTS.permutation_p_raw).all()
    assert TRACKED_RESULTS.bootstrap_valid_rate.ge(0.99).all()
    assert TRACKED_RESULTS.australia_direction_pattern.eq(
        "material improved; social outcome deteriorated"
    ).all()

    recomputed_holm = holm_adjust(TRACKED_RESULTS.permutation_p_raw)
    np.testing.assert_allclose(
        recomputed_holm, TRACKED_RESULTS.permutation_p_holm, rtol=0, atol=1e-12
    )
    assert (
        TRACKED_RESULTS.loc[
            TRACKED_RESULTS.social_indicator_code.eq("11_2"), "permutation_p_holm"
        ]
        < 0.05
    ).all()
    assert (
        TRACKED_RESULTS.loc[
            TRACKED_RESULTS.social_indicator_code.eq("7_1_DEP"), "permutation_p_holm"
        ]
        >= 0.05
    ).all()


def test_method5_tracked_results_are_deterministic():
    recomputed = recompute_method5()

    pd.testing.assert_frame_equal(
        recomputed,
        TRACKED_RESULTS,
        check_dtype=False,
        check_exact=False,
        rtol=1e-12,
        atol=1e-12,
    )
