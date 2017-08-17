"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution(object):

    target_fount = False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        self.target_fount = False
        self.search_matrix(matrix, 0, 0, len(
            matrix[0]) - 1, len(matrix) - 1, target)
        return self.target_fount

    def search_matrix(self, matrix, left, top, right, bottom, target):
        if left > right or top > bottom:
            return
        if self.target_fount:
            return
        if target < matrix[top][left] or target > matrix[bottom][right]:
            return

        mid_h, mid_v = left, top
        if left == right and top == bottom:
            self.target_fount = True
            return

        mid_h = (left + right) // 2
        mid_v = (top + bottom) // 2

        value = matrix[mid_v][mid_h]
        if value == target:
            self.target_fount = True
        else:
            self.search_matrix(matrix, mid_h + 1, top, right, mid_v, target)
            self.search_matrix(matrix, left, mid_v + 1, mid_h, bottom, target)
            self.search_matrix(matrix, mid_h + 1, mid_v +
                               1, right, bottom, target)
            if value > target:
                self.search_matrix(matrix, left, top, mid_h, mid_v, target)
