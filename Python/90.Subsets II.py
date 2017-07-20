"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums,
return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):

    subsets = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return [[]]

        self.subsets = []
        nums.sort()
        length = len(nums)
        for i in range(0, length + 1):
            if i == 0:
                self.subsets.append([])
            else:
                self.get_subset(nums, 0, i, [])

        return self.subsets

    def get_subset(self, nums, index, left_count, pre_num):
        if left_count == 0:
            if pre_num not in self.subsets:
                self.subsets.append(pre_num)
            return
        length = len(nums)
        if length - index < left_count:
            return

        add_set = set()
        for i in range(index, length):
            n = nums[i]
            if n in add_set:
                continue
            else:
                add_set.add(n)
            record = pre_num[:]
            record.append(n)
            self.get_subset(nums, i + 1, left_count - 1, record)
