from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right, step = 0, 0, 0
        while right < len(nums) - 1:
            step += 1
            left, right = right, max(i + nums[i] for i in range(left, right + 1))
        return step
