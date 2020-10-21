from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        left, right = 0, len(height) - 1
        maxA = 0
        while left < right:
            l_h, r_h = height[left], height[right]
            maxA = max(maxA, (right - left) * min(l_h, r_h))
            if l_h <= r_h:
                left += 1
            else:
                right -= 1
        return maxA
