# 20. Valid Parentheses
# Runtime: 42 ms
# Memory Usage: 16.4 MB
# By https://leetcode.com/jessicaccp/ on Jul 29, 2023

def getLeft(char):
    if char == ')':
        return '('
    if char == '}':
        return '{'
    if char == ']':
        return '['
    return ""

class Solution:
    def isValid(self, s: str) -> bool:
        index = 0
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []

        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if len(stack):
                    if stack[-1] == getLeft(char):
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack) > 0:
            return False
        return True
