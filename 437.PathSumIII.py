# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        self.numOfPath = 0
        self.findTarget(root, s)
        return self.numOfPath

    def findTarget(self, node: TreeNode, target: int):
        if not node:
            return
        self.testHead(node, target)

        [self.findTarget(n, target) for n in (node.left, node.right)]

    def testHead(self, node: TreeNode, target: int):
        if not node:
            return
        if node.val == target:
            self.numOfPath += 1
        [self.testHead(n, target - node.val) for n in (node.left, node.right)]
