"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search.
If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return -1 if nums[0] != target else 0

        length = len(nums)
        left, right = 0, length - 1
        while right > left + 1:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        if left == 0 and right == 1 and nums[left] < nums[right]:
            right = length - 1
        elif nums[0] <= target and target <= nums[left]:
            left, right = 0, left
        elif nums[right] <= target and target <= nums[length - 1]:
            left, right = right, length - 1
        else:
            return -1

        while right > left + 1:
            mid = (left + right) // 2
            v = nums[mid]
            if v == target:
                return mid
            elif v > target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
