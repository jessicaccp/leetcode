# 459. Repeated Substring Pattern
# Runtime: 168 ms
# Memory Usage: 16.6 MB
# By https://leetcode.com/jessicaccp/ on Jul 30, 2023

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substring = ""
        multiple_sub = ""

        for char in s:
            substring += char
            if len(s) % len(substring) == 0:
                if len(s) / len(substring) != 1:
                    multiple_sub = ""
                    for i in range(0, int(len(s) / len(substring))):
                        multiple_sub += substring
                    if multiple_sub == s:
                        return True

        return False