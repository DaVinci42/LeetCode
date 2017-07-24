"""
103. Binary Tree Zigzag Level Order Traversal


Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result, level_list = [], [root]
        is_ltr = True
        while len(level_list) > 0:
            val_list = map(lambda n: n.val, level_list[::1 if is_ltr else -1])
            tmp_list = []
            for node in level_list:
                if node.left is not None:
                    tmp_list.append(node.left)
                if node.right is not None:
                    tmp_list.append(node.right)
            level_list = tmp_list
            result.append(val_list)
            is_ltr = not is_ltr
        return result
