from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) <= 1:
            return
        k %= len(nums)
        if not k:
            return

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
