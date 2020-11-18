from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        m0, m1, c0, c1 = nums[0], nums[0] - 1, 0, 0
        for n in nums:
            if m0 == n:
                c0 += 1
            elif m1 == n:
                c1 += 1
            elif c0 == 0:
                m0, c0 = n, 1
            elif c1 == 0:
                m1, c1 = n, 1
            else:
                c0 -= 1
                c1 -= 1
        return [n for n in [m0, m1] if nums.count(n) > len(nums) // 3]