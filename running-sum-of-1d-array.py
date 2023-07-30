# 1480. Running Sum of 1d Array
# Runtime: 48 ms
# Memory Usage: 16.4 MB
# By https://leetcode.com/jessicaccp/ on Jul 29, 2023

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        sum = 0
        for num in nums:
            sum += num
            output.append(sum)
        return output