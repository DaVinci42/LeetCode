from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        if nums[0] + nums[1] >= 0:
            return [nums[0:3]] if nums[2] == 0 else []
        if nums[-1] + nums[-2] <= 0:
            return [nums[-3:]] if nums[-3] == 0 else []

        nums_set = set(nums)
        left, result = 0, []
        while left <= len(nums) - 3 and nums[left] <= 0:
            if left > 0 and nums[left] == nums[left - 1]:
                left += 1
                continue
            v_left = nums[left]
            right = left + 1
            while right <= len(nums) - 2 and v_left + nums[right] <= 0:
                if right > left + 1 and nums[right] == nums[right - 1]:
                    right += 1
                    continue

                v_right = nums[right]
                target = 0 - v_left - v_right
                if target in nums_set:
                    if v_right < target or nums[right + 1] == target:
                        result.append([v_left, v_right, target])
                right += 1

            left += 1

        return result
