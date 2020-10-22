# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = [root]
        depth = 0
        while l:
            depth += 1
            nextL = []
            for n in l:
                if not n.left and not n.right:
                    return depth
                if n.left:
                    nextL.append(n.left)
                if n.right:
                    nextL.append(n.right)
            l = nextL
        return depth
