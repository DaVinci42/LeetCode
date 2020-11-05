from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        n0, n1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            n0, n1 = n1, max(n0 + nums[i], n1)
        return n1
