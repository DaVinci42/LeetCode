from typing import List
import itertools


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if len(mat) < k:
            return []

        def countOne(row: List[int]) -> int:
            left, right = 0, len(row) - 1
            if row[left] == 0:
                return 0
            if row[right] == 1:
                return right + 1

            while left + 1 < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid
                else:
                    right = mid
            return left + 1

        return list(
            map(
                lambda t: t[1],
                sorted(map(lambda i: (countOne(mat[i]), i), range(len(mat))))[:k],
            )
        )