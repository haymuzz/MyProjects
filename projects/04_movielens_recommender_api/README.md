# MovieLens Recommendation API

## Описание проекта

Рекомендательная система фильмов с REST API и оценкой качества рекомендаций.

## Бизнес-задача

Контентному сервису нужно персонализировать список фильмов, чтобы повысить вовлечение пользователей.

## Датасет

- Kaggle: [MovieLens Dataset](https://www.kaggle.com/datasets/sriharshabsprasad/movielens-dataset-100k-ratings)
- Данные не хранятся в репозитории из-за размера и лицензии Kaggle.
- После скачивания положите файлы в `data/raw/`.

## Что будет сделано

- подготовить ratings, movies и user-item matrix
- построить popularity baseline
- реализовать item-based collaborative filtering
- сравнить baseline и персональные рекомендации
- оценить Precision@K и Recall@K
- завернуть рекомендации в FastAPI endpoint

## Метрики

- Precision@K
- Recall@K
- coverage
- MAP@K
- recommendation diversity

## Стек

Python, pandas, NumPy, scikit-learn, FastAPI, SQLite, SQLAlchemy

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

локальный API-сервис рекомендаций с базой данных и метриками качества.

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
