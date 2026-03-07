WITH t1 AS (
    SELECT
        user_pseudo_id,
        event_timestamp_kst,
        LAG(event_timestamp_kst) OVER (
            PARTITION BY user_pseudo_id
            ORDER BY event_timestamp_kst
        ) AS prev_time
    FROM ga
    WHERE user_pseudo_id = 'S3WDQCqLpK'
),
t2 AS (
    SELECT
        user_pseudo_id,
        event_timestamp_kst,
        CASE
            WHEN prev_time IS NULL THEN 1
            WHEN TIMESTAMPDIFF(MINUTE, prev_time, event_timestamp_kst) >= 60 THEN 1
            ELSE 0
        END AS new_session
    FROM t1
),
t3 AS (
    SELECT
        user_pseudo_id,
        event_timestamp_kst,
        SUM(new_session) OVER (
            PARTITION BY user_pseudo_id
            ORDER BY event_timestamp_kst
        ) AS session_no
    FROM t2
)
SELECT
    user_pseudo_id,
    MIN(event_timestamp_kst) AS session_start,
    MAX(event_timestamp_kst) AS session_end
FROM t3
GROUP BY user_pseudo_id, session_no
ORDER BY session_start;