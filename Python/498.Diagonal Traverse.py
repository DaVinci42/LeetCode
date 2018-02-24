"""
498. Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""


class Solution:

    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None:
            return list()
        h = len(matrix)
        if h == 0:
            return list()
        w = len(matrix[0])
        if w == 0:
            return list()

        diagonals = list()
        for i in range(0, w + h - 1):
            row = self.__diagonal_in_matrix(i, matrix)
            diagonals.append(row)

        result = list()
        for i, r in enumerate(diagonals):
            if i % 2 == 0:
                result += r[::-1]
            else:
                result += r
        return result

    # top-right to bottom-left
    def __diagonal_in_matrix(self, index, matrix):
        w, h = len(matrix[0]), len(matrix)
        if index < w:
            x, y = index, 0
        else:
            x, y = len(matrix[0]) - 1, index - w + 1

        result = list()
        while x >= 0 and y < h:
            result.append(matrix[y][x])
            x -= 1
            y += 1
        return result
