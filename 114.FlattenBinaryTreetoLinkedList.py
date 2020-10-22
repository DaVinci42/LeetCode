from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        self.flattenNode(root)

    def flattenNode(self, root: TreeNode) -> Tuple[TreeNode, TreeNode]:
        if not root:
            return None

        head, tail = root, root
        if not root.left and not root.right:
            return (head, tail)

        l, r = self.flattenNode(root.left), self.flattenNode(root.right)
        root.left = None
        root.right = None
        if l:
            root.right = l[0]
            tail = l[1]
        if r:
            tail.right = r[0]
            tail = r[1]
        return (head, tail)

