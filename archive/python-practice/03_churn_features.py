"""
Факторы оттока клиентов

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
np.random.seed(103)

def main():
    n = 2500
    df = pd.DataFrame({'tenure': np.random.randint(1,73,n), 'monthly_fee': np.random.normal(800,220,n), 'support_tickets': np.random.poisson(1.5,n)})
    p = 1/(1+np.exp(-(-2.5 + .004*df['monthly_fee'] - .03*df['tenure'] + .35*df['support_tickets'])))
    df['churn'] = np.random.binomial(1,p)
    corr = df.corr(numeric_only=True)['churn'].drop('churn').sort_values()
    corr.plot(kind='barh', figsize=(8,5), title='Корреляция признаков с churn')
    plt.tight_layout(); plt.savefig(FIG_DIR/'churn_correlations.png', dpi=160); plt.close()
    conclusion = 'Главный положительный фактор риска: ' + corr.idxmax() + f'. Churn rate: {df.churn.mean():.2%}.'
    (REPORT_DIR / "03_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
