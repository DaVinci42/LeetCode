from typing import Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        cache = {}
        self.getHeight(root, cache)

        l = [root]
        while l:
            nextL = []
            for n in l:
                leftH, rightH = cache.get(n.left, 0), cache.get(n.right, 0)
                if abs(leftH - rightH) > 1:
                    return False
                if n.left:
                    nextL.append(n.left)
                if n.right:
                    nextL.append(n.right)
                l = nextL
        return True

    def getHeight(self, root: TreeNode, cache: Dict[TreeNode, int]) -> int:
        if not root:
            return 0
        height = 1 + max(
            self.getHeight(root.left, cache), self.getHeight(root.right, cache)
        )
        cache[root] = height
        return height

