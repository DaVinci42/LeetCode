import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right):
            return 0

        self.minDiff = sys.maxsize

        def check(node: TreeNode, lower: int, upper: int):
            self.minDiff = min(
                self.minDiff, abs(node.val - lower), abs(node.val - upper)
            )
            if node.left:
                check(node.left, lower, node.val)
            if node.right:
                check(node.right, node.val, upper)

        check(root, -sys.maxsize, sys.maxsize)
        return self.minDiff
