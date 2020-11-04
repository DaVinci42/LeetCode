from typing import List, Dict, Tuple


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache: Dict[Tuple[int, int], int] = {}

        def dp(m: int, n: int) -> int:
            if (m, n) in cache:
                return cache[(m, n)]

            if (
                m >= len(obstacleGrid)
                or n >= len(obstacleGrid[0])
                or obstacleGrid[m][n] == 1
            ):
                return 0
            elif m == len(obstacleGrid) - 1 and n == len(obstacleGrid[0]) - 1:
                cache[(m, n)] = 1
                return 1
            res = dp(m + 1, n) + dp(m, n + 1)
            cache[(m, n)] = res
            return res

        return dp(0, 0)

