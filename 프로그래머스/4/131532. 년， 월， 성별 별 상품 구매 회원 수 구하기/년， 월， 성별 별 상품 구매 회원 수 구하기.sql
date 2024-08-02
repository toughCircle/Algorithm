-- 코드를 입력하세요
SELECT year(o.SALES_DATE) AS YEAR, 
    month(o.SALES_DATE) AS MONTH, 
    GENDER,
    COUNT(DISTINCT u.USER_ID) AS USERS
FROM USER_INFO u
JOIN ONLINE_SALE o ON u.USER_ID = o.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY year(o.SALES_DATE), month(o.SALES_DATE), GENDER
ORDER BY year(o.SALES_DATE), month(o.SALES_DATE), GENDER;