from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        if target <= nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            return len(nums)

        i, j = 0, len(nums) - 1
        while j - i > 1:
            mid = (i + j) // 2
            mid_v = nums[mid]
            if mid_v == target:
                return mid
            elif mid_v > target:
                j = mid
            else:
                i = mid
        return j
