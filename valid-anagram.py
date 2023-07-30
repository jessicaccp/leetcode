# 242. Valid Anagram
# Runtime: 65 ms
# Memory Usage: 21.2 MB
# By https://leetcode.com/jessicaccp/ on Jul 29, 2023

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s, key=str.lower))
        t = "".join(sorted(t, key=str.lower))

        if s == t:
            return True
        else:
            return False