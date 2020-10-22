from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        indexRoot = inorder.index(postorder[-1])
        return TreeNode(
            postorder[-1],
            self.buildTree(inorder[:indexRoot], postorder[:indexRoot]),
            self.buildTree(inorder[indexRoot + 1 :], postorder[indexRoot:-1]),
        )
