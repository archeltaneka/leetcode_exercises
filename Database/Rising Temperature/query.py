"""
# Write your MySQL query statement below
SELECT Weather.Id as id
FROM Weather
JOIN Weather w ON DATEDIFF(Weather.recordDate, w.recordDate) = 1 AND Weather.Temperature > w.Temperature
"""