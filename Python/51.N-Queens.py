"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an nxn chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0:
            return []

        result = []
        record = {}
        for i in range(0, n):
            pre = record.copy()
            pre[0] = i
            self.pick(pre, 1, n, result)
        return result

    def pick(self, record, index, n, result):
        if index >= n:
            lis = []
            for i in range(0, n):
                lis.append('')
            for key in record:
                value = record[key]
                string = ''
                for i in range(0, value):
                    string += '.'
                string += 'Q'
                for i in range(value + 1, n):
                    string += '.'
                lis[key] = string
            result.append(lis)
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
            self.pick(record, index + 1, n, result)
