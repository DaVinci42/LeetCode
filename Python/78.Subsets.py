"""
78. Subsets

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []

        result = [[]]
        for i in range(0, len(nums) + 1):
            result += self.combine(nums, i)
        return result

    def combine(self, nums, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []

        result = []
        self.pick_num(nums, [], 0, len(nums) - 1, k, result)
        return result

    def pick_num(self, nums, pre_list, start, end, k, result):
        if len(pre_list) + end - start + 1 < k:
            return
        elif len(pre_list) == k:
            result.append(pre_list)
            return

        for i in range(start, end + 1):
            tmp_lis = pre_list[:]
            tmp_lis.append(nums[i])
            self.pick_num(nums, tmp_lis, i + 1, end, k, result)
