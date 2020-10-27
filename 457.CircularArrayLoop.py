from typing import List, Set


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums:
            return False
        for i, v in enumerate(nums):
            if self.testStep(i, v > 0, nums, set()):
                return True
        return False

    def testStep(
        self, index: int, forward: bool, nums: List[int], visited: Set[int]
    ) -> bool:
        v = nums[index]
        if v == 0:
            return False
        if v < 0 and forward or v > 0 and not forward:
            return False

        next = (index + v) % len(nums)
        if next in visited and next != index:
            return True

        visited.add(index)
        if next not in visited:
            return self.testStep(next, forward, nums, visited)
        else:
            return next != index
