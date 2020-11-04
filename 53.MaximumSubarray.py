from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = [0] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                res[i] = nums[0]
            else:
                preMax = res[i - 1]
                res[i] = max(preMax + n, n)
        return max(res)
