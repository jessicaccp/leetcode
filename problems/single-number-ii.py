# 137. Single Number II
# Runtime: 62 ms
# Memory Usage: 18.2 MB
# By https://leetcode.com/jessicaccp/ on Jul 31, 2023

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for number in nums:
            if number in count:
                count[number] += 1
                if count[number] == 3:
                    count.pop(number)
            else:
                count[number] = 1

        for key in count.keys():
            return key