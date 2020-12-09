from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if not A:
            return 0

        minA, maxA = min(A), max(A)
        if minA + K >= maxA - K:
            return 0
        else:
            return (maxA - K) - (minA + K)