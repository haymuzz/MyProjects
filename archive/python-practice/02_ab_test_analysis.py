"""
Анализ A/B-теста

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
np.random.seed(102)

def main():
    n = 6000
    df = pd.DataFrame({'group': np.random.choice(['A','B'], n)})
    df['converted'] = np.where(df['group']=='A', np.random.binomial(1, .095, n), np.random.binomial(1, .112, n))
    result = df.groupby('group')['converted'].agg(['mean','sum','count'])
    lift = result.loc['B','mean'] / result.loc['A','mean'] - 1
    result['mean'].plot(kind='bar', figsize=(8,5), title='Conversion rate по группам')
    plt.ylabel('Conversion rate'); plt.tight_layout(); plt.savefig(FIG_DIR/'ab_conversion.png', dpi=160); plt.close()
    conclusion = f'Конверсия A: {result.loc["A","mean"]:.2%}, B: {result.loc["B","mean"]:.2%}. Относительный uplift: {lift:.2%}.'
    (REPORT_DIR / "02_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
