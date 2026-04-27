"""
Unit-экономика

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
np.random.seed(109)

def main():
    df = pd.DataFrame({'channel': ['SEO','Ads','Referral','CRM'], 'cac': [300, 850, 420, 120], 'arppu': [950, 1200, 1100, 700], 'margin': [.42,.38,.40,.45], 'retention_months': [5,4,6,3]})
    df['ltv'] = df.arppu * df.margin * df.retention_months
    df['ltv_cac'] = df.ltv / df.cac
    df.set_index('channel')['ltv_cac'].plot(kind='bar', figsize=(8,5), title='LTV/CAC по каналам')
    plt.tight_layout(); plt.savefig(FIG_DIR/'ltv_cac.png', dpi=160); plt.close()
    best = df.sort_values('ltv_cac', ascending=False).iloc[0]
    conclusion = f'Лучший канал по LTV/CAC: {best.channel}, коэффициент {best.ltv_cac:.2f}.'
    (REPORT_DIR / "09_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
