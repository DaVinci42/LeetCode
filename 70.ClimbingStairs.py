from typing import Dict


class Solution:
    def climbStairs(self, n: int) -> int:

        cache: Dict[int, int] = {}

        def dp(m: int) -> int:
            if m <= 0:
                return 0
            if m == 1:
                return 1
            elif m == 2:
                return 2
            elif m in cache:
                return cache[m]

            res = dp(m - 1) + dp(m - 2)
            cache[m] = res
            return res

        return dp(n)

