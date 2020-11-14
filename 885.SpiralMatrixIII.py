from typing import List


class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def generate(left: int, top: int, right: int, bottom: int) -> List[int]:
            if left < 0 and top < 0 and right >= C and bottom >= R:
                return []
            if left == right and top == bottom:
                return [[top, left]] + generate(
                    left - 1, top - 1, right + 1, bottom + 1
                )

            res = []
            if right < C:
                for i in range(max(0, top + 1), min(R - 1, bottom) + 1):
                    res.append([i, right])
            if res and res[-1] == [bottom, right]:
                res.pop()

            if bottom < R:
                for i in range(min(right, C - 1), max(0, left) - 1, -1):
                    res.append([bottom, i])
            if res and res[-1] == [bottom, left]:
                res.pop()

            if left >= 0:
                for i in range(min(bottom, R - 1), max(top, 0) - 1, -1):
                    res.append([i, left])
            if res and res[-1] == [top, left]:
                res.pop()

            if top >= 0:
                for i in range(max(0, left), min(C - 1, right) + 1):
                    res.append([top, i])
            return res + generate(left - 1, top - 1, right + 1, bottom + 1)

        return generate(c0, r0, c0, r0)
