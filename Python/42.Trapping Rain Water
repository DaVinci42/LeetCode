"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!
"""


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None:
            return 0
        length = len(height)
        if length == 0:
            return 0

        max_from_left, max = {}, 0
        for i in range(0, length):
            num = height[i]
            if num > height[max]:
                max = i
            max_from_left[i] = max

        max_from_right, max, i = {}, length - 1, length - 1
        while i >= 0:
            num = height[i]
            if num > height[max]:
                max = i
            max_from_right[i] = max
            i -= 1

        count = 0
        for i, v in enumerate(height):
            max_left = max_from_left[i]
            max_right = max_from_right[i]

            value = min(height[max_left], height[max_right]) - v
            count += value
        return count
