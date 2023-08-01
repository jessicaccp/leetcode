# 1768. Merge Strings Alternately
# Runtime: 41 ms
# Memory Usage: 16.4 MB
# By https://leetcode.com/jessicaccp/ on Jul 29, 2023

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        output = ""

        while (True):
            if index < len(word1):
                output += word1[index]
            else:
                if index < len(word2):
                    output += word2[index:len(word2)]
                    break
                else:
                    break

            if index < len(word2):
                output += word2[index]
            else:
                if index + 1 < len(word1):
                    output += word1[index + 1:len(word1)]
                    break
                else:
                    break

            index += 1

        return output