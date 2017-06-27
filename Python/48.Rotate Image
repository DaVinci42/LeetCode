"""
48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""


class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) <= 1:
            return

        start = len(matrix) // 2
        while start < len(matrix):
            self.rotate_row(matrix, start)
            start += 1

    def rotate_row(self, matrix, row):
        length = len(matrix)
        if row * 2 == length - 1:
            return
        start = length - 1 - row
        end = length - start

        for i in range(start, end - 1):
            tmp = matrix[row][i]

            # right to bottom
            matrix[row][i] = matrix[length - 1 - i][row]
            # top to right
            matrix[length - 1 - i][row] = matrix[length - 1 -
                                                 row][length - 1 - i]
            # left to top
            matrix[length - 1 - row][length - 1 -
                                     i] = matrix[i][length - 1 - row]
            # bottom ro left
            matrix[i][length - 1 - row] = tmp
