"""
Анализ отзывов клиентов

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
np.random.seed(110)

def main():
    feedback = ['быстрая доставка', 'плохая поддержка', 'удобный сервис', 'дорого', 'отличное качество', 'медленная доставка'] * 80
    df = pd.DataFrame({'feedback': np.random.choice(feedback, 480), 'rating': np.random.choice([1,2,3,4,5], 480, p=[.08,.12,.20,.35,.25])})
    words = df.feedback.str.split().explode().value_counts().head(10)
    words.plot(kind='bar', figsize=(8,5), title='Частотность слов в отзывах')
    plt.tight_layout(); plt.savefig(FIG_DIR/'feedback_words.png', dpi=160); plt.close()
    conclusion = f'Самое частое слово в отзывах: {words.index[0]}. Средний рейтинг: {df.rating.mean():.2f}.'
    (REPORT_DIR / "10_conclusion.md").write_text(conclusion, encoding="utf-8")
    print(conclusion)

if __name__ == "__main__":
    main()
