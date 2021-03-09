from typing import List


class Solution:
    def checkValidString(self, s: str) -> bool:
        minP, maxP = 0, 0
        for c in s:
            if c == "(":
                minP += 1
                maxP += 1
            elif c == ")":
                minP -= 1
                maxP -= 1
            elif c == "*":
                minP -= 1
                maxP += 1

            minP = max(minP, 0)
            if maxP < 0:
                return False
        return minP == 0