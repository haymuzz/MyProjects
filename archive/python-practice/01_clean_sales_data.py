"""Задача 1. Очистка продаж: пропуски, дубликаты, типы и расчет выручки."""

import pandas as pd


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result = result.drop_duplicates()
    result["order_date"] = pd.to_datetime(result["order_date"], errors="coerce")
    result = result.dropna(subset=["order_id", "order_date"])
    result["quantity"] = pd.to_numeric(result["quantity"], errors="coerce").fillna(0)
    result["price"] = pd.to_numeric(result["price"], errors="coerce").fillna(0)
    result.loc[result["quantity"] < 0, "quantity"] = 0
    result.loc[result["price"] < 0, "price"] = 0
    result["revenue"] = result["quantity"] * result["price"]
    return result.sort_values(["order_date", "order_id"]).reset_index(drop=True)


if __name__ == "__main__":
    raw = pd.DataFrame({"order_id": [1, 1, 2, 3], "order_date": ["2025-01-01", "2025-01-01", "bad", "2025-01-03"], "quantity": [2, 2, 1, -3], "price": [100, 100, 250, 400]})
    print(clean_sales_data(raw))
