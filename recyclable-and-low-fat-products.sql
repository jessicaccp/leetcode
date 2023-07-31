-- 1757. Recyclable and Low Fat Products
-- Runtime: 1086 ms
-- By https://leetcode.com/jessicaccp/ on Jul 31, 2023

-- Write your MySQL query statement below
SELECT product_id FROM Products WHERE low_fats='Y' AND recyclable='Y'