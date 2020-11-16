from typing import List
import bisect


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        preSum, sumList = 0, [0] * len(nums)
        for i, n in enumerate(nums):
            preSum += n
            sumList[i] = preSum

        if sumList[-1] < s:
            return 0

        minLen = len(nums)
        for i, n in enumerate(sumList):
            if n < s:
                continue

            left = bisect.bisect_right(sumList, n - s)
            if left > 0 and nums[left - 1] == n - s:
                minLen = min(minLen, i - left + 2)
            else:
                minLen = min(minLen, i - left + 1)
        return minLen
