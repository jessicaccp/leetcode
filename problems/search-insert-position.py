# 35. Search Insert Position
# Runtime: 60 ms
# Memory Usage: 17.2 MB
# By https://leetcode.com/jessicaccp/ on Aug 1, 2023

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while (True):
            middle = int((start + end) / 2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1

            if end < 0:
                if nums[0] > target:
                    return 0
                else:
                    return 1
            elif start == len(nums):
                return len(nums)
            elif start > end:
                if nums[end] > target:
                    return end
                else:
                    return end + 1
