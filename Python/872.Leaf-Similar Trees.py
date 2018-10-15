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
        return self.leafs_of_tree(root1) == self.leafs_of_tree(root2)

    def leafs_of_tree(self, root):
        if not root:
            return list()

        result, task = list(), [root]
        while task:
            last = task.pop()
            if last.left is None and last.right is None:
                result.append(last.val)
                continue
            if last.right is not None:
                task.append(last.right)
            if last.left is not None:
                task.append(last.left)
        return result
