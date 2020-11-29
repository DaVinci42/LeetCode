from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        if nums:
            self.sums = [nums[0]] * len(nums)
            for i in range(1, len(nums)):
                self.sums[i] = nums[i] + self.sums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if i <= 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i - 1]
