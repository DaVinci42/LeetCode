from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return [d[target - v], i]
            d[v] = i
        return []
