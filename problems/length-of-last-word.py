# 58. Length of Last Word
# Runtime: 39 ms
# Memory Usage: 16.3 MB
# By https://leetcode.com/jessicaccp/ on Jul 31, 2023

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])