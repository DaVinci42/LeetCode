"""
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        else:
            self.flat_tree(root)

    def flat_tree(self, node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return node

        left, right = self.flat_tree(node.left), self.flat_tree(node.right)
        original_left, original_right = node.left, node.right
        node.left = None
        if left is not None and right is not None:
            node.right = original_left
            left.right = original_right
            return right
        elif left is not None:
            node.right = original_left
            return left
        else:
            return right
