SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS REGEXP'통풍시트|열선시트|가죽시트'
GROUP BY 1
ORDER BY 1