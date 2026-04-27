"""
Анализ продуктовой воронки

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
np.random.seed(108)

def main():
    steps = ['visit','signup','activation','purchase']
    users = pd.Series({'visit': 10000, 'signup': 3800, 'activation': 2100, 'purchase': 850})
    conv = users / users.iloc[0]
    conv.plot(kind='bar', figsize=(8,5), title='Конверсия воронки от первого шага')
    plt.ylabel('Conversion'); plt.tight_layout(); plt.savefig(FIG_DIR/'product_funnel.png', dpi=160); plt.close()
    drop = (1 - users.shift(-1)/users).dropna().sort_values(ascending=False)
    conclusion = f'Самое большое падение после шага {drop.index[0]}: drop-off {drop.iloc[0]:.2%}.'
    (REPORT_DIR / "08_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
