class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        i, dp[1] = 1, 1
        while i < n:
            i += 1
            dp[i] = sum(dp[j] * dp[i - 1 - j] for j in range(1, i)) + 2 * dp[i - 1]
        return dp[n]
