# 278. First Bad Version
# Runtime: 31 ms
# Memory Usage: 16.3 MB
# By https://leetcode.com/jessicaccp/ on Aug 1, 2023

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        good = 1
        bad = n

        while(True):
            middle = int((good + bad) / 2)

            if isBadVersion(middle):
                bad = middle
            else:
                good = middle

            if good + 1 == bad and not isBadVersion(good):
                return bad
            elif bad == 1:
                return bad
            elif good == bad:
                return bad

            if bad <= 0:
                if isBadVersion(1):
                    return 1
            elif bad < good:
                if isBadVersion(bad):
                    return bad

            if good > n:
                if isBadVersion(n):
                    return n
                else:
                    if isBadVersion(good):
                        return good