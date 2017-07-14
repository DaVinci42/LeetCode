"""
77. Combinations

Given two integers n and k,
return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        elif k > n:
            return []

        result = []
        self.pick_num([], 1, n, k, result)
        return result

    def pick_num(self, pre_list, start, end, k, result):
        if len(pre_list) + end - start + 1 < k:
            return
        elif len(pre_list) == k:
            result.append(pre_list)
            return

        for i in range(start, end + 1):
            tmp_lis = pre_list[:]
            tmp_lis.append(i)
            self.pick_num(tmp_lis, i + 1, end, k, result)
