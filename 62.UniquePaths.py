from typing import Dict, Tuple


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache: Dict[Tuple[int, int], int] = {}

        def dp(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]
            if i <= 0 or j <= 0:
                return 0
            if i == 1 or j == 1:
                return 1

            res = dp(i - 1, j) + dp(i, j - 1)
            cache[(i, j)] = res
            return res

        return dp(m, n)
