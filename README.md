# Портфолио аналитика данных — Егор Хаймусов

Привет! Меня зовут **Егор Хаймусов**, я **Junior Data Analyst**.

В этом репозитории собраны проекты по аналитике данных, SQL, продуктовым метрикам, ETL, базовому ML и системному анализу. Каждый проект оформлен как полноценный кейс: бизнес-задача, данные, ход анализа, код, SQL-запросы, графики, выводы и дальнейшие улучшения.

## Контакты

- Email: **ha1musov@yandex.ru**
- Telegram: [@thehaymuz](https://t.me/thehaymuz)
- GitHub: [github.com/haymuzz](https://github.com/haymuzz)
- Резюме: [Egor_Khaimusov_Resume.pdf](resume/Egor_Khaimusov_Resume.pdf)

## Навыки

**Python:** pandas, NumPy, matplotlib, scikit-learn, statsmodels, Jupyter  
**SQL:** CTE, joins, оконные функции, витрины, продуктовые метрики  
**Аналитика:** EDA, когортный анализ, RFM, churn, retention, A/B-тесты  
**Data Engineering:** ETL, Airflow, контроль качества данных, автоматизация  
**Системный анализ:** BPMN, AS-IS / TO-BE, требования, пользовательские сценарии

## Featured Projects

| Проект | Описание | Стек |
|---|---|---|
| [Olist Marketplace Product Analytics](olist-marketplace-product-analytics) | Анализ продаж, доставки, отзывов и клиентского опыта маркетплейса | Python, SQL, pandas, matplotlib |
| [Fraud Detection & Risk Scoring](fraud-detection-risk-scoring) | Выявление подозрительных транзакций и расчёт риск-скора | Python, SQL, scikit-learn |
| [Store Sales Forecasting ETL](store-sales-forecasting-etl) | ETL-пайплайн и baseline-прогноз продаж | Python, SQL, Airflow, ML |
| [Telco Retention Experiment Design](telco-retention-experiment-design) | Анализ оттока и дизайн retention-эксперимента | Python, SQL, statsmodels |
| [MovieLens Recommendation API](movielens-recommendation-api) | Прототип рекомендательной системы с API | Python, FastAPI, SQLite |
| [Customer Lifetime Value Segmentation](customer-lifetime-value-segmentation) | RFM-сегментация и оценка ценности клиентов | Python, SQL, clustering |

## Практика

- [Python Practice](archive/python-practice) — 10 самостоятельных задач с обработкой данных, графиками и выводами.
- [SQL Practice](archive/sql-practice) — 10 аналитических SQL-запросов с CTE, оконными функциями и бизнес-метриками.

## Структура репозитория

```text
.
├── README.md
├── requirements.txt
├── resume/
├── docs/
├── archive/
│   ├── python-practice/
│   └── sql-practice/
├── olist-marketplace-product-analytics/
├── fraud-detection-risk-scoring/
├── store-sales-forecasting-etl/
├── telco-retention-experiment-design/
├── movielens-recommendation-api/
└── customer-lifetime-value-segmentation/
```

## Как запустить

```bash
git clone https://github.com/haymuzz/analytics-portfolio.git
cd analytics-portfolio
python -m venv venv
venv\Scriptsctivate
pip install -r requirements.txt
```

Для macOS / Linux:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

Данные Kaggle нужно скачать отдельно и положить в `data/raw` соответствующего проекта. Подробности находятся в `data/README.md` внутри каждого проекта и в [docs/dataset_sources.md](docs/dataset_sources.md).
