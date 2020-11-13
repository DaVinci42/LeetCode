from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1:
            return []

        matrix = [[0] * n for _ in range(n)]

        def generate(i: int) -> None:
            if i >= n or matrix[i][i] != 0:
                return

            lower, upper = i, n - 1 - i
            num = 0 if i == 0 else matrix[i][i - 1]
            if lower == upper:
                matrix[i][i] = num + 1
                return

            for j in range(lower, upper):
                num += 1
                matrix[i][j] = num
            for j in range(lower, upper):
                num += 1
                matrix[j][n - i - 1] = num
            for j in range(upper, lower, -1):
                num += 1
                matrix[n - i - 1][j] = num
            for j in range(upper, lower, -1):
                num += 1
                matrix[j][i] = num
            generate(i + 1)

        generate(0)
        return matrix
