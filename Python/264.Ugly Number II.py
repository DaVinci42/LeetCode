"""
264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
"""


class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1

        list2, list3, list5 = [2], [3], [5]

        current, value, nums = 1, 1, set([1])
        while current < n:
            v2, v3, v5 = list2[0], list3[0], list5[0]
            if v2 < v3 and v2 < v5:
                del list2[0]
                value = v2
            elif v3 < v2 and v3 < v5:
                del list3[0]
                value = v3
            elif v5 < v2 and v5 < v3:
                del list5[0]
                value = v5
            if value * 2 not in nums:
                list2.append(value * 2)
                nums.add(value * 2)
            if value * 3 not in nums:
                list3.append(value * 3)
                nums.add(value * 3)
            if value * 5 not in nums:
                list5.append(value * 5)
                nums.add(value * 5)
            current += 1
        return value
