-- Задача 5. Подготовить RFM-сегменты клиентов.
-- Таблица: orders(order_id, customer_id, order_date, revenue, status)

WITH customer_metrics AS (
    SELECT
        customer_id,
        CURRENT_DATE - MAX(order_date)::date AS recency_days,
        COUNT(DISTINCT order_id) AS frequency,
        SUM(revenue) AS monetary
    FROM orders
    WHERE status = 'paid'
    GROUP BY customer_id
),
rfm_scores AS (
    SELECT
        customer_id,
        recency_days,
        frequency,
        monetary,
        NTILE(4) OVER (ORDER BY recency_days DESC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(4) OVER (ORDER BY monetary ASC) AS m_score
    FROM customer_metrics
)
SELECT
    *,
    CASE
        WHEN r_score >= 3 AND f_score >= 3 AND m_score >= 3 THEN 'лояльные клиенты'
        WHEN r_score <= 2 AND f_score >= 3 THEN 'нужно вернуть'
        WHEN r_score >= 3 AND frequency = 1 THEN 'новые клиенты'
        ELSE 'обычные клиенты'
    END AS segment
FROM rfm_scores
ORDER BY monetary DESC;
