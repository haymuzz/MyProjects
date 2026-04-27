# Fraud Detection & Risk Scoring

## Описание проекта

ML-проект для выявления подозрительных транзакций и построения risk-score.

## Бизнес-задача

Банку или платежному сервису нужно находить мошеннические операции так, чтобы снижать финансовые потери и не блокировать слишком много нормальных клиентов.

## Датасет

- Kaggle: [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Данные не хранятся в репозитории из-за размера и лицензии Kaggle.
- После скачивания положите файлы в `data/raw/`.

## Что будет сделано

- провести EDA транзакций и сравнить fraud / non-fraud поведение
- оценить дисбаланс классов и выбрать правильные метрики
- построить baseline: Logistic Regression / Random Forest
- улучшить модель через class_weight, undersampling или SMOTE
- подобрать threshold под бизнес-стоимость ошибок
- сформировать risk-score и список транзакций для ручной проверки

## Метрики

- PR-AUC
- ROC-AUC
- Recall@K
- Precision@K
- confusion matrix
- expected fraud loss saved

## Стек

Python, pandas, NumPy, scikit-learn, imbalanced-learn, matplotlib, seaborn

## Структура проекта

```text
.
├── data/
│   ├── raw/              # файлы Kaggle, не добавляются в Git
│   └── processed/        # очищенные данные, не добавляются в Git
├── notebooks/
│   └── 01_analysis.ipynb
├── src/
│   └── README.md
├── sql/
│   └── business_metrics.sql
├── reports/
│   └── figures/
├── docs/
│   └── business_requirements.md
├── requirements.txt
└── README.md
```

## Ожидаемый результат

risk-scoring pipeline, threshold tuning, business-friendly выводы по снижению false negatives.

## Бизнес-эффект

После завершения проект должен отвечать на вопросы:
- какая бизнес-проблема решается;
- какие данные использованы и какие ограничения есть;
- какие метрики рассчитаны;
- какая модель или аналитическая логика построена;
- какие действия бизнес может предпринять на основе результатов.

## Ограничения

- Kaggle-данные могут быть обезличенными, синтетическими или историческими.
- Метрики нужно интерпретировать как демонстрацию аналитического подхода.
- Для production-решения потребуется мониторинг качества данных и модели.

## Следующие шаги

- добавить итоговые графики в `reports/figures/`;
- обновить README фактическими метриками;
- добавить `requirements.txt` с точными версиями;
- оформить краткий executive summary в начале проекта.
