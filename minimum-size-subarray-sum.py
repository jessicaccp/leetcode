# 209. Minimum Size Subarray Sum
# Runtime: 452 ms
# Memory Usage: 29.6 MB
# By https://leetcode.com/jessicaccp/ on Jul 31, 2023


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minor = 100000
        current = []
        current_sum = 0

        for number in nums:
            if number >= target:
                return 1
            else:
                current.append(number)
                current_sum += number

                if current_sum >= target:
                    while(True):
                        if current_sum - current[0] >= target: 
                            current_sum -= current[0]
                            current.pop(0)
                        else:
                            break
            if current_sum >= target:
                if len(current) < minor:
                    minor = len(current)

        if current_sum >= target:
            return minor
        else:
            return 0