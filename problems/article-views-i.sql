-- 1148. Article Views I
-- Runtime: 740 ms
-- By https://leetcode.com/jessicaccp/ on Jul 31, 2023

-- Write your MySQL query statement below
SELECT DISTINCT author_id AS id FROM Views WHERE author_id=viewer_id ORDER BY author_id ASC