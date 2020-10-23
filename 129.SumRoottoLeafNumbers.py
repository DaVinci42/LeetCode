from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        sums = []
        self.findSum(root, 0, sums)
        return sum(sums)

    def findSum(self, root: TreeNode, parent: int, sums: List[int]):
        if not root:
            return 0
        parent = parent * 10 + root.val
        if not root.left and not root.right:
            sums.append(parent)
            return
        if root.left:
            self.findSum(root.left, parent, sums)
        if root.right:
            self.findSum(root.right, parent, sums)
