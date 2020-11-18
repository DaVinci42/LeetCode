from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        m, count = nums[0], 0
        for n in nums:
            if count == 0:
                m = n
                count += 1
            elif m == n:
                count += 1
            else:
                count -= 1
        return m
