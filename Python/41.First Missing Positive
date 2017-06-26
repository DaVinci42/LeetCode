"""
41. First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 1

        nums.sort()
        if nums[0] > 1:
            return 1
        for i, v in enumerate(nums):
            if i == len(nums) - 1:
                return v + 1
            elif nums[i + 1] - v > 1:
                if v <= 0 and nums[i + 1] > 1:
                    return 1
                elif v > 0:
                    return v + 1
