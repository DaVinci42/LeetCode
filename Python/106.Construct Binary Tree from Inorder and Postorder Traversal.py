"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

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

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if (postorder is None or len(postorder) == 0 or
                inorder is None or len(inorder) == 0):
            return None

        val = postorder[-1]
        top = TreeNode(val)

        top_index = 0
        for i, v in enumerate(inorder):
            if v == val:
                top_index = i
                break

        top.left = self.buildTree(
            inorder[:top_index], postorder[:top_index])
        top.right = self.buildTree(
            inorder[top_index + 1:], postorder[top_index:len(postorder) - 1])

        return top
