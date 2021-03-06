from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        l, result = [root], []
        while l:
            layer, nextL = [], []
            for n in l:
                layer.append(n.val)
                if n.left:
                    nextL.append(n.left)
                if n.right:
                    nextL.append(n.right)
            result.append(layer)
            l = nextL
        return [r[-1] for r in result]
