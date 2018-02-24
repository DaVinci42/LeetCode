"""
238. Product of Array Except Self

Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return list()

        length = len(nums)
        previous_product = [1] * length
        after_product = [1] * length

        for i in range(1, length):
            previous_product[i] = nums[i - 1] * previous_product[i - 1]
        for i in range(length - 2, -1, -1):
            after_product[i] = nums[i + 1] * after_product[i + 1]

        return list(previous_product[i] * after_product[i] for i in range(0, length))
