"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result = []
        level_list = [root]
        while len(level_list) > 0:
            val_list = []
            tmp_list = []
            for node in level_list:
                val_list.append(node.val)
                if node.left is not None:
                    tmp_list.append(node.left)
                if node.right is not None:
                    tmp_list.append(node.right)
            level_list = tmp_list
            result.append(val_list)
        return result
