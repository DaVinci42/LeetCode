"""
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        length = len(nums)
        if length <= 2:
            return []

        nums.sort()
        all_nums = {}
        for i, n in enumerate(nums):
            all_nums[n] = i

        result = []
        for i in range(0, length - 2):
            v1 = nums[i]
            if i > 0 and v1 == nums[i - 1]:
                continue
            for j in range(i + 1, length - 1):
                v2 = nums[j]
                if j > i + 1 and v2 == nums[j - 1]:
                    continue
                target = 0 - v1 - v2
                if target in all_nums and all_nums[target] > j:
                    result.append([v1, v2, target])
        return result
