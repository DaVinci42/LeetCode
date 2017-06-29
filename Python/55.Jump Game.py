"""
55. Jump Game

Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) <= 1:
            return True

        i, dest, length = 0, 0, len(nums)
        while i < length - 1:
            value = nums[i]
            dest = max(dest, value + i)
            if dest < i + 1:
                break
            else:
                i += 1
        return dest >= length - 1
