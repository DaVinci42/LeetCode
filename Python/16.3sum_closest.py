from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return 0

        nums.sort()
        result = sum(nums[:3])
        for i in range(0, len(nums) - 2):
            a = nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = a + nums[j] + nums[k]
                if abs(target - s) < abs(target - result):
                    result = s
                if s == target:
                    return target
                elif s < target:
                    j += 1
                else:
                    k -= 1
        return result
