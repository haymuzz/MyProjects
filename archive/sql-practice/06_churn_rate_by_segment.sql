-- Задача 6. Посчитать churn rate по тарифам или сегментам.
-- Таблица: customers(customer_id, segment, tariff, is_churned)

SELECT
    segment,
    tariff,
    COUNT(*) AS customers_count,
    SUM(is_churned::int) AS churned_count,
    ROUND(AVG(is_churned::int)::numeric, 4) AS churn_rate
FROM customers
GROUP BY segment, tariff
HAVING COUNT(*) >= 30
ORDER BY churn_rate DESC, customers_count DESC;
