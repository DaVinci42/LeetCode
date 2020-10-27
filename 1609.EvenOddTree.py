from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return False

        layer = deque([root])
        isEven = True
        while layer:
            preNode = None
            for _ in range(0, len(layer)):
                n = layer.popleft()
                if isEven:
                    if n.val % 2 == 0:
                        return False
                    if preNode and n.val <= preNode.val:
                        return False
                else:
                    if n.val % 2 == 1:
                        return False
                    if preNode and n.val >= preNode.val:
                        return False

                if n.left:
                    layer.append(n.left)
                if n.right:
                    layer.append(n.right)
                preNode = n

            isEven = not isEven
        return True
