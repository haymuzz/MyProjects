-- Задача 10. Базовые проверки качества данных по заказам.
-- Таблица: orders(order_id, customer_id, order_date, revenue, status)

SELECT
    COUNT(*) AS rows_total,
    COUNT(*) FILTER (WHERE order_id IS NULL) AS missing_order_id,
    COUNT(*) FILTER (WHERE customer_id IS NULL) AS missing_customer_id,
    COUNT(*) FILTER (WHERE order_date IS NULL) AS missing_order_date,
    COUNT(*) FILTER (WHERE revenue IS NULL) AS missing_revenue,
    COUNT(*) FILTER (WHERE revenue < 0) AS negative_revenue_rows,
    COUNT(*) - COUNT(DISTINCT order_id) AS possible_duplicate_order_ids,
    MIN(order_date) AS min_order_date,
    MAX(order_date) AS max_order_date
FROM orders;
