# 3. Longest Substring Without Repeating Characters
# Runtime: 62 ms
# Memory Usage: 16.5 MB
# By https://leetcode.com/jessicaccp/ on Jul 29, 2023

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        longest = ""

        for char in s:
            if char in substring:
                if len(substring) > len(longest):
                    longest = substring
                index = substring.find(char) + 1
                substring = substring[index:len(substring)]
                substring += char
            else:
                substring += char
                if len(substring) > len(longest):
                    longest = substring
                    
        return len(longest)