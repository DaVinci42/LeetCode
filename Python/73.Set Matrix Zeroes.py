"""
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in place.
"""


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        zero_row, zero_col = set(), set()
        for r in range(0, len(matrix)):
            row = matrix[r]
            for c in range(0, len(row)):
                if row[c] == 0:
                    zero_row.add(r)
                    zero_col.add(c)

        for r in zero_row:
            row = matrix[r]
            for c in range(0, len(row)):
                row[c] = 0

        for c in zero_col:
            for r in range(0, len(matrix)):
                matrix[r][c] = 0
