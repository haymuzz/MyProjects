"""
Бейзлайн прогноза продаж

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
np.random.seed(105)

def main():
    dates = pd.date_range('2024-01-01', periods=240)
    sales = 1000 + np.arange(240)*2 + 120*np.sin(np.arange(240)/7) + np.random.normal(0,45,240)
    df = pd.DataFrame({'date': dates, 'sales': sales})
    df['forecast'] = df['sales'].rolling(14).mean().shift(1)
    test = df.dropna().tail(60)
    mae = (test.sales-test.forecast).abs().mean()
    df.plot(x='date', y=['sales','forecast'], figsize=(10,5), title='Факт и rolling forecast')
    plt.tight_layout(); plt.savefig(FIG_DIR/'forecast_baseline.png', dpi=160); plt.close()
    conclusion = f'MAE rolling-прогноза на последних 60 днях: {mae:.2f}.'
    (REPORT_DIR / "05_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
