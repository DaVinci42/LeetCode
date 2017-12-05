"""
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        node_list = list([root])
        left_node = list()
        while len(node_list) > 0:
            tmp_list = list()
            for n in node_list:
                if n.left is not None:
                    tmp_list.append(n.left)
                    if n.left.left is None and n.left.right is None:
                        left_node.append(n.left)
                if n.right is not None:
                    tmp_list.append(n.right)
            node_list = tmp_list

        sum = 0
        for n in left_node:
            sum += n.val
        return sum
