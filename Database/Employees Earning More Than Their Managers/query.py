"""
# Write your MySQL query statement below
WITH managers AS (
    SELECT Salary, Id
    FROM Employee
)

SELECT Name AS Employee
FROM Employee
INNER JOIN managers ON managers.Id = Employee.ManagerId
WHERE managers.Salary < Employee.Salary
"""