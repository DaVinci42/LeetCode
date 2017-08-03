"""
204. Count Primes

Description:

Count the number of prime numbers less than a non-negative number, n.
"""

import math


class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0

        nums = [True] * n
        nums[0], nums[-1] = False, False

        for i in range(2, int(math.sqrt(n)) + 1):
            if nums[i - 1] and self.is_primary(i):
                a = 2 * i - 1
                while a <= n - 1:
                    if nums[a]:
                        nums[a] = False
                    a += i

        count = 0
        for i in nums:
            if i:
                count += 1
        return count

    def is_primary(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
