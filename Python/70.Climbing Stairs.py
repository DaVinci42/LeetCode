"""
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2

        pre_two, pre_one = 1, 2
        for i in range(3, n + 1):
            sum = pre_one + pre_two
            pre_two = pre_one
            pre_one = sum
        return sum
