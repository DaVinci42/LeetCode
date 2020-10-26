from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = self.sumLeft(root.left, True) + self.sumLeft(root.right, False)
        return sum(res)

    def sumLeft(self, node: TreeNode, isLeft: bool) -> List[int]:
        if not node:
            return [0]
        if not node.left and not node.right:
            return [node.val] if isLeft else [0]
        return self.sumLeft(node.left, True) + self.sumLeft(node.right, False)
