"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix) == 0:
            return []

        top, result = 0, []
        while top <= (len(matrix) - 1) // 2:
            width, height = len(matrix[top]), len(matrix)
            bottom = height - 1 - top
            left, right = top, width - 1 - top

            if top > bottom or left > right:
                break

            if top == bottom:
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                break
            elif left == right:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][left])
                break

            for i in range(left, right):
                result.append(matrix[top][i])

            for i in range(top, bottom):
                result.append(matrix[i][right])

            i = right
            while i > left:
                result.append(matrix[bottom][i])
                i -= 1

            i = bottom
            while i > top:
                result.append(matrix[i][left])
                i -= 1

            top += 1
        return result
