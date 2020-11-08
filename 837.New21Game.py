class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 0 <= N

        dp = [0] * (K + W)
        for i in range(K, K + W):
            dp[i] = 1 if i <= N else 0

        s = sum(dp[K : K + W])
        for i in range(K - 1, -1, -1):
            dp[i] = s / W
            s += dp[i] - dp[i + W]
        return dp[0]
