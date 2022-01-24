"""
# Write your MySQL query statement below
SELECT Name AS Customers
FROM Customers
LEFT JOIN (
    SELECT *
    FROM Orders
) orders
ON orders.CustomerId = Customers.Id
WHERE CustomerId IS NULL
"""