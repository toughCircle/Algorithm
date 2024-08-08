-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, 
    date_format(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE date_format(DATE_OF_BIRTH, "%m") = "03" AND
    GENDER = "W" AND
    TLNO is not null
ORDER BY MEMBER_ID;