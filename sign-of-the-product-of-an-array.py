# 1822. Sign of the Product of an Array
# Runtime: 71 ms
# Memory Usage: 16.6 MB
# By https://leetcode.com/jessicaccp/ on Jul 30, 2023

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        
        count = 0
        for number in nums:
            if number < 0:
                count += 1

        if count % 2 == 0:
            return 1
        else:
            return -1