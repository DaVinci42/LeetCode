import math


class Solution:
    def numSquares(self, n: int) -> int:
        if n < 1:
            return 0

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = min((dp[i - j * j] for j in range(1, int(math.sqrt(i)) + 1))) + 1
        return dp[n]