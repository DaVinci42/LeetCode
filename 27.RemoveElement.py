from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        i, j = 0, len(nums) - 1
        while j >= 0 and nums[j] == val:
            j -= 1
        if j < 0:
            return 0

        while i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                while j >= 0 and nums[j] == val:
                    j -= 1
                i += 1
            else:
                i += 1

        return i + (0 if nums[i] == val else 1)
