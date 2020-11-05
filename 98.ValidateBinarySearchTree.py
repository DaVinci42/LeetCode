import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def isValid(node: TreeNode, lower: int, upper: int) -> bool:
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False
            if node.left and (
                node.left.val >= node.val
                or node.left.val >= upper
                or node.left.val <= lower
            ):
                return False
            if node.right and (
                node.right.val <= node.val
                or node.right.val >= upper
                or node.right.val <= lower
            ):
                return False

            return isValid(node.left, lower, node.val) and isValid(
                node.right, node.val, upper
            )

        return isValid(root, -sys.maxsize - 1, sys.maxsize)
