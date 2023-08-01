-- 1683. Invalid Tweets
-- Runtime: 1465 ms
-- By https://leetcode.com/jessicaccp/ on Jul 31, 2023

-- Write your MySQL query statement below
SELECT tweet_id FROM Tweets WHERE LENGTH(content)>15