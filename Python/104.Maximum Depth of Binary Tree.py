"""
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        level_list, level = [root], 0
        while len(level_list) > 0:
            tmp_list = []
            for node in level_list:
                if node.left is not None:
                    tmp_list.append(node.left)
                if node.right is not None:
                    tmp_list.append(node.right)
            level += 1
            level_list = tmp_list
        return level
