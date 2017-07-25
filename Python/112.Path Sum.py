"""
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    path_found = False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        self.path_found = False
        self.check_sum(0, root, sum)
        return self.path_found

    def check_sum(self, pre_sum, node, target):
        if self.path_found:
            return
        current = pre_sum + node.val

        if node.left is not None:
            self.check_sum(current, node.left, target)
        if node.right is not None:
            self.check_sum(current, node.right, target)
        if node.left is None and node.right is None and current == target:
            self.path_found = True
