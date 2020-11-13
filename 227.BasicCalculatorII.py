from typing import List
import itertools


class Solution:
    def calculate(self, s: str) -> int:
        def cal(input: List, highPriority: bool) -> int:
            if not input:
                return 0

            res, i = [], 0
            while i < len(input):
                n = input[i]
                if not res or not isinstance(n, int):
                    res.append(n)
                elif res[-1] == "*":
                    if not highPriority:
                        res.append(n)
                    else:
                        res.pop()
                        res.append(res.pop() * n)
                elif res[-1] == "/":
                    if not highPriority:
                        res.append(n)
                    else:
                        res.pop()
                        res.append(int(res.pop() / n))
                elif res[-1] == "+":
                    if highPriority:
                        res.append(n)
                    else:
                        res.pop()
                        res.append(res.pop() + n)
                else:
                    if highPriority:
                        res.append(n)
                    else:
                        res.pop()
                        res.append(res.pop() - n)
                i += 1
            return res

        res = [
            next(g) if not k else int("".join(g))
            for k, g in itertools.groupby(
                filter(lambda c: c != " ", s), lambda c: c.isdigit()
            )
        ]

        return cal(cal(res, True), False)[0]
