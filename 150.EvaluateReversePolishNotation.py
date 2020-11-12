from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s, operators = [], {"+", "-", "*", "/"}

        for t in tokens:
            if t not in operators:
                s.append(int(t))
                continue

            v1 = s.pop()
            v0 = s.pop()
            if t == "+":
                s.append(v0 + v1)
            elif t == "-":
                s.append(v0 - v1)
            elif t == "*":
                s.append(v0 * v1)
            elif t == "/":
                s.append(int(v0 / v1))

        return s[0]
