"""
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""


class Solution(object):

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        r = 0
        while n >= 5:
            r = r + n // 5
            n = n // 5
        return r
