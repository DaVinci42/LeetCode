# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        def rec(node: TreeNode) -> bool:
            if not node:
                return True
            elif node.val != root.val:
                return False
            return rec(node.left) and rec(node.right)

        return rec(root.left) and rec(root.right)
