"""
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.find_count(n, {})

    def find_count(self, n, cache):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            count = 0
            for i in range(1, n + 1):
                # left_combine * right_combine
                count += (self.find_count(i - 1, cache) *
                          self.find_count(n - i, cache))
            cache[n] = count
            return count
