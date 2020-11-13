from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        def spiralLayer(left: int, top: int, right: int, bottom: int) -> List[int]:
            if top > bottom or left > right:
                return []
            if top == bottom:
                return matrix[top][left : right + 1]
            if left == right:
                return [matrix[i][left] for i in range(top, bottom + 1)]

            return (
                matrix[top][left:right]
                + [matrix[i][right] for i in range(top, bottom)]
                + matrix[bottom][right:left:-1]
                + [matrix[i][left] for i in range(bottom, top, -1)]
                + spiralLayer(left + 1, top + 1, right - 1, bottom - 1)
            )

        return spiralLayer(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
