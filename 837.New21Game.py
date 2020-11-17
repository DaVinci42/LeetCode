class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K <= 0:
            return 1

        dp, preSum = [1] * (N + 1), 1
        for i in range(1, N + 1):
            dp[i] = 1 / W * preSum
            if i < K:
                preSum += dp[i]
            if i >= W:
                preSum -= dp[i - W]

        return sum(dp[K : N + 1])