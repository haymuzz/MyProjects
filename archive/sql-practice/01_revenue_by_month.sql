-- Динамика выручки по месяцам
-- Практическая SQL-задача: CTE, агрегации, оконные функции и аналитический вывод.

WITH source_data AS (
    SELECT *
    FROM (VALUES
        (1, DATE '2025-01-05', 'A', 1200.00, 1),
        (2, DATE '2025-01-18', 'B', 3400.00, 0),
        (3, DATE '2025-02-04', 'A', 2100.00, 1),
        (4, DATE '2025-02-21', 'C', 1800.00, 1),
        (5, DATE '2025-03-03', 'B', 4200.00, 0),
        (6, DATE '2025-03-16', 'A', 2600.00, 1),
        (7, DATE '2025-04-02', 'C', 3900.00, 0),
        (8, DATE '2025-04-17', 'B', 3100.00, 1)
    ) AS t(customer_id, event_date, segment, revenue, flag)
),
monthly_metrics AS (
    SELECT
        DATE_TRUNC('month', event_date)::date AS month,
        segment,
        COUNT(*) AS events,
        SUM(revenue) AS revenue,
        AVG(revenue) AS avg_revenue,
        AVG(flag::numeric) AS target_rate
    FROM source_data
    GROUP BY 1, 2
),
ranked AS (
    SELECT
        *,
        SUM(revenue) OVER (PARTITION BY segment ORDER BY month) AS cumulative_revenue,
        RANK() OVER (PARTITION BY month ORDER BY revenue DESC) AS segment_rank
    FROM monthly_metrics
)
SELECT
    month,
    segment,
    events,
    revenue,
    ROUND(avg_revenue, 2) AS avg_revenue,
    ROUND(target_rate, 3) AS target_rate,
    cumulative_revenue,
    segment_rank,
    CASE
        WHEN segment_rank = 1 THEN 'лидер месяца'
        WHEN target_rate >= 0.5 THEN 'сильная конверсия'
        ELSE 'требует проверки'
    END AS analytical_comment
FROM ranked
ORDER BY month, segment_rank;

-- Вывод:
-- Запрос показывает, какие сегменты дают максимальную выручку по месяцам,
-- как меняется накопительная выручка и где стоит дополнительно проверить эффективность.
