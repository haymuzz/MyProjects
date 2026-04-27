# Customer Lifetime Value & RFM Segmentation

## Описание проекта

Сегментация клиентов по покупательскому поведению, RFM и потенциальной ценности.

## Бизнес-задача

Команде маркетинга нужно разделить клиентов на сегменты и понять, кому отправлять retention, upsell и win-back коммуникации.

## Датасет

- Kaggle: [Customer Segmentation Dataset / Online Retail](https://www.kaggle.com/datasets/yasserh/customer-segmentation-dataset)
- Данные не хранятся в репозитории из-за размера и лицензии Kaggle.
- После скачивания положите файлы в `data/raw/`.

## Что будет сделано

- очистить транзакции и обработать возвраты/аномалии
- рассчитать Recency, Frequency, Monetary
- построить RFM-сегменты
- обучить KMeans / Agglomerative clustering
- оценить качество кластеров и интерпретировать сегменты
- сформировать action plan по каждому сегменту

## Метрики

- RFM score
- average order value
- purchase frequency
- segment revenue share
- silhouette score

## Стек

Python, pandas, SQL, scikit-learn, clustering, matplotlib

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

понятная сегментация клиентов, CLV-подход и маркетинговые рекомендации.

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
