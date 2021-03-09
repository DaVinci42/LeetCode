from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c, res = Counter(text), 0
        while (
            c["b"] >= 1 and c["a"] >= 1 and c["l"] >= 2 and c["o"] >= 2 and c["n"] >= 1
        ):
            c["b"] -= 1
            c["a"] -= 1
            c["l"] -= 2
            c["o"] -= 2
            c["n"] -= 1

            res += 1
        return res
