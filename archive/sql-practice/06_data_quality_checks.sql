-- Задача 6: проверки качества данных
-- Полный SQL-сценарий для PostgreSQL.
-- Внутри есть демонстрационные данные, расчёт метрик, оконные функции и аналитический вывод.

WITH source_data AS (
    SELECT * FROM (VALUES
        (1, 'A', DATE '2024-01-01', 1200.0, 1, 14),
        (2, 'A', DATE '2024-01-02', 850.0, 0, 30),
        (3, 'B', DATE '2024-01-03', 1430.0, 1, 9),
        (4, 'B', DATE '2024-01-04', 640.0, 0, 41),
        (5, 'C', DATE '2024-01-05', 2100.0, 1, 7),
        (6, 'C', DATE '2024-01-06', 400.0, 0, 55),
        (7, 'A', DATE '2024-02-01', 980.0, 1, 11),
        (8, 'B', DATE '2024-02-04', 1340.0, 1, 16),
        (9, 'C', DATE '2024-02-07', 760.0, 0, 33)
    ) AS t(user_id, segment, event_date, revenue, target_flag, days_since_last_action)
),
base_metrics AS (
    SELECT
        segment,
        COUNT(DISTINCT user_id) AS users_cnt,
        SUM(revenue) AS revenue_total,
        AVG(revenue) AS avg_revenue,
        AVG(target_flag::numeric) AS target_rate,
        AVG(days_since_last_action) AS avg_days_since_last_action
    FROM source_data
    GROUP BY segment
),
ranked AS (
    SELECT
        *,
        RANK() OVER (ORDER BY revenue_total DESC) AS revenue_rank,
        RANK() OVER (ORDER BY target_rate DESC) AS target_rank
    FROM base_metrics
),
final AS (
    SELECT
        segment,
        users_cnt,
        revenue_total,
        ROUND(avg_revenue::numeric, 2) AS avg_revenue,
        ROUND(target_rate::numeric, 4) AS target_rate,
        ROUND(avg_days_since_last_action::numeric, 2) AS avg_days_since_last_action,
        revenue_rank,
        target_rank,
        CASE
            WHEN revenue_rank = 1 AND target_rank = 1
                THEN 'Вывод: сегмент одновременно лидер по выручке и целевой метрике.'
            WHEN revenue_rank = 1
                THEN 'Вывод: сегмент приносит максимум выручки, его нужно удерживать.'
            WHEN target_rank = 1
                THEN 'Вывод: сегмент показывает лучшую целевую метрику, его можно масштабировать.'
            ELSE 'Вывод: сегмент требует дополнительного анализа и проверки гипотез.'
        END AS analytical_conclusion
    FROM ranked
)
SELECT *
FROM final
ORDER BY revenue_rank;
