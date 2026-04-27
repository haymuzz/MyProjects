"""
Проверки качества данных

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
np.random.seed(106)

def main():
    df = pd.DataFrame({'id': [1,2,2,4,5], 'amount': [100, None, 250, -10, 500], 'status': ['ok','ok','ok','bad',None]})
    checks = pd.Series({'duplicates': df.duplicated('id').sum(), 'missing_values': df.isna().sum().sum(), 'negative_amounts': (df.amount.fillna(0)<0).sum()})
    checks.plot(kind='bar', figsize=(8,5), title='Ошибки качества данных')
    plt.tight_layout(); plt.savefig(FIG_DIR/'data_quality_checks.png', dpi=160); plt.close()
    conclusion = 'Найдены проблемы: ' + ', '.join([f'{k}={v}' for k,v in checks.items()]) + '. Требуется очистка перед аналитикой.'
    (REPORT_DIR / "06_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
