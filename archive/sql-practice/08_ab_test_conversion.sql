-- Задача 8. Подготовить таблицу конверсии для A/B-теста.
-- Таблица: experiment_events(user_id, group_name, event_name, event_date)

WITH users AS (
    SELECT DISTINCT
        user_id,
        group_name
    FROM experiment_events
    WHERE event_name = 'experiment_start'
),
conversions AS (
    SELECT DISTINCT
        user_id
    FROM experiment_events
    WHERE event_name = 'purchase'
)
SELECT
    u.group_name,
    COUNT(DISTINCT u.user_id) AS users_count,
    COUNT(DISTINCT c.user_id) AS conversions_count,
    ROUND(COUNT(DISTINCT c.user_id)::numeric / NULLIF(COUNT(DISTINCT u.user_id), 0), 4) AS conversion_rate
FROM users u
LEFT JOIN conversions c ON u.user_id = c.user_id
GROUP BY u.group_name
ORDER BY u.group_name;
