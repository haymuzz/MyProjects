
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
FIG_DIR = BASE_DIR / "reports" / "figures"
REPORT_DIR = BASE_DIR / "reports"
FIG_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

np.random.seed(42)
pd.set_option("display.max_columns", 80)
pd.set_option("display.width", 160)

PROJECT_NAME = "Store Sales Forecasting ETL Pipeline"
SCENARIO = "sales"


def find_csv_files():
    return sorted(RAW_DIR.glob("*.csv"))


def create_demo_data():
    """Создаём демонстрационные данные, чтобы проект запускался без Kaggle-файлов."""
    n = 2500
    dates = pd.date_range("2024-01-01", periods=240, freq="D")

    if SCENARIO == "fraud":
        df = pd.DataFrame({
            "transaction_id": range(1, n + 1),
            "event_date": np.random.choice(dates, n),
            "amount": np.random.gamma(2.2, 120, n),
            "customer_age_days": np.random.randint(1, 2000, n),
            "transactions_last_24h": np.random.poisson(2, n),
        })
        risk = -4 + 0.004 * df["amount"] + 0.35 * df["transactions_last_24h"] - 0.0004 * df["customer_age_days"]
        df["target"] = np.random.binomial(1, 1 / (1 + np.exp(-risk)))
        return df

    if SCENARIO == "telco":
        df = pd.DataFrame({
            "customer_id": range(1, n + 1),
            "tenure": np.random.randint(1, 73, n),
            "monthly_charges": np.random.normal(75, 22, n).clip(20, 140),
            "contract": np.random.choice(["Month-to-month", "One year", "Two year"], n, p=[0.55, 0.25, 0.20]),
            "payment_method": np.random.choice(["Electronic check", "Credit card", "Bank transfer", "Mailed check"], n),
        })
        risk = -2.2 - 0.035 * df["tenure"] + 0.018 * df["monthly_charges"] + (df["contract"] == "Month-to-month") * 1.0
        df["target"] = np.random.binomial(1, 1 / (1 + np.exp(-risk)))
        df["revenue"] = df["monthly_charges"]
        df["event_date"] = np.random.choice(dates, n)
        return df

    if SCENARIO == "recs":
        users = np.arange(1, 401)
        movies = np.arange(1, 151)
        rows = []
        for user in users:
            for movie in np.random.choice(movies, 24, replace=False):
                rows.append([user, movie, np.random.choice([2, 3, 4, 5], p=[0.10, 0.25, 0.40, 0.25])])
        return pd.DataFrame(rows, columns=["user_id", "item_id", "rating"])

    if SCENARIO == "clv":
        df = pd.DataFrame({
            "customer_id": np.random.randint(1, 650, n * 2),
            "invoice_id": [f"INV{i}" for i in range(n * 2)],
            "event_date": np.random.choice(dates, n * 2),
            "quantity": np.random.poisson(3, n * 2) + 1,
            "price": np.random.gamma(2.0, 450, n * 2),
        })
        df["revenue"] = df["quantity"] * df["price"]
        return df

    if SCENARIO == "sales":
        rows = []
        for store in range(1, 9):
            for category in ["grocery", "beverages", "cleaning", "dairy"]:
                base = np.random.randint(120, 260)
                for date in dates:
                    seasonal = 35 * np.sin(2 * np.pi * date.dayofyear / 365)
                    weekend = 35 if date.weekday() >= 5 else 0
                    promo = np.random.binomial(1, 0.18)
                    revenue = max(0, base + seasonal + weekend + promo * 70 + np.random.normal(0, 25))
                    rows.append([date, store, category, promo, revenue])
        return pd.DataFrame(rows, columns=["event_date", "store_id", "category", "promo", "revenue"])

    # Базовый сценарий marketplace/e-commerce.
    df = pd.DataFrame({
        "order_id": range(1, n + 1),
        "customer_id": np.random.randint(1, 850, n),
        "event_date": np.random.choice(dates, n),
        "category": np.random.choice(["electronics", "home", "beauty", "sport", "auto"], n),
        "delivery_days": np.random.randint(2, 22, n),
        "planned_delivery_days": np.random.randint(4, 16, n),
        "review_score": np.random.choice([1, 2, 3, 4, 5], n, p=[0.06, 0.08, 0.15, 0.31, 0.40]),
        "revenue": np.random.gamma(2.4, 650, n),
    })
    df["is_late"] = (df["delivery_days"] > df["planned_delivery_days"]).astype(int)
    return df


