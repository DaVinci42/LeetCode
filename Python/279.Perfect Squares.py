"""
279. Perfect Squares

Given a positive integer n,
find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4;
given n = 13, return 2 because 13 = 4 + 9.
"""

import math


class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        min_list = [0] * (n + 1)
        for i in range(1, n + 1):
            if i == 1:
                min_list[i] = 1
            else:
                min_set = set()
                for j in range(int(math.sqrt(i)), 0, -1):
                    min_set.add(min_list[i - j * j] + 1)
                min_list[i] = min(min_set)
        return min_list[-1]
