"""
# Write your MySQL query statement below
SELECT Person.Email
FROM Person
INNER JOIN (
    SELECT Id, Email, COUNT(*)
    FROM Person
    GROUP BY Email
    HAVING COUNT(*) > 1
) duplicate_rows
ON duplicate_rows.id = Person.Id AND duplicate_rows.Email = Person.Email
"""