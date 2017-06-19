"""
7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer.
Your function should return 0 when the reversed integer overflows.
"""

import math


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = math.pow(2, 31) - 1
        min_int = -math.pow(2, 31)
        if x > max_int or x < min_int:
            return 0
        if x <= 9 and x >= -9:
            return x

        is_positive = True if x > 0 else False
        if not is_positive:
            x = -1 * x

        result = 0
        length = int(math.log10(x))
        for i in range(0, length + 1):
            num = int(x // math.pow(10, i) - (x // math.pow(10, i + 1) * 10))
            result += (num * math.pow(10, length - i))
        result = int(result)

        if result > max_int or result < min_int:
            return 0
        elif not is_positive:
            return -1 * result
        else:
            return result
