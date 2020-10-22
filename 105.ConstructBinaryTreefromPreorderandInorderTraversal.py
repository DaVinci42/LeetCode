from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        root = preorder[0]
        indexRoot = inorder.index(root)
        return TreeNode(
            root,
            self.buildTree(
                preorder[1:indexRoot + 1], inorder[:indexRoot]),
            self.buildTree(preorder[indexRoot + 1:], inorder[indexRoot + 1:]))