def load_data():
    """Загружаем первый CSV из data/raw или создаём demo-data."""
    files = find_csv_files()
    if not files:
        print("Kaggle CSV не найден. Используем демонстрационные данные.")
        return create_demo_data()

    # Для портфолио используем универсальную загрузку: код можно адаптировать под конкретные Kaggle-файлы.
    path = files[0]
    print(f"Загружаем файл: {path.name}")
    df = pd.read_csv(path)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return normalize_columns(df)


def normalize_columns(df):
    """Приводим популярные Kaggle-колонки к единому аналитическому виду."""
    rename_map = {}
    for c in df.columns:
        lc = c.lower()
        if lc in ["class", "churn", "is_fraud", "fraud"]:
            rename_map[c] = "target"
        if lc in ["amount", "price", "sales", "total", "totalcharges", "monthlycharges"]:
            rename_map[c] = "revenue"
        if lc in ["invoicedate", "date", "order_purchase_timestamp", "timestamp"]:
            rename_map[c] = "event_date"
        if lc in ["customerid", "customer_id", "userid", "user_id"]:
            rename_map[c] = "customer_id"
        if lc in ["rating", "review_score"]:
            rename_map[c] = "rating"
    df = df.rename(columns=rename_map)

    if "event_date" in df.columns:
        df["event_date"] = pd.to_datetime(df["event_date"], errors="coerce")
    if "target" in df.columns and df["target"].dtype == "object":
        df["target"] = df["target"].astype(str).str.lower().isin(["yes", "true", "1", "fraud"]).astype(int)
    if "revenue" in df.columns:
        df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    return df


def save_bar(series, title, filename, ylabel="Значение"):
    plt.figure(figsize=(10, 5))
    series.plot(kind="bar")
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, dpi=160)
    plt.close()


def save_hist(series, title, filename, xlabel="Значение"):
    plt.figure(figsize=(10, 5))
    pd.Series(series).dropna().hist(bins=30)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Количество")
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, dpi=160)
    plt.close()


def save_line(df, x, y, title, filename):
    plt.figure(figsize=(10, 5))
    plt.plot(df[x], df[y], marker="o")
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, dpi=160)
    plt.close()


def run_eda(df):
    """Общий EDA-блок: качество данных, пропуски, числовые распределения."""
    print("Размер данных:", df.shape)
    print("Первые строки:")
    print(df.head())
    print("\\nПропуски по колонкам:")
    print(df.isna().sum().sort_values(ascending=False).head(10))

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        print("\\nОписание числовых признаков:")
        print(df[numeric_cols].describe().T)
        for col in numeric_cols[:3]:
            save_hist(df[col], f"Распределение: {col}", f"hist_{col}.png", col)

    if "event_date" in df.columns:
        df["event_date"] = pd.to_datetime(df["event_date"], errors="coerce")
        daily = df.dropna(subset=["event_date"]).groupby(df["event_date"].dt.date).size().reset_index(name="events")
        if len(daily) > 1:
            daily.columns = ["date", "events"]
            save_line(daily, "date", "events", "Динамика количества событий", "events_by_date.png")


