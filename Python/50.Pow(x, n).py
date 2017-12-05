"""
50. Pow(x, n)

Implement pow(x, n).
"""


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        is_positive = True
        if n == 0 or x == 0 or x == 1:
            return 1
        elif x == -1:
            return 1 if n % 2 == 0 else -1
        elif n < 0:
            is_positive = False
            n = -n
        else:
            is_positive = True

        max_int = pow(2, 32) - 1

        i, result = 1, x
        while i < n:
            result *= x
            if result > max_int or abs(result) < 1.0 / max_int:
                return 0
            i += 1
        return result if is_positive else 1.0 / result
