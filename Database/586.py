"""
# Write your MySQL query statement below
WITH cnt AS(
    SELECT
        customer_number,
        COUNT(customer_number) AS num_orders
    FROM
        orders
    GROUP BY
        customer_number
    ORDER BY num_orders DESC
)

SELECT
    customer_number
FROM cnt
LIMIT 1
"""