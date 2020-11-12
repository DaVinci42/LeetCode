from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []

        res = set()

        def generate(left: int, right: int, s: str):
            if not left and not right:
                res.add(s)
            if left:
                generate(left - 1, right + 1, s + "(")
            if right:
                generate(left, right - 1, s + ")")

        generate(n, 0, "")
        return list(res)
