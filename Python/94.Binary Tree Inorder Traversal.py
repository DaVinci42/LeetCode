"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.print_node(root)

    def print_node(self, node):
        result = [node.val]
        if node.left is None and node.right is None:
            return result
        if node.left is not None:
            left = self.print_node(node.left)
            result = left + result
        if node.right is not None:
            right = self.print_node(node.right)
            result += right
        return result
