from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            midV = nums[mid]
            if midV > nums[left]:
                left = mid
            elif midV < nums[right]:
                right = mid
        return min(nums[left], nums[right])