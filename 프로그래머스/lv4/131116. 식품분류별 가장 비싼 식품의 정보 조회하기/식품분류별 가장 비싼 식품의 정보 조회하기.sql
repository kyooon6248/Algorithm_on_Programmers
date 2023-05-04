SELECT a.CATEGORY, b.m_price AS MAX_PRICE, a.PRODUCT_NAME
    FROM FOOD_PRODUCT a,
        (SELECT CATEGORY, MAX(price) as m_price
            FROM food_product
            GROUP BY 1
            HAVING category IN ('과자', '국', '김치', '식용유')) b
    WHERE a.price = b.m_price AND a.category = b.category
    ORDER BY 2 DESC