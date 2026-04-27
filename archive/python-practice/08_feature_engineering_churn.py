"""Задача 8. Подготовка признаков для модели оттока."""

import pandas as pd


def make_churn_features(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["avg_monthly_charge"] = result["total_charges"] / result["tenure_months"].replace(0, pd.NA)
    result["avg_monthly_charge"] = result["avg_monthly_charge"].fillna(result["monthly_charges"])
    binary_map = {"Yes": 1, "No": 0}
    for column in ["partner", "dependents", "paperless_billing"]:
        result[column + "_flag"] = result[column].map(binary_map).fillna(0).astype(int)
    result["is_new_customer"] = (result["tenure_months"] <= 3).astype(int)
    result["high_monthly_payment"] = (result["monthly_charges"] > result["monthly_charges"].median()).astype(int)
    return result


if __name__ == "__main__":
    customers = pd.DataFrame({"customer_id": [1, 2, 3], "tenure_months": [1, 12, 0], "monthly_charges": [95, 55, 70], "total_charges": [95, 660, 0], "partner": ["No", "Yes", "No"], "dependents": ["No", "No", "Yes"], "paperless_billing": ["Yes", "No", "Yes"]})
    print(make_churn_features(customers))
