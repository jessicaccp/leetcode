-- 584. Find Customer Referee
-- Runtime: 869 ms
-- By https://leetcode.com/jessicaccp/ on Jul 31, 2023

-- Write your MySQL query statement below
SELECT name FROM Customer WHERE referee_id IS NULL OR referee_id!=2