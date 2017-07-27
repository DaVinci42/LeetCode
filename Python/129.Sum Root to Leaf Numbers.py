"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        result = TreeNode(0)
        self.add_leaf(root, 0, result)
        return result.val

    def add_leaf(self, node, pre_sum, result):
        pre_sum = pre_sum * 10 + node.val
        if node.left is not None:
            self.add_leaf(node.left, pre_sum, result)
        if node.right is not None:
            self.add_leaf(node.right, pre_sum, result)
        if node.left is None and node.right is None:
            result.val += pre_sum
