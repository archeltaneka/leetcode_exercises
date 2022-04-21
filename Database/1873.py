"""
# Write your MySQL query statement below
SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 AND lower(name) NOT LIKE 'm%' THEN salary
        ELSE 0
    END AS bonus
FROM
    Employees

"""