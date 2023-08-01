# 374. Guess Number Higher or Lower
# Runtime: 34 ms
# Memory Usage: 16.2 MB
# By https://leetcode.com/jessicaccp/ on Aug 1, 2023

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        start = 1
        end = n

        while True:
            num = int((start + end) / 2)

            if guess(num) == 0:
                return num
            elif guess(num) == -1:
                end = num - 1
            else:
                start = num + 1

            if end < 1 and guess(1) == 0:
                return 1
            elif start > n and guess(n) == 0:
                return n
            elif start == end:
                return start