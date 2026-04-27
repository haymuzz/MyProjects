"""
Анализ API-логов

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
np.random.seed(107)

def main():
    n = 4000
    df = pd.DataFrame({'endpoint': np.random.choice(['/auth','/orders','/payments','/profile'], n), 'status': np.random.choice([200,200,200,400,500], n), 'latency_ms': np.random.gamma(2,120,n)})
    err = df.assign(is_error=df.status>=400).groupby('endpoint')['is_error'].mean().sort_values(ascending=False)
    latency = df.groupby('endpoint')['latency_ms'].median().sort_values(ascending=False)
    err.plot(kind='bar', figsize=(8,5), title='Error rate по endpoint')
    plt.tight_layout(); plt.savefig(FIG_DIR/'api_error_rate.png', dpi=160); plt.close()
    conclusion = f'Самый проблемный endpoint по ошибкам: {err.index[0]} ({err.iloc[0]:.2%}). Самый медленный: {latency.index[0]}.'
    (REPORT_DIR / "07_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
