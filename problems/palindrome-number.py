# 9. Palindrome Number
# Runtime: 59 ms
# Memory Usage: 16.4 MB
# By https://leetcode.com/jessicaccp/ on Aug 3, 2023

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        end = int(len(x) / 2) - 1
        palindrome = True

        for index, number in enumerate(x):
            if x[index] != x[(-1) * (index + 1)]:
                palindrome = False
                return palindrome

            if (index == end):
                break

        return palindrome