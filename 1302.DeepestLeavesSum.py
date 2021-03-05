from queue import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        d, res = deque([root]), root.val
        while d:
            r = 0
            for i in range(len(d)):
                node = d.popleft()
                r += node.val
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res = r
        return res