-- Задача 7. Добавить к заказам оконные метрики клиента.
-- Таблица: orders(order_id, customer_id, order_date, revenue, status)

SELECT
    order_id,
    customer_id,
    order_date,
    revenue,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date, order_id) AS order_number,
    SUM(revenue) OVER (
        PARTITION BY customer_id
        ORDER BY order_date, order_id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue,
    order_date::date - LAG(order_date::date) OVER (PARTITION BY customer_id ORDER BY order_date, order_id) AS days_since_previous_order
FROM orders
WHERE status = 'paid'
ORDER BY customer_id, order_date;
