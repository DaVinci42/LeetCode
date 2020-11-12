from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        s = sum(nums)
        leftSum, preNum = 0, 0
        for i, n in enumerate(nums):
            leftSum += preNum
            if s - leftSum - n == leftSum:
                return i
            preNum = n
        return -1
