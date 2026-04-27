-- Задача 1. Посчитать месячную выручку и количество заказов.
-- Таблица: orders(order_id, customer_id, order_date, revenue, status)

SELECT
    DATE_TRUNC('month', order_date)::date AS month_start,
    COUNT(DISTINCT order_id) AS orders_count,
    SUM(revenue) AS revenue,
    AVG(revenue) AS avg_order_value
FROM orders
WHERE status = 'paid'
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month_start;
