"""
52. N-Queens II

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""


class Solution(object):

    total_count = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return []

        self.total_count = 0
        record = {}
        for i in range(0, n):
            pre = record.copy()
            pre[0] = i
            self.pick(pre, 1, n)
        return self.total_count

    def pick(self, record, index, n):
        if index >= n:
            self.total_count += 1
            return

        record = record.copy()
        available = set()
        for i in range(0, n):
            available.add(i)
        for key in record:
            value = record[key]
            diff = abs(key - index)
            if value + diff in available:
                available.remove(value + diff)
            if value - diff in available:
                available.remove(value - diff)
            if value in available:
                available.remove(value)

        for i in available:
            record[index] = i
            self.pick(record, index + 1, n)
