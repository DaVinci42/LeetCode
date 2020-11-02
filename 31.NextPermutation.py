from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums or len(nums) <= 1:
            return

        def reverse(left: int, right: int) -> None:
            while right > left:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1 and nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        reverse(i + 1, len(nums) - 1)
                        break
                return
        reverse(0, len(nums) - 1)
