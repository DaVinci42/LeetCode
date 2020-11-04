from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        res = 0
        for j in range(1, len(rating) - 1):
            res += sum(1 for i in range(0, j) if rating[i] > rating[j]) * sum(
                1 for i in range(j + 1, len(rating)) if rating[i] < rating[j]
            ) + (
                sum(1 for i in range(0, j) if rating[i] < rating[j])
                * sum(1 for i in range(j + 1, len(rating)) if rating[i] > rating[j])
            )
        return res
