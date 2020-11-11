# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        def prune(node: TreeNode) -> bool:
            if not node:
                return True
            if not node.left and not node.right:
                return node.val == 0

            delLeft, delRight = prune(node.left), prune(node.right)
            if delLeft:
                node.left = None
            if delRight:
                node.right = None
            return delLeft and delRight and node.val == 0

        if prune(root):
            return None
        else:
            return root
