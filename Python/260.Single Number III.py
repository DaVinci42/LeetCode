"""
260. Single Number III

Given an array of numbers nums,
in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?
"""


class Solution:

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return list()

        xor = 0
        for n in nums:
            xor ^= n

        b_xor = '{:32b}'.format(0xFFFFFFFF & xor)
        p_bit = 0
        for i, v in enumerate(b_xor):
            if v == '1':
                p_bit = i
                break

        xor1 = xor
        for n in nums:
            b_n = '{:32b}'.format(0xFFFFFFFF & n)
            if b_n[p_bit] == '1':
                xor1 ^= n

        return [xor1, xor1 ^ xor]
