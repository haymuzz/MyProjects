"""Задача 3. Проверка A/B-теста по конверсии."""

import pandas as pd
from statsmodels.stats.proportion import proportions_ztest


def check_ab_test(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby("group").agg(users=("user_id", "nunique"), conversions=("converted", "sum")).reset_index()
    summary["conversion_rate"] = summary["conversions"] / summary["users"]
    ordered = summary.set_index("group").loc[["A", "B"]]
    stat, p_value = proportions_ztest(ordered["conversions"], ordered["users"])
    summary["z_stat"] = stat
    summary["p_value"] = p_value
    summary["significant_5pct"] = p_value < 0.05
    return summary


if __name__ == "__main__":
    data = pd.DataFrame({"user_id": range(1, 201), "group": ["A"] * 100 + ["B"] * 100, "converted": [1] * 12 + [0] * 88 + [1] * 19 + [0] * 81})
    print(check_ab_test(data))
