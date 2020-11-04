from typing import Dict


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        cache: Dict[int, int] = {}

        def dp(index: int) -> int:
            if index in cache:
                return cache[index]

            if index < 0 or s[index] == "(":
                cache[index] = 0
                return 0

            # ...()
            if index > 0 and s[index - 1] == "(":
                res = dp(index - 2) + 2
                cache[index] = res
                return res

            # ...(..)
            preRes = dp(index - 1)
            if preRes and index - preRes - 1 >= 0 and s[index - preRes - 1] == "(":
                cache[index] = preRes + 2 + dp(index - preRes - 2)
                return cache[index]
            return 0

        return max((dp(i) for i in range(len(s))), default=0)
