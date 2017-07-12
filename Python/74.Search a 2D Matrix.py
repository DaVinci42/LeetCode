"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""


class Solution(object):

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

        target_row = 0
        if target >= matrix[-1][0]:
            target_row = len(matrix) - 1
        else:
            left, right = 0, len(matrix) - 1
            while right - left > 1:
                mid = (left + right) // 2
                mid_value = matrix[mid][0]
                if mid_value == target:
                    return True
                elif mid_value < target:
                    left = mid
                else:
                    right = mid
            target_row = left

        print(target_row)
        row = matrix[target_row]
        left, right = 0, len(row) - 1
        while right - left > 1:
            mid = (left + right) // 2
            mid_value = row[mid]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid
            else:
                right = mid
        return row[left] == target or row[right] == target
