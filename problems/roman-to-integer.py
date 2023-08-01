# 13. Roman to Integer
# Runtime: 58 ms
# Memory Usage: 16.3 MB
# By https://leetcode.com/jessicaccp/ on Jul 30, 2023

def getValue(number):
    if number == 'I':
        return 1
    elif number == 'V':
        return 5
    elif number == 'X':
        return 10
    elif number == 'L':
        return 50
    elif number == 'C':
        return 100
    elif number == 'D':
        return 500
    else:
        return 1000

def previousIsHigher(current, last):
    if current == 'I':
        return True
    elif current == 'V':
        if last in ['I']:
            return False
        else:
            return True
    elif current == 'X':
        if last in ['I', 'V']:
            return False
        else:
            return True
        return 10
    elif current == 'L':
        if last in ['I', 'V', 'X']:
            return False
        else:
            return True
    elif current == 'C':
        if last in ['I', 'V', 'X', 'L']:
            return False
        else:
            return True
    elif current == 'D':
        if last in ['I', 'V', 'X', 'L', 'C']:
            return False
        else:
            return True
    else:
        if last in ['I', 'V', 'X', 'L', 'C', 'D']:
            return False
        else:
            return True

class Solution:
    def romanToInt(self, s: str) -> int:
        last = ""
        integer = 0

        for number in s:
            if last == "":
                integer += getValue(number)
            elif previousIsHigher(number, last):
                integer += getValue(number)
            else:
                integer -= 2 * getValue(last)
                integer += getValue(number)
            last = number

        return integer
            