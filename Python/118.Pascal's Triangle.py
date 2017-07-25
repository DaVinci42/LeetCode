"""
118. Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        result = []
        pre_row = []
        for i in range(0, numRows):
            row = self.generate_row(pre_row)
            result.append(row)
            pre_row = row
        return result

    def generate_row(self, pre_row):
        pre_length = len(pre_row)
        if pre_length == 0:
            return [1]
        elif pre_length == 1:
            return [1, 1]
        elif pre_length == 2:
            return [1, 2, 1]
        else:
            row = [1]
            for i in range(0, len(pre_row) - 1):
                row.append(pre_row[i] + pre_row[i + 1])
            row.append(1)
            return row
