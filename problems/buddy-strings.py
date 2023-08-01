# 859. Buddy Strings
# Runtime: 39 ms
# Memory Usage: 16.6 MB
# By https://leetcode.com/jessicaccp/ on Jul 31, 2023

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal:
            unique = "".join(set(s))
            if len(unique) != len(s):
                return True

        count = 0
        index = []
        for i in range(0, len(s)):
            if s[i] != goal[i]:
                count += 1
                index.append(i)

                if count == 2:
                    s = list(s)
                    s[index[0]], s[index[1]] = s[index[1]], s[index[0]]
                    s = "".join(s)

                    if s == goal:
                        return True
                    else:
                        return False
        
        return False