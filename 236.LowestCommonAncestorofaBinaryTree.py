from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if root is None or root == p or root == q:
            return root

        left, right = (
            self.lowestCommonAncestor(r, p, q) for r in (root.left, root.right)
        )
        if left and right:
            return root
        return left or right

