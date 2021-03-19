from typing import List, Dict
from queue import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if root is None or root == p or root == q:
            return root

        parentDict: Dict[TreeNode, TreeNode] = {}
        d = deque([root])
        while d:
            for i in range(len(d)):
                n = d.pop()
                if n.left:
                    parentDict[n.left] = n
                    d.appendleft(n.left)
                if n.right:
                    parentDict[n.right] = n
                    d.appendleft(n.right)

        np, pAncestor = p, [p]
        while np in parentDict:
            parent = parentDict[np]
            pAncestor.append(parent)
            np = parent

        nq, qAncestor = q, [q]
        while nq in parentDict:
            parent = parentDict[nq]
            qAncestor.append(parent)
            nq = parent

        res = None
        i, j = len(pAncestor) - 1, len(qAncestor) - 1
        while i >= 0 and j >= 0 and pAncestor[i] == qAncestor[j]:
            res = pAncestor[i]
            i -= 1
            j -= 1
        return res