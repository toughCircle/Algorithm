-- 코드를 입력하세요
WITH RECURSIVE hours AS (
    SELECT 0 AS HOUR  -- Anchor Member: 초기 값 0을 생성
    UNION ALL
    SELECT HOUR + 1   -- Recursive Member: 현재 값에 1을 더하여 다음 값을 생성
    FROM hours
    WHERE HOUR < 23   -- 종료 조건: hour가 23 미만인 동안 반복
)
SELECT h.HOUR,
    COALESCE(COUNT(ANIMAL_ID), 0) AS COUNT
FROM HOURS h
LEFT JOIN (
    SELECT hour(DATETIME) AS hour,
        ANIMAL_ID
    FROM ANIMAL_OUTS
) a ON a.hour = h.HOUR
GROUP BY h.HOUR
ORDER BY h.HOUR;