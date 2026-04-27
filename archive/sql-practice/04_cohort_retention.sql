-- Задача 4. Построить месячное удержание клиентов по когортам.
-- Таблица: events(user_id, event_date, event_name)

WITH user_activity AS (
    SELECT DISTINCT
        user_id,
        DATE_TRUNC('month', event_date)::date AS activity_month
    FROM events
),
cohorts AS (
    SELECT
        user_id,
        MIN(activity_month) AS cohort_month
    FROM user_activity
    GROUP BY user_id
),
retention AS (
    SELECT
        c.cohort_month,
        a.activity_month,
        EXTRACT(year FROM AGE(a.activity_month, c.cohort_month)) * 12
            + EXTRACT(month FROM AGE(a.activity_month, c.cohort_month)) AS period_number,
        COUNT(DISTINCT a.user_id) AS active_users
    FROM user_activity a
    JOIN cohorts c ON a.user_id = c.user_id
    GROUP BY c.cohort_month, a.activity_month
),
cohort_sizes AS (
    SELECT
        cohort_month,
        active_users AS cohort_size
    FROM retention
    WHERE period_number = 0
)
SELECT
    r.cohort_month,
    r.period_number,
    r.active_users,
    cs.cohort_size,
    ROUND(r.active_users::numeric / NULLIF(cs.cohort_size, 0), 4) AS retention_rate
FROM retention r
JOIN cohort_sizes cs ON r.cohort_month = cs.cohort_month
ORDER BY r.cohort_month, r.period_number;
