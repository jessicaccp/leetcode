# 896. Monotonic Array
# Runtime: 810 ms
# Memory Usage: 30.7 MB
# By https://leetcode.com/jessicaccp/ on Jul 30, 2023

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        direction = ""

        for i in range(1, len(nums)):
            if direction == "":
                if nums[i] == nums[i - 1]:
                    continue
                elif nums[i] < nums[i - 1]:
                    direction = "dec"
                else:
                    direction = "inc"
            elif direction == "dec":
                if nums[i] > nums[i - 1]:
                    return False
            else:
                if nums[i] < nums[i - 1]:
                    return False

        return True