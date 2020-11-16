from queue import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0

        depth, d = 0, deque([root])
        while d:
            depth += 1
            for _ in range(len(d)):
                n = d.popleft()
                for child in n.children:
                    d.append(child)
        return depth