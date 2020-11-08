from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        n = len(matrix)
        for i in range(0, n // 2):
            for j in range(0, n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

        for i in range(0, n):
            for j in range(0, i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
