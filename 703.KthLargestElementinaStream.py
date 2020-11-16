from typing import List
import bisect


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for n in nums:
            bisect.insort_left(self.nums, -1 * n)

    def add(self, val: int) -> int:
        bisect.insort_left(self.nums, val * -1)
        return self.nums[self.k - 1] * -1
