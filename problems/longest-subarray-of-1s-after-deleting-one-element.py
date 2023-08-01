# 1493. Longest Subarray of 1's After Deleting One Element
# Runtime: 395 ms
# Memory Usage: 19 MB
# By https://leetcode.com/jessicaccp/ on Jul 31, 2023

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        current = 0
        last = 0
        current_delete = 0
        count_zeros = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                current += 1
                current_delete += 1

                if current_delete > longest:
                    longest = current_delete

            else:
                count_zeros += 1

                if i + 1 < len(nums):
                    if nums[i + 1] == 1:
                        current_delete -= last
                        last = current
                        current = 0
                    else:
                        last = 0
                        current = 0
                        current_delete = 0
        
        if count_zeros:
            return longest
        else:
            return longest - 1