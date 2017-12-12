"""
563. Binary Tree Tilt

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values.
Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1

Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
"""

# Definition for a binary tree node.


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        sum_dict = dict()
        self.sum_tree(root, sum_dict)

        node_stack = list([root])
        total_diff = 0
        while len(node_stack) > 0:
            node = node_stack.pop()
            left_val, right_val = 0, 0
            if node.left is not None:
                left_val = sum_dict[node.left]
                node_stack.append(node.left)
            if node.right is not None:
                right_val = sum_dict[node.right]
                node_stack.append(node.right)
            total_diff += abs(left_val - right_val)
        return total_diff

    def sum_tree(self, root, sum_dict):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            sum_dict[root] = root.val
            return root.val
        sum = root.val + self.sum_tree(root.left, sum_dict) + self.sum_tree(root.right, sum_dict)
        sum_dict[root] = sum
        return sum
