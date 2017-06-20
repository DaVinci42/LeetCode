"""
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None:
            return 0
        length = len(nums)
        if length <= 3:
            return sum(nums[i] for i in range(0, length))

        nums.sort()
        min_sum = sum(nums[i] for i in range(0, 3))
        if min_sum >= target:
            return min_sum

        max_sum = sum(nums[i] for i in range(length - 3, length))
        if max_sum <= target:
            return max_sum

        result = min_sum
        for i in range(0, length - 2):
            v1 = nums[i]
            if i > 0 and v1 == nums[i - 1]:
                continue
            for j in range(i + 1, length - 1):
                v2 = nums[j]
                if j > i + 1 and v2 == nums[j - 1]:
                    continue

                left = nums[j + 1]
                right = nums[length - 1]

                sum_left = v1 + v2 + left
                sum_right = v1 + v2 + right
                diff_now = abs(target - result)

                if target < sum_left:
                    if abs(target - sum_left) < diff_now:
                        result = sum_left
                    continue
                elif target > sum_right:
                    if abs(target - sum_right) < diff_now:
                        result = sum_right
                    continue
                else:
                    desired = target - v1 - v2
                    l, r = j + 1, length - 1
                    while r - l > 1:
                        mid = (l + r) // 2
                        if nums[mid] == desired:
                            return target
                        elif nums[mid] < desired:
                            l = mid
                        else:
                            r = mid
                    if abs(desired - nums[l]) < diff_now:
                        result = v1 + v2 + nums[l]
                    if abs(desired - nums[r]) < diff_now:
                        result = v1 + v2 + nums[r]

        return result
