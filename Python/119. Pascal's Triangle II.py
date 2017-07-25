"""
119. Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        elif rowIndex == 0:
            return [1]
        else:
            pre_row = self.getRow(rowIndex - 1)
            row = [1]
            for i in range(0, len(pre_row) - 1):
                row.append(pre_row[i] + pre_row[i + 1])
            row.append(1)
            return row


s = Solution()
print(s.getRow(3))
