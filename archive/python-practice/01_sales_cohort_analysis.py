"""
Когортный анализ продаж

Полноценная практическая задача: создаём демонстрационные данные, проводим анализ,
строим график и сохраняем текстовый вывод. Все комментарии на русском.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
FIG_DIR = BASE_DIR / "figures"
REPORT_DIR = BASE_DIR / "reports"
FIG_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)
np.random.seed(101)

def main():
    dates = pd.date_range('2024-01-01', periods=180, freq='D')
    df = pd.DataFrame({'user_id': np.random.randint(1, 500, 3000), 'date': np.random.choice(dates, 3000), 'revenue': np.random.gamma(2, 500, 3000)})
    df['date'] = pd.to_datetime(df['date'])
    first = df.groupby('user_id')['date'].min().rename('first_date')
    df = df.join(first, on='user_id')
    df['cohort'] = df['first_date'].dt.to_period('M').astype(str)
    df['order_month'] = df['date'].dt.to_period('M').astype(str)
    cohort = df.pivot_table(index='cohort', columns='order_month', values='user_id', aggfunc='nunique').fillna(0)
    cohort.to_csv(REPORT_DIR/'cohort_table.csv')
    cohort.sum(axis=1).plot(kind='bar', figsize=(10,5), title='Размер когорт')
    plt.tight_layout(); plt.savefig(FIG_DIR/'cohort_size.png', dpi=160); plt.close()
    conclusion = f'Когорт построено: {cohort.shape[0]}. Самая крупная когорта: {cohort.sum(axis=1).idxmax()}.'
    (REPORT_DIR / "01_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
