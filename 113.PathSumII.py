from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        if not root:
            return result
        self.findSum(root, sum, [], result)
        return result

    def findSum(
        self, root: TreeNode, sum: int, parents: List[int], result: List[List[int]]
    ):
        if not root.left and not root.right and root.val == sum:
            parents.append(sum)
            result.append(parents)
            return

        if root.left:
            p = parents[:]
            p.append(root.val)
            self.findSum(root.left, sum - root.val, p, result)
        if root.right:
            p = parents[:]
            p.append(root.val)
            self.findSum(root.right, sum - root.val, p, result)
