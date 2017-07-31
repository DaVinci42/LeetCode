"""
153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""


class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while right > left + 1:
            mid = (left + right) // 2
            mid_v = nums[mid]
            if nums[left] <= mid_v and mid_v > nums[right]:
                left = mid
            elif mid_v < nums[left] and mid_v <= nums[right]:
                right = mid
            elif mid_v > nums[left] and mid_v <= nums[right]:
                right = mid
        return min(nums[left], nums[right])
