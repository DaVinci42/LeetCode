"""
34. Search for a Range

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        elif target < nums[0] or target > nums[-1]:
            return [-1, -1]

        length, start = len(nums), 0
        if nums[0] != target:
            left, right = 0, length - 1
            while right - left > 1:
                mid = (left + right) // 2
                v = nums[mid]
                if v >= target:
                    right = mid
                else:
                    left = mid
            start = right
            if nums[start] != target:
                return [-1, -1]

        end = length - 1
        if nums[end] == target:
            return [start, end]
        else:
            left, right = start, end
            while right - left > 1:
                mid = (left + right) // 2
                v = nums[mid]
                if v <= target:
                    left = mid
                else:
                    right = mid

            return[start, left]
