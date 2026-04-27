"""Задача 5. Поиск выбросов методом межквартильного размаха."""

import pandas as pd


def mark_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    result = df.copy()
    q1 = result[column].quantile(0.25)
    q3 = result[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    result["is_outlier"] = (result[column] < lower_bound) | (result[column] > upper_bound)
    result["lower_bound"] = lower_bound
    result["upper_bound"] = upper_bound
    return result


if __name__ == "__main__":
    payments = pd.DataFrame({"payment_id": range(1, 11), "amount": [100, 120, 130, 125, 115, 118, 122, 119, 500, 90]})
    print(mark_outliers_iqr(payments, "amount"))
