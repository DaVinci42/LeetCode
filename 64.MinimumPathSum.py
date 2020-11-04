from typing import List, Dict, Tuple


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dp(m: int, n: int) -> int:
            if (m, n) in cache:
                return cache[(m, n)]

            if m == len(grid) - 1 and n < len(grid[m]) - 1:
                return grid[m][n] + dp(m, n + 1)
            elif m < len(grid) - 1 and n == len(grid[m]) - 1:
                return grid[m][n] + dp(m + 1, n)
            elif m == len(grid) - 1 and n == len(grid[m]) - 1:
                return grid[m][n]

            res = grid[m][n] + min(dp(m + 1, n), dp(m, n + 1))
            cache[(m, n)] = res
            return res

        return dp(0, 0)

