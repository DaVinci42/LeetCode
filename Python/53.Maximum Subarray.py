"""
53. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        pre_sum, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            value = nums[i]
            include_max = max(pre_sum + value, value)
            current_max = max(pre_sum, include_max)
            pre_sum = include_max
            if current_max > max_sum:
                max_sum = current_max
        return max_sum
