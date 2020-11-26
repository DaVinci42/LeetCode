from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        return int(N * (1 + N) / 2) - sum(nums)
