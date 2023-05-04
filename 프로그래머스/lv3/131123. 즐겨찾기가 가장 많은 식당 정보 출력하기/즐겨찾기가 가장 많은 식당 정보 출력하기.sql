SELECT a.FOOD_TYPE, a.REST_ID, a.REST_NAME, b.favorites
    FROM rest_info a,
    (SELECT food_type, max(favorites)AS favorites
        FROM rest_info
        GROUP BY 1) b
    WHERE a.favorites = b.favorites
        AND a.food_type = b.food_type
    ORDER BY food_type DESC