"""
60. Permutation Sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""


class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        count = self.factorial(n)
        if k < 0 or k > count:
            return ""

        available, result = [], ""
        for i in range(1, n + 1):
            available.append(str(i))

        while len(result) < n:
            unit = self.factorial(n - len(result) - 1)
            d, r = k // unit, k % unit
            c = ''
            if r == 0:
                c = available[d - 1]
                k = unit
            else:
                c = available[d]
                k = r

            result += c
            available.remove(c)

        return result

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)
