"""
530. Minimum Absolute Difference in BST

Given a binary search tree with non-negative values,
find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
"""

# Definition for a binary tree node.


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or (root.left is None and root.right is None):
            return 0

        val_list = list()
        node_stack = list([root])
        while len(node_stack) > 0:
            node = node_stack.pop()
            val_list.append(node.val)
            if node.left is not None:
                node_stack.append(node.left)
            if node.right is not None:
                node_stack.append(node.right)

        val_list.sort()
        diff = abs(val_list[0] - val_list[1])
        for i in range(0, len(val_list) - 1):
            d = abs(val_list[i] - val_list[i + 1])
            if abs(d) < diff:
                diff = abs(d)

        return diff
