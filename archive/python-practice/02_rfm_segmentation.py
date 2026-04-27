"""Задача 2. RFM-сегментация клиентов по заказам."""

import pandas as pd


def build_rfm(orders: pd.DataFrame, analysis_date: str) -> pd.DataFrame:
    df = orders.copy()
    df["order_date"] = pd.to_datetime(df["order_date"])
    analysis_ts = pd.Timestamp(analysis_date)
    rfm = df.groupby("customer_id").agg(last_order_date=("order_date", "max"), frequency=("order_id", "nunique"), monetary=("revenue", "sum")).reset_index()
    rfm["recency"] = (analysis_ts - rfm["last_order_date"]).dt.days
    rfm["r_score"] = pd.qcut(rfm["recency"].rank(method="first"), 4, labels=[4, 3, 2, 1]).astype(int)
    rfm["f_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
    rfm["m_score"] = pd.qcut(rfm["monetary"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
    rfm["rfm_score"] = rfm["r_score"].astype(str) + rfm["f_score"].astype(str) + rfm["m_score"].astype(str)
    rfm["segment"] = "обычные клиенты"
    rfm.loc[(rfm["r_score"] >= 3) & (rfm["f_score"] >= 3) & (rfm["m_score"] >= 3), "segment"] = "лояльные клиенты"
    rfm.loc[(rfm["r_score"] <= 2) & (rfm["f_score"] >= 3), "segment"] = "нужно вернуть"
    return rfm.sort_values("monetary", ascending=False)


if __name__ == "__main__":
    orders = pd.DataFrame({"customer_id": [1, 1, 2, 3, 3], "order_id": [10, 11, 12, 13, 14], "order_date": ["2025-01-01", "2025-02-10", "2024-12-15", "2025-03-01", "2025-03-10"], "revenue": [1000, 1500, 700, 900, 1100]})
    print(build_rfm(orders, "2025-04-01"))
