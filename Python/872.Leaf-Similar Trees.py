"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leaf_of_tree(root1) == self.leaf_of_tree(root2)

    def leaf_of_tree(self, root):
        result = list()
        if not root:
            return result
        if root.left is None and root.right is None:
            result.append(root.val)

        if root.right is not None:
            result += self.leaf_of_tree(root.right)
        if root.left is not None:
            result += self.leaf_of_tree(root.left)
        return result
