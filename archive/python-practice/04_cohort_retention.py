"""Задача 4. Когортный анализ удержания пользователей."""

import pandas as pd


def build_retention_matrix(events: pd.DataFrame) -> pd.DataFrame:
    df = events.copy()
    df["event_date"] = pd.to_datetime(df["event_date"])
    df["event_month"] = df["event_date"].dt.to_period("M")
    first_month = df.groupby("user_id")["event_month"].min().rename("cohort_month")
    df = df.join(first_month, on="user_id")
    df["period_number"] = (df["event_month"] - df["cohort_month"]).apply(lambda value: value.n)
    cohorts = df.groupby(["cohort_month", "period_number"])["user_id"].nunique().reset_index(name="active_users")
    sizes = cohorts[cohorts["period_number"] == 0][["cohort_month", "active_users"]].rename(columns={"active_users": "cohort_size"})
    cohorts = cohorts.merge(sizes, on="cohort_month")
    cohorts["retention"] = cohorts["active_users"] / cohorts["cohort_size"]
    return cohorts.pivot(index="cohort_month", columns="period_number", values="retention").round(3)


if __name__ == "__main__":
    events = pd.DataFrame({"user_id": [1, 1, 2, 3, 3], "event_date": ["2025-01-05", "2025-02-07", "2025-01-20", "2025-02-01", "2025-03-02"]})
    print(build_retention_matrix(events))
