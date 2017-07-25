"""
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = []
        self.check_sum([], 0, root, sum, result)
        return result

    def check_sum(self, pre_num, pre_sum, node, target, result):
        current = pre_sum + node.val
        pre_num.append(node.val)
        if node.left is not None:
            pre_list = pre_num[:]
            self.check_sum(pre_list, current, node.left, target, result)
        if node.right is not None:
            pre_list = pre_num[:]
            self.check_sum(pre_list, current, node.right, target, result)
        if node.left is None and node.right is None and current == target:
            result.append(pre_num)
