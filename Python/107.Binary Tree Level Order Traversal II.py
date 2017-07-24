"""
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        level_list, result = [root], []
        while len(level_list) > 0:
            tmp_list, val_list = [], []
            for node in level_list:
                val_list.append(node.val)
                if node.left is not None:
                    tmp_list.append(node.left)
                if node.right is not None:
                    tmp_list.append(node.right)
            level_list = tmp_list
            result.append(val_list)
        return result[::-1]
