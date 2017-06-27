"""
47. Permutations II

Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []

        available = {}
        for n in nums:
            count = 0
            if n in available:
                count = available[n] + 1
            else:
                count = 1
            available[n] = count
        result = []
        self.pick(nums, available, '', set(), result)
        return result

    def pick(self, nums, available, prenums, cache, result):
        if len(available) == 0:
            lis = []
            tmp = prenums.split()
            for i in tmp:
                lis.append(int(i))
            result.append(lis)
            return

        for n in available:
            pre = prenums + ' ' + str(n)
            if pre in cache:
                continue
            avail = available.copy()
            if avail[n] == 1:
                del avail[n]
            else:
                avail[n] = avail[n] - 1
            cache.add(pre)
            self.pick(nums, avail, pre, cache, result)
