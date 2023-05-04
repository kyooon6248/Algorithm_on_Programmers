-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS 'count'
    FROM ANIMAL_INS
    group by animal_type
    order by animal_type;