"""
RFM-сегментация

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
np.random.seed(104)

def main():
    df = pd.DataFrame({'customer_id': np.random.randint(1,700,5000), 'date': np.random.choice(pd.date_range('2024-01-01', periods=300), 5000), 'amount': np.random.gamma(2,450,5000)})
    snapshot = pd.to_datetime(df.date).max() + pd.Timedelta(days=1)
    rfm = df.groupby('customer_id').agg(recency=('date', lambda x: (snapshot-pd.to_datetime(x).max()).days), frequency=('date','count'), monetary=('amount','sum'))
    rfm['score'] = pd.qcut(rfm['monetary'], 4, labels=[1,2,3,4]).astype(int) + pd.qcut(rfm['frequency'], 4, labels=[1,2,3,4]).astype(int)
    rfm['score'].value_counts().sort_index().plot(kind='bar', title='Распределение RFM score', figsize=(8,5))
    plt.tight_layout(); plt.savefig(FIG_DIR/'rfm_score.png', dpi=160); plt.close()
    conclusion = f'Самый ценный клиентский score: {rfm.score.max()}, клиентов в нём: {(rfm.score==rfm.score.max()).sum()}.'
    (REPORT_DIR / "04_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
