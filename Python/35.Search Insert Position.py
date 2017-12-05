"""
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""


class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        length = len(nums)
        if target <= nums[0]:
            return 0
        elif target == nums[length - 1]:
            return length - 1
        elif target > nums[length - 1]:
            return length

        left, right = 0, length - 1
        while right - left > 1:
            mid = (left + right) // 2
            v = nums[mid]
            if v == target:
                return mid
            elif v < target:
                left = mid
            else:
                right = mid
        return right
