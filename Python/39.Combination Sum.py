"""
39. Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None:
            return []
        candidates.sort()
        length = len(candidates)

        if target < candidates[0]:
            return []
        result = []
        for i in range(0, length):
            self.find_from_index(i, candidates, target, [], result, set())
        return result

    def find_from_index(self, index, nums, target, pre_list, result, handled):
        length = len(nums)
        if index >= length:
            return

        for i in range(index, length):
            num = nums[index]
            if num > target:
                break
            elif target == num:
                lis = pre_list[:]
                lis.append(num)
                key = ''
                for j in lis:
                    key += str(j)
                if key not in handled:
                    handled.add(key)
                    result.append(lis)
            else:
                lis = pre_list[:]
                lis.append(num)
                self.find_from_index(
                    i, nums, target - num, lis, result, handled)
