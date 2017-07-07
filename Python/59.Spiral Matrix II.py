"""
59. Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        if n <= 0:
            return result
        for i in range(0, n):
            row = []
            result.append(row)
            for j in range(0, n):
                row.append(0)

        for i in range(0, (n + 1) // 2):
            top, left, bottom, right = i, i, n - 1 - i, n - 1 - i
            start_num = sum(4 * j - 4 for j in range(n, n - 2 * i, -2))

            if top == bottom:
                result[top][left] = start_num + 1
                break

            # top
            for j in range(left, right):
                start_num += 1
                result[top][j] = start_num

            # right
            for j in range(top, bottom):
                start_num += 1
                result[j][right] = start_num

            # bottom
            for j in range(right, left, -1):
                start_num += 1
                result[bottom][j] = start_num

            # left
            for j in range(bottom, top, -1):
                start_num += 1
                result[j][left] = start_num

        return result
