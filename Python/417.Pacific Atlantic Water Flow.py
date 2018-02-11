"""
417. Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""


class Solution:

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix is None or len(matrix) == 0:
            return list()

        a_set, p_set = set(), set()
        w, h = len(matrix[0]), len(matrix)
        for i in range(0, w):
            p_set.add((0, i))
            a_set.add((h - 1, i))
        for i in range(0, h):
            p_set.add((i, 0))
            a_set.add((i, w - 1))

        a_cells, p_cells = self.cells_from_stack(a_set, matrix), self.cells_from_stack(p_set, matrix)
        return list(a_cells.intersection(p_cells))

    def cells_from_stack(self, cell_set, matrix):
        result_set = set()
        while len(cell_set) > 0:
            r, c = cell_set.pop()
            if (r, c) in result_set:
                continue
            result_set.add((r, c))

            cell_height = matrix[r][c]
            # top
            if r > 0 and matrix[r - 1][c] >= cell_height:
                cell_set.add((r - 1, c))
            # left
            if c > 0 and matrix[r][c - 1] >= cell_height:
                cell_set.add((r, c - 1))
            # right
            if c < len(matrix[r]) - 1 and matrix[r][c + 1] >= cell_height:
                cell_set.add((r, c + 1))
            # bottom
            if r < len(matrix) - 1 and matrix[r + 1][c] >= cell_height:
                cell_set.add((r + 1, c))

        return result_set
