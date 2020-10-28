from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        self.result = set()
        self.generate(n, 0, "")
        return list(self.result)

    def generate(self, allowedLeft: int, allowedRight: int, s: str):
        if not allowedLeft and not allowedRight:
            self.result.add(s)
            return

        for i in range(1, allowedLeft + 1):
            s1 = s[:]
            self.generate(allowedLeft - i, allowedRight + i - 1, s1 + "(" * i + ")")

        for i in range(1, allowedRight + 1):
            s1 = s[:]
            self.generate(allowedLeft, allowedRight - i, s1 + ")" * i)
