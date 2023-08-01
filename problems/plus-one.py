# 66. Plus One
# Runtime: 49 ms
# Memory Usage: 16.3 MB
# By https://leetcode.com/jessicaccp/ on Jul 30, 2023

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1

            if (digits[i] + one) > 9:
                digits[i] = (digits[i] + one) % 10
                one = 1

                if i == 0:
                    digits = [1] + digits
                    return digits
                    
            else:
                digits[i] = digits[i] + one
                one = 0

        return digits