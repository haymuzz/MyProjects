-- Бизнес-метрики для проекта: Customer Lifetime Value & RFM Segmentation
-- Адаптируйте названия таблиц и колонок после загрузки данных Kaggle в PostgreSQL.

-- 1. Количество строк
SELECT COUNT(*) AS rows_total
FROM raw_table;

-- 2. Пример проверки пропусков
SELECT
    COUNT(*) AS rows_total,
    SUM(CASE WHEN key_column IS NULL THEN 1 ELSE 0 END) AS missing_key_column
FROM raw_table;

-- 3. Пример агрегации
SELECT
    DATE_TRUNC('month', event_date) AS month,
    COUNT(*) AS events,
    COUNT(DISTINCT user_id) AS users
FROM fact_events
GROUP BY 1
ORDER BY 1;

-- 4. Пример оконной функции
SELECT
    user_id,
    event_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY user_id
        ORDER BY event_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_amount
FROM fact_events;
