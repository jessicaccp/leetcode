# 682. Baseball Game
# Runtime: 44 ms
# Memory Usage: 16.6 MB
# By https://leetcode.com/jessicaccp/ on Jul 31, 2023

def is_number(value):
    try:
        float(value)
        return True
    except:
        return False

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        score_sum = 0

        for op in operations:
            if is_number(op):
                score.append(int(op))
                score_sum += score[-1]
            elif op == "+":
                score.append(score[-1] + score[-2])
                score_sum += score[-1]
            elif op == "D":
                score.append(2 * score[-1])
                score_sum += score[-1]
            elif op == "C":
                previous = score.pop()
                score_sum -= previous

        return score_sum