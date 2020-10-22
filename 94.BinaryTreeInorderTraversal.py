from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        l = [] if not root.left else self.inorderTraversal(root.left)
        r = [] if not root.right else self.inorderTraversal(root.right)
        return l + [root.val] + r
