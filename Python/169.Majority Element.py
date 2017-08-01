"""
169. Majority Element

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        d, s = {}, len(nums) // 2
        for n in nums:
            count = 0
            if n in d:
                count = d[n] + 1
            else:
                count = 1
            if count > s:
                return n
            else:
                d[n] = count
