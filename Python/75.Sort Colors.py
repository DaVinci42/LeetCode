"""
75. Sort Colors

Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""


class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        red, white, blue = 0, 0, 0
        for color in nums:
            if color == 0:
                red += 1
            elif color == 1:
                white += 1
            elif color == 2:
                blue += 1

        for i in range(0, red):
            nums[i] = 0
        for i in range(red, red + white):
            nums[i] = 1
        for i in range(red + white, red + white + blue):
            nums[i] = 2
