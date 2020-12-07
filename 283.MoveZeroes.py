from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                right += 1
                continue

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1