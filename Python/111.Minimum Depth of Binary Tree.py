"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

# Definition for a binary tree node.


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        row_list = [root]
        current_depth = 1
        while len(row_list) > 0:
            tmp_list = list()
            for n in row_list:
                if n.left is None and n.right is None:
                    return current_depth
                if n.left is not None:
                    tmp_list.append(n.left)
                if n.right is not None:
                    tmp_list.append(n.right)
            current_depth += 1
            row_list = tmp_list
