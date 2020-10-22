# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricTrees(root.left, root.right)

    def isSymmetricTrees(self, left: TreeNode, right: TreeNode) -> bool:
        if not left or not right:
            return not left and not right
        if left.val != right.val:
            return False
        return self.isSymmetricTrees(left.left, right.right) and self.isSymmetricTrees(
            left.right, right.left
        )
