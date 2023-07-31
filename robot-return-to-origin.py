# 657. Robot Return to Origin
# Runtime: 67 ms
# Memory Usage: 16.4 MB
# By https://leetcode.com/jessicaccp/ on Jul 31, 2023

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = [0, 0, 0, 0] # R, L, U, D
        for move in moves:
            if move == "R":
                directions[0] += 1
            elif move == "L":
                directions[1] += 1
            elif move == "U":
                directions[2] += 1
            elif move == "D":
                directions[3] += 1

        if directions[0] == directions[1] and directions[2] == directions[3]:
            return True
        else:
            return False