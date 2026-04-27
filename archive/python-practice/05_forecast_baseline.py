"""Baseline-прогноз продаж.

Самостоятельный мини-кейс: подготовка данных, расчёт метрик, визуализация и вывод.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
FIGURES_DIR = ROOT / "figures"
REPORTS_DIR = ROOT / "reports"
FIGURES_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)

np.random.seed(105)


def build_dataset() -> pd.DataFrame:
    dates = pd.date_range("2025-01-01", periods=120, freq="D")
    rows = []
    for i, date in enumerate(dates):
        channel = np.random.choice(["organic", "paid", "referral", "email"], p=[0.42, 0.28, 0.18, 0.12])
        users = int(np.random.normal(900 + i * 2, 110))
        conversion = np.clip(np.random.normal(0.055 + (channel == "email") * 0.015, 0.012), 0.01, 0.13)
        orders = int(users * conversion)
        avg_check = np.random.normal(2400 + (channel == "paid") * 300, 350)
        revenue = max(0, orders * avg_check)
        cost = users * np.random.uniform(8, 42) if channel != "organic" else users * np.random.uniform(1, 5)
        rows.append([date, channel, users, orders, revenue, cost])
    df = pd.DataFrame(rows, columns=["date", "channel", "users", "orders", "revenue", "marketing_cost"])
    df["conversion_rate"] = df["orders"] / df["users"]
    df["profit"] = df["revenue"] - df["marketing_cost"]
    return df


def analyze(df: pd.DataFrame) -> pd.DataFrame:
    monthly = (
        df.assign(month=df["date"].dt.to_period("M").astype(str))
        .groupby(["month", "channel"], as_index=False)
        .agg(users=("users", "sum"), orders=("orders", "sum"), revenue=("revenue", "sum"), cost=("marketing_cost", "sum"), profit=("profit", "sum"))
    )
    monthly["conversion_rate"] = monthly["orders"] / monthly["users"]
    monthly["romi"] = (monthly["revenue"] - monthly["cost"]) / monthly["cost"]
    return monthly


def plot_results(monthly: pd.DataFrame) -> None:
    pivot = monthly.pivot(index="month", columns="channel", values="revenue")
    pivot.plot(kind="bar", figsize=(10, 5))
    plt.title("Выручка по каналам и месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Выручка")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "forecast_revenue.png", dpi=160)
    plt.close()

    monthly.groupby("channel")["romi"].mean().sort_values().plot(kind="bar", figsize=(8, 4))
    plt.title("Средний ROMI по каналам")
    plt.xlabel("Канал")
    plt.ylabel("ROMI")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "forecast_romi.png", dpi=160)
    plt.close()


def save_report(monthly: pd.DataFrame) -> None:
    best_channel = monthly.groupby("channel")["profit"].sum().idxmax()
    best_conversion = monthly.groupby("channel")["conversion_rate"].mean().idxmax()
    total_revenue = monthly["revenue"].sum()
    report = f"""# Baseline-прогноз продаж

## Итоги

- Общая выручка за период: {total_revenue:,.0f} руб.
- Самый прибыльный канал: **{best_channel}**.
- Лучший канал по конверсии: **{best_conversion}**.
- Для управленческого отчёта стоит отслеживать не только выручку, но и ROMI, прибыль и конверсию.

## Практический вывод

Каналы с высокой выручкой не всегда дают лучший экономический результат. Для принятия решений по бюджету необходимо сравнивать выручку, стоимость привлечения и итоговую прибыль.
"""
    (REPORTS_DIR / "forecast_conclusion.md").write_text(report, encoding="utf-8")


def main() -> None:
    df = build_dataset()
    monthly = analyze(df)
    plot_results(monthly)
    save_report(monthly)
    print(monthly.head(10).to_string(index=False))
    print("Готово: графики сохранены в figures, выводы — в reports.")


if __name__ == "__main__":
    main()
