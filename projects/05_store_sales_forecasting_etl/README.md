# Store Sales Forecasting ETL Pipeline

## Описание проекта

Прогноз продаж и ETL-пайплайн для регулярного обновления аналитики.

## Бизнес-задача

Ритейлу нужно прогнозировать продажи, чтобы управлять запасами, промо и планом закупок.

## Датасет

- Kaggle: [Superstore Sales Dataset / Store Sales Forecasting](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)
- Данные не хранятся в репозитории из-за размера и лицензии Kaggle.
- После скачивания положите файлы в `data/raw/`.

## Что будет сделано

- подготовить временной ряд продаж по категориям и регионам
- проверить сезонность, тренд и выбросы
- построить baseline moving average
- обучить ML-модель для прогноза продаж
- сравнить модели через MAE, RMSE, MAPE
- описать Airflow DAG для регулярного обновления витрины

## Метрики

- MAE
- RMSE
- MAPE
- forecast bias
- sales by category
- inventory risk

## Стек

Python, pandas, SQL, scikit-learn, Airflow, time series, matplotlib

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

forecasting notebook, ETL design, DAG skeleton и monitoring checks.

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
