"""Задача 10. Быстрый отчет о качестве данных."""

import pandas as pd


def data_quality_report(df: pd.DataFrame) -> pd.DataFrame:
    total_rows = len(df)
    report = pd.DataFrame({"column": df.columns, "dtype": [str(df[column].dtype) for column in df.columns], "missing_count": [df[column].isna().sum() for column in df.columns], "missing_share": [df[column].isna().mean() for column in df.columns], "unique_count": [df[column].nunique(dropna=True) for column in df.columns], "duplicate_rows_total": df.duplicated().sum(), "rows_total": total_rows})
    return report.sort_values("missing_share", ascending=False)


if __name__ == "__main__":
    df = pd.DataFrame({"client_id": [1, 2, 2, 3], "email": ["a@test.ru", None, None, "c@test.ru"], "revenue": [100, 200, 200, None]})
    print(data_quality_report(df))
