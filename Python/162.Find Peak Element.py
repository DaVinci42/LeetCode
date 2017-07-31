"""
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""


class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        length = len(nums)
        if length == 0 or length == 1:
            return 0

        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i

        if nums[0] >= nums[1] and nums[0] >= nums[-1]:
            return 0
        if nums[-1] >= nums[-2] and nums[-1] >= nums[0]:
            return length - 1
