"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        sum_min = []
        for i in range(0, len(grid)):
            row = []
            sum_min.append(row)
            for j in grid[i]:
                row.append(0)

        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                min_pre = 0
                if row > 0 and col > 0:
                    min_pre = min(sum_min[row - 1][col], sum_min[row][col - 1])
                elif row > 0:
                    min_pre = sum_min[row - 1][col]
                elif col > 0:
                    min_pre = sum_min[row][col - 1]
                sum_min[row][col] = min_pre + grid[row][col]
        for row in sum_min:
            print(row)
        return sum_min[-1][-1]
