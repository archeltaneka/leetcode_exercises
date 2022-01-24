"""
# Write your MySQL query statement below
DELETE p.*
FROM Person p, Person p2
WHERE p.Email = p2.Email AND p.Id > p2.Id
"""