"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check_depth(root) != -1

    def check_depth(self, node):
        if node is None:
            return 0
        left, right = self.check_depth(node.left), self.check_depth(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(right - left) > 1:
            return -1
        return max(left, right) + 1
