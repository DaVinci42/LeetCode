"""
46. Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        available = set()
        for i in nums:
            available.add(i)
        result = []
        self.pick(available, [], result)
        return result

    def pick(self, available, pre_nums, result):
        if len(available) == 0:
            result.append(pre_nums)
            return
        for i in available:
            pre = pre_nums[:]
            avail = available.copy()
            pre.append(i)
            avail.remove(i)
            self.pick(avail, pre, result)
