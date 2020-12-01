from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        res, N = 0, len(citations)
        for i in range(N - 1, -1, -1):
            if citations[i] < N - i:
                break
            res += 1
        return res