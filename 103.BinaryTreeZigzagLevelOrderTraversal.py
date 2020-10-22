from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        l, result, reversed = [root], [], False
        while l:
            layer, nextL = [], []
            for n in l:
                layer.append(n.val)
                if n.left:
                    nextL.append(n.left)
                if n.right:
                    nextL.append(n.right)
            l = nextL
            result.append(layer if not reversed else layer[::-1])
            reversed = not reversed
        return result
