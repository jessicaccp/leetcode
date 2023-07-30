# 389. Find the Difference
# Runtime: 49 ms
# Memory Usage: 16.3 MB
# By https://leetcode.com/jessicaccp/ on Jul 29, 2023

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = list(s)

        for char in t:
            try:
                s_list.pop(s_list.index(char))
            except:
                return char