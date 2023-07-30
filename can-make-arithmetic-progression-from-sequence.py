# 1502. Can Make Arithmetic Progression From Sequence
# Runtime: 50 ms
# Memory Usage: 16.4 MB
# By https://leetcode.com/jessicaccp/ on Jul 30, 2023

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()
        for i in range(0, len(arr)):
            if i == 0:
                continue
            elif i == 1:
                diff = arr[i] - arr[i - 1]
            elif arr[i] - arr[i - 1] != diff:
                    return False

        return True