# Analytics & Data Portfolio

Меня зовут **Егор Хаймусов**. Я **Junior Data Analyst** из Москвы.

Развиваюсь на стыке аналитики данных, продуктового мышления, системного анализа и автоматизации аналитических процессов. Основной фокус: **Python**, **SQL**, **pandas**, **ETL**, продуктовые метрики, A/B-тестирование, базовое машинное обучение и подготовка понятных бизнес-выводов.

В этом портфолио собраны проекты на открытых датасетах Kaggle. Каждый проект оформлен как законченный аналитический кейс: от постановки задачи и подготовки данных до моделей, SQL-запросов, метрик, ограничений и рекомендаций.

Мои контакты:

- Telegram: [@thehaymuz](https://t.me/thehaymuz)
- Email: ha1musov@yandex.ru
- GitHub: [github.com/haymuzz](https://github.com/haymuzz)

## Resume

Актуальное резюме доступно в репозитории:

## [Download resume](resume/Egor_Khaimusov_Resume.pdf)

## Featured Projects

### 1. Olist Marketplace Product Analytics

Продуктовый анализ маркетплейса на данных бразильского e-commerce.

Что сделано:

- рассчитаны метрики заказов, выручки, среднего чека и доставки
- изучена связь сроков доставки, отзывов и клиентского опыта
- выделены категории и регионы с повышенным риском плохих оценок
- подготовлены SQL-запросы для регулярной аналитической отчётности
- сформулированы продуктовые рекомендации для улучшения сервиса

Стек: Python, Pandas, SQL, Matplotlib, Seaborn, Product Analytics

[Открыть проект](olist-marketplace-product-analytics)

---

### 2. Fraud Detection & Risk Scoring

Модель выявления подозрительных транзакций и расчёт риск-скора.

Что сделано:

- проведён EDA транзакций и анализ дисбаланса классов
- построены baseline и ML-модели классификации
- рассчитаны ROC-AUC, PR-AUC, Precision и Recall
- подобран threshold под разные бизнес-сценарии
- подготовлена логика риск-скоринга для приоритизации проверок

Стек: Python, Pandas, Scikit-learn, SQL, Risk Scoring

[Открыть проект](fraud-detection-risk-scoring)

---

### 3. Store Sales Forecasting ETL Pipeline

ETL-пайплайн и прогнозирование продаж магазинов на временных рядах.

Что сделано:

- описан процесс загрузки, очистки и валидации данных
- подготовлены витрины по магазинам, категориям и датам
- реализована структура ETL-процесса и Airflow DAG
- построена baseline-модель прогноза продаж
- рассчитаны MAE, RMSE и MAPE

Стек: Python, SQL, Pandas, Apache Airflow, Time Series, ETL

[Открыть проект](store-sales-forecasting-etl)

---

### 4. Telco Retention Experiment Design

Анализ оттока клиентов телеком-компании и дизайн retention-эксперимента.

Что сделано:

- проведён EDA клиентской базы
- рассчитаны churn rate и метрики удержания
- выделены сегменты клиентов с высоким риском оттока
- построена модель для оценки вероятности churn
- описан дизайн A/B-теста для проверки retention-механик

Стек: Python, Pandas, SQL, Scikit-learn, Statsmodels, A/B testing

[Открыть проект](telco-retention-experiment-design)

---

### 5. MovieLens Recommendation API

Рекомендательная система фильмов с REST API.

Что сделано:

- подготовлены данные о пользователях, фильмах и оценках
- построена baseline-рекомендательная логика
- рассчитаны top-K рекомендации для пользователей
- подготовлена SQLite-база и структура API
- реализован демонстрационный FastAPI-сервис

Стек: Python, FastAPI, SQLite, SQLAlchemy, Pandas, Scikit-learn

[Открыть проект](movielens-recommendation-api)

---

### 6. Customer Lifetime Value & RFM Segmentation

Сегментация клиентов и оценка клиентской ценности на retail-данных.

Что сделано:

- рассчитаны Recency, Frequency и Monetary
- построены RFM-сегменты
- выделены группы клиентов по ценности и риску потери
- применена кластеризация для поиска поведенческих сегментов
- сформулированы CRM-рекомендации по удержанию и реактивации

Стек: Python, Pandas, SQL, Scikit-learn, Clustering, CRM Analytics

[Открыть проект](customer-lifetime-value-segmentation)

---

## Archive

- [Python Practice](archive/python-practice)
- [SQL Practice](archive/sql-practice)

---

## Skills

Analytics: Product Analytics, A/B testing, Retention, Cohort Analysis, Churn Analysis, RFM, LTV, Customer Segmentation

ML: Classification, Feature Engineering, Logistic Regression, Tree-based Models, Clustering, Forecasting, Recommendation Systems, ROC-AUC, PR-AUC, Precision@K

Data: SQL, PostgreSQL, Greenplum, ETL/ELT, Data Quality, Analytical Reporting

Tools: Python, Pandas, NumPy, Jupyter, Git, Apache Airflow, FastAPI, SQLite, Jira, Confluence

System Analysis: BPMN, UML, AS-IS / TO-BE, Requirements, Use Cases, Business Processes

---

## About

В портфолио собраны проекты по аналитике данных, продуктовой аналитике, машинному обучению, ETL и системному анализу.

Цель портфолио — показать практический подход к работе аналитика: понять бизнес-задачу, подготовить данные, рассчитать метрики, проверить гипотезы, построить модель, описать ограничения и предложить действия для бизнеса.

## Полноценные исполняемые коды

В каждом проекте добавлен файл `src/full_analysis.py`.

Он запускается от начала до конца:

```bash
python src/full_analysis.py
```

Что делает код:

- загружает Kaggle CSV из `data/raw`;
- если CSV ещё не скачан, создаёт демонстрационный датасет;
- проводит EDA и проверки качества данных;
- считает бизнес-метрики;
- строит графики в `reports/figures`;
- сохраняет итоговые выводы в `reports/summary.md`.

Также в архиве обновлены практические разделы:

- `archive/python-practice` — 10 полноценных Python-задач с графиками и выводами;
- `archive/sql-practice` — 10 SQL-задач с CTE, метриками, оконными функциями и аналитическими выводами.