def run_business_analysis(df):
    """Сценарный анализ под конкретный проект."""
    findings = []

    if "revenue" in df.columns:
        revenue = pd.to_numeric(df["revenue"], errors="coerce").fillna(0)
        findings.append(f"Совокупная выручка/объём: {revenue.sum():,.0f}.")
        findings.append(f"Среднее значение revenue: {revenue.mean():,.2f}.")
        save_hist(revenue, "Распределение revenue", "revenue_distribution.png", "revenue")

    if "category" in df.columns and "revenue" in df.columns:
        top_categories = df.groupby("category")["revenue"].sum().sort_values(ascending=False).head(10)
        save_bar(top_categories, "Топ категорий по revenue", "top_categories.png", "Revenue")
        findings.append(f"Лидер по revenue: {top_categories.index[0]}.")

    if "target" in df.columns:
        target_rate = pd.to_numeric(df["target"], errors="coerce").mean()
        findings.append(f"Доля целевого события: {target_rate:.2%}.")
        save_bar(df["target"].value_counts().sort_index(), "Баланс целевого события", "target_balance.png", "Количество")

        try:
            from sklearn.model_selection import train_test_split
            from sklearn.linear_model import LogisticRegression
            from sklearn.metrics import roc_auc_score, classification_report
            from sklearn.preprocessing import StandardScaler

            model_df = df.select_dtypes(include="number").dropna()
            if "target" in model_df.columns and model_df["target"].nunique() == 2 and len(model_df) > 100:
                X = model_df.drop(columns=["target"])
                y = model_df["target"].astype(int)
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
                scaler = StandardScaler()
                X_train_s = scaler.fit_transform(X_train)
                X_test_s = scaler.transform(X_test)
                model = LogisticRegression(max_iter=1000, class_weight="balanced")
                model.fit(X_train_s, y_train)
                proba = model.predict_proba(X_test_s)[:, 1]
                auc = roc_auc_score(y_test, proba)
                findings.append(f"ROC-AUC baseline-модели: {auc:.3f}.")
                (REPORT_DIR / "classification_report.txt").write_text(classification_report(y_test, (proba >= 0.5).astype(int)), encoding="utf-8")
                save_hist(proba, "Распределение risk score", "risk_score_distribution.png", "risk score")
        except Exception as exc:
            findings.append(f"ML-блок пропущен: {exc}")

    if SCENARIO == "clv":
        customer_col = "customer_id" if "customer_id" in df.columns else df.columns[0]
        if "event_date" in df.columns and "revenue" in df.columns:
            snapshot = pd.to_datetime(df["event_date"]).max() + pd.Timedelta(days=1)
            rfm = df.dropna(subset=["event_date"]).groupby(customer_col).agg(
                recency=("event_date", lambda x: (snapshot - pd.to_datetime(x).max()).days),
                frequency=("event_date", "count"),
                monetary=("revenue", "sum"),
            )
            rfm["segment_score"] = pd.qcut(rfm["monetary"].rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
            save_bar(rfm["segment_score"].value_counts().sort_index(), "Распределение RFM-сегментов", "rfm_segments.png", "Клиенты")
            findings.append(f"Клиентов в RFM-анализе: {len(rfm)}.")
            findings.append(f"Средний monetary: {rfm['monetary'].mean():,.2f}.")

    if SCENARIO == "recs":
        if {"user_id", "item_id", "rating"}.issubset(df.columns):
            top_items = df.groupby("item_id")["rating"].agg(["mean", "count"]).query("count >= 5").sort_values(["mean", "count"], ascending=False).head(10)
            save_bar(top_items["mean"], "Топ объектов по средней оценке", "top_items_rating.png", "Средняя оценка")
            findings.append(f"Пользователей: {df['user_id'].nunique()}, объектов: {df['item_id'].nunique()}, оценок: {len(df):,}.")
            findings.append(f"Лучший объект по рейтингу: {top_items.index[0] if len(top_items) else 'недостаточно данных'}.")

    if "event_date" in df.columns and "revenue" in df.columns:
        monthly = df.dropna(subset=["event_date"]).copy()
        monthly["month"] = pd.to_datetime(monthly["event_date"]).dt.to_period("M").astype(str)
        monthly = monthly.groupby("month", as_index=False)["revenue"].sum()
        if len(monthly) > 1:
            save_line(monthly, "month", "revenue", "Динамика revenue по месяцам", "monthly_revenue.png")
            findings.append("Построена месячная динамика revenue для оценки тренда.")

    return findings


def write_summary(findings):
    summary = "# Итоговые выводы\\n\\n"
    summary += f"Проект: **{PROJECT_NAME}**.\\n\\n"
    summary += "## Ключевые результаты\\n\\n"
    for item in findings:
        summary += f"- {item}\\n"

    summary += """
## Бизнес-интерпретация

Анализ показывает не только технические метрики, но и практические зоны принятия решений: какие сегменты требуют внимания, где возникают риски, какие показатели стоит вынести в регулярный мониторинг.

## Рекомендации

1. Перенести ключевые расчёты в регулярную SQL-витрину.
2. Добавить автоматические проверки качества данных перед расчётом метрик.
3. Использовать графики из `reports/figures` в README или презентации проекта.
4. Для production-версии заменить демонстрационные данные на актуальные Kaggle CSV в `data/raw`.

## Ограничения

Если Kaggle-данные не загружены, результаты построены на демонстрационной выборке. Это позволяет проверить код, структуру и визуализации, но бизнес-выводы нужно пересчитать после загрузки реального датасета.
"""
    (REPORT_DIR / "summary.md").write_text(summary, encoding="utf-8")
    print(summary)


def main():
    df = load_data()
    run_eda(df)
    findings = run_business_analysis(df)
    write_summary(findings)


if __name__ == "__main__":
    main()
