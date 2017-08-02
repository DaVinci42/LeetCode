"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        row, result = [root], []
        while len(row) > 0:
            result.append(row[-1].val)
            tmp_row = []
            for node in row:
                if node.left is not None:
                    tmp_row.append(node.left)
                if node.right is not None:
                    tmp_row.append(node.right)
            row = tmp_row
        return result
