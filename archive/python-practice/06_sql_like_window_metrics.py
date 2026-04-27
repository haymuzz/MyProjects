"""Задача 6. Оконные метрики в pandas в стиле SQL."""

import pandas as pd


def add_window_metrics(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["order_date"] = pd.to_datetime(result["order_date"])
    result = result.sort_values(["customer_id", "order_date", "order_id"])
    result["order_number"] = result.groupby("customer_id").cumcount() + 1
    result["cumulative_revenue"] = result.groupby("customer_id")["revenue"].cumsum()
    result["previous_order_date"] = result.groupby("customer_id")["order_date"].shift(1)
    result["days_since_previous_order"] = (result["order_date"] - result["previous_order_date"]).dt.days
    return result


if __name__ == "__main__":
    orders = pd.DataFrame({"customer_id": [1, 1, 2, 1], "order_id": [101, 102, 201, 103], "order_date": ["2025-01-01", "2025-01-10", "2025-01-05", "2025-02-01"], "revenue": [1000, 500, 700, 1200]})
    print(add_window_metrics(orders))
