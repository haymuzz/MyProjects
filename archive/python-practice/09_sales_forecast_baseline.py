"""Задача 9. Бейзлайн-прогноз продаж по скользящему среднему."""

import pandas as pd


def moving_average_forecast(df: pd.DataFrame, window: int = 7) -> pd.DataFrame:
    result = df.copy()
    result["date"] = pd.to_datetime(result["date"])
    result = result.sort_values("date")
    result["forecast"] = result["sales"].shift(1).rolling(window=window, min_periods=1).mean()
    result["absolute_error"] = (result["sales"] - result["forecast"]).abs()
    return result


if __name__ == "__main__":
    sales = pd.DataFrame({"date": pd.date_range("2025-01-01", periods=10), "sales": [100, 120, 115, 130, 125, 140, 150, 160, 155, 170]})
    print(moving_average_forecast(sales, window=3))
