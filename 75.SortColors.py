from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return

        left, right = 0, len(nums) - 1
        while right > left:
            if nums[right] != 0:
                right -= 1
                continue

            if nums[left] == 0:
                left += 1
                continue

            nums[left], nums[right] = 0, nums[left]
            left += 1
            right -= 1

        left, right = 0, len(nums) - 1
        while right > left:
            if nums[left] != 2:
                left += 1
                continue
            if nums[right] == 2:
                right -= 1
                continue

            nums[left], nums[right] = nums[right], 2
            left += 1
            right -= 1
