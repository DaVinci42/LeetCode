from typing import List
from queue import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        d, res = deque([root]), []
        while d:
            rowMax = d[0].val
            for _ in range(len(d)):
                n = d.popleft()
                rowMax = max(n.val, rowMax)
                if n.left:
                    d.append(n.left)
                if n.right:
                    d.append(n.right)
            res.append(rowMax)
        return res