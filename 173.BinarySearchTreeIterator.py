from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.cache = self.buildSmallest(root)

    def next(self) -> int:
        n = self.cache.pop()
        if n.right:
            self.cache = self.cache + self.buildSmallest(n.right)
        return n.val

    def hasNext(self) -> bool:
        return self.cache

    def buildSmallest(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []
        result = [root]
        if root.left:
            result += self.buildSmallest(root.left)
        return result
