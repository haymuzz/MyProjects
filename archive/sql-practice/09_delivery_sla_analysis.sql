-- Задача 9. Проанализировать соблюдение SLA доставки.
-- Таблица: deliveries(order_id, promised_delivery_date, delivered_at, city)

SELECT
    city,
    COUNT(*) AS deliveries_count,
    COUNT(*) FILTER (WHERE delivered_at <= promised_delivery_date) AS on_time_count,
    COUNT(*) FILTER (WHERE delivered_at > promised_delivery_date) AS late_count,
    ROUND(COUNT(*) FILTER (WHERE delivered_at <= promised_delivery_date)::numeric / NULLIF(COUNT(*), 0), 4) AS on_time_rate,
    ROUND(AVG(EXTRACT(epoch FROM delivered_at - promised_delivery_date) / 86400)::numeric, 2) AS avg_delay_days
FROM deliveries
WHERE delivered_at IS NOT NULL
GROUP BY city
ORDER BY on_time_rate ASC, deliveries_count DESC;
