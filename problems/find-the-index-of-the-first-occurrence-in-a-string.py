# 28. Find the Index of the First Occurrence in a String
# Runtime: 39 ms
# Memory Usage: 16.3 MB
# By https://leetcode.com/jessicaccp/ on Jul 29, 2023

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)
        return index