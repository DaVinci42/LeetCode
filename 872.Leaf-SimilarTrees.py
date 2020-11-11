from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return not root1 and not root2

        def getLeaf(node: TreeNode) -> List[int]:
            if not node.left and not node.right:
                return [node.val]

            return (getLeaf(node.left) if node.left else []) + (
                getLeaf(node.right) if node.right else []
            )

        return getLeaf(root1) == getLeaf(root2)
