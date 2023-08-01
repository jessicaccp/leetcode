# 283. Move Zeroes
# Runtime: 6149 ms
# Memory Usage: 17.9 MB
# By https://leetcode.com/jessicaccp/ on Jul 30, 2023

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pos_non_zero = 0
        count_zeros = 0

        for number in nums:
            if number == 0:
                count_zeros += 1
            else:
                nums[pos_non_zero] = number
                number = 0
                pos_non_zero += 1

        for i in range(len(nums) - count_zeros, len(nums)):
            nums[i] = 0