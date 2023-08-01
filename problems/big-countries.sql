-- 595. Big Countries
-- Runtime: 532 ms
-- By https://leetcode.com/jessicaccp/ on Jul 31, 2023

-- Write your MySQL query statement below
SELECT name, population, area FROM World WHERE area>=3000000 OR population>=25000000