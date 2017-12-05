"""
40. Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""


class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or len(candidates) <= 0:
            return []
        candidates.sort()
        if target < candidates[0]:
            return []

        result, handled = [], set()
        for i in range(0, len(candidates)):
            self.find_num(i, candidates, target, [], handled, result)
        return result

    def find_num(self, index, nums, target, pre_nums, handled, result):
        if index >= len(nums):
            return
        pre_nums = pre_nums[:]
        num = nums[index]
        if target < num:
            return
        elif target == num:
            pre_nums.append(num)
            key = ''
            for n in pre_nums:
                key += str(n)
            if key not in handled:
                handled.add(key)
                result.append(pre_nums)
        else:
            pre_nums.append(num)
            for j in range(index + 1, len(nums)):
                self.find_num(j, nums, target - num,
                              pre_nums, handled, result)
