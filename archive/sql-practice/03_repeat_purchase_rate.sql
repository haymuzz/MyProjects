-- Задача 3. Посчитать долю клиентов с повторной покупкой.
-- Таблица: orders(order_id, customer_id, order_date, status)

WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(DISTINCT order_id) AS orders_count
    FROM orders
    WHERE status = 'paid'
    GROUP BY customer_id
)
SELECT
    COUNT(*) AS customers_total,
    COUNT(*) FILTER (WHERE orders_count >= 2) AS repeat_customers,
    ROUND(COUNT(*) FILTER (WHERE orders_count >= 2)::numeric / NULLIF(COUNT(*), 0), 4) AS repeat_purchase_rate
FROM customer_orders;
