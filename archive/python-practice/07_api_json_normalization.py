"""Задача 7. Нормализация вложенного JSON из API."""

import pandas as pd


def normalize_orders_json(payload: list[dict]) -> pd.DataFrame:
    rows = []
    for order in payload:
        for item in order.get("items", []):
            rows.append({"order_id": order.get("order_id"), "customer_id": order.get("customer", {}).get("id"), "city": order.get("customer", {}).get("city"), "created_at": order.get("created_at"), "sku": item.get("sku"), "quantity": item.get("quantity", 0), "price": item.get("price", 0)})
    df = pd.DataFrame(rows)
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["revenue"] = df["quantity"] * df["price"]
    return df


if __name__ == "__main__":
    payload = [{"order_id": 1, "created_at": "2025-01-01", "customer": {"id": 10, "city": "Москва"}, "items": [{"sku": "A", "quantity": 2, "price": 100}]}]
    print(normalize_orders_json(payload))
