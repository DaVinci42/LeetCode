from typing import List
from collections import deque


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return A

        res = deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = A[l] * A[l], A[r] * A[r]
            if left >= right:
                res.appendleft(left)
                l += 1
            else:
                res.appendleft(right)
                r -= 1

        return list(res)
