from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost[0], cost[1])

        m, n = 0, 0
        for i in range(2, len(cost) + 1):
            m, n = n, min(m + cost[i - 2], n + cost[i - 1])
        return n
