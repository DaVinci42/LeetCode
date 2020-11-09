from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return 0

        left, right = 0, 0
        while left <= right:
            farest = max(i + nums[i] for i in range(left, right + 1))
            if farest >= len(nums) - 1:
                return True
            left, right = right + 1, farest
        return False
