from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        return self.path(root, "")

    def path(self, node: TreeNode, parents: str) -> List[str]:
        p = f"{node.val}" if not parents else f"{parents}->{node.val}"

        if not node.left and not node.right:
            return [p]
        return (self.path(node.left, p) if node.left else []) + (
            self.path(node.right, p) if node.right else []
        )
