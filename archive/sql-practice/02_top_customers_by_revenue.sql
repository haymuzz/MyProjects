-- Задача 2. Найти топ-10 клиентов по суммарной выручке.
-- Таблица: orders(order_id, customer_id, order_date, revenue, status)

SELECT
    customer_id,
    COUNT(DISTINCT order_id) AS orders_count,
    SUM(revenue) AS total_revenue,
    AVG(revenue) AS avg_order_value
FROM orders
WHERE status = 'paid'
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;
