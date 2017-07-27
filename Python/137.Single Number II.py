"""
137. Single Number II

Given an array of integers, every element appears three times except for one,
which appears exactly once.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1

        res, sign = [0] * 32, 0
        for n in nums:
            bina = format(n, 'b')
            if bina[0] == '-':
                sign += 1
                bina = bina[1:]
            for i in range(0, len(bina)):
                bit = bina[-(i + 1)]
                if bit == '1':
                    res[-(i + 1)] += 1
        s = ""
        for n in res:
            s += str(n % 3)

        value, sign = int(s, 2), sign % 3
        if sign == 1:
            value *= -1
        return value
