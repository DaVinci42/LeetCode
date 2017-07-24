"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if (preorder is None or len(preorder) == 0 or
                inorder is None or len(inorder) == 0):
            return None

        val = preorder[0]
        top = TreeNode(val)

        top_index = 0
        for i, v in enumerate(inorder):
            if v == val:
                top_index = i
                break

        top.left = self.buildTree(
            preorder[1:top_index + 1], inorder[:top_index])
        top.right = self.buildTree(
            preorder[top_index + 1:], inorder[top_index + 1:])

        return top
