from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            row = triangle[i]
            for j in range(0, len(row)):
                dp[j] = row[j] + min(dp[j], dp[j + 1])
        return dp[0]