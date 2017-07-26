"""
120. Triangle

Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
"""


class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or len(triangle) == 0:
            return 0
        return min(self.find_min_sum(len(triangle) - 1, triangle))

    def find_min_sum(self, r, triangle):
        if r == 0:
            return triangle[r]
        else:
            pre_sum_list = self.find_min_sum(r - 1, triangle)
            row = triangle[r][:]
            row[0] += pre_sum_list[0]
            row[-1] += pre_sum_list[-1]
            for i in range(len(row) - 2, 0, -1):
                row[i] += min(pre_sum_list[i], pre_sum_list[i - 1])
            return row
