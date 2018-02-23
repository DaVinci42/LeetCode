"""
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

# Definition for a binary tree node.


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return 0

        result = self.__tree_to_list(root)
        return result[k - 1]

    def __tree_to_list(self, root):
        result = [root.val]
        if root.left is not None:
            result = self.__tree_to_list(root.left) + result
        if root.right is not None:
            result += self.__tree_to_list(root.right)
        return result
