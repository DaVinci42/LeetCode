"""
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or (root.left is None and root.right is None):
            return 0

        # key is node
        # value is (left_child_longest_path, right_child_longest_path, max_child_longest_path)
        node_path_dict = dict()
        self.path_of_node(root, node_path_dict)
        return max(map(lambda p: p[0] + p[1], list(node_path_dict.values())))

    def path_of_node(self, node, path_dict):
        if node in path_dict:
            return path_dict[node]
        left_child_path, right_child_path = 0, 0
        if node.left is not None:
            left_child_path = self.path_of_node(node.left, path_dict)[2] + 1
        if node.right is not None:
            right_child_path = self.path_of_node(node.right, path_dict)[2] + 1

        path_count = (left_child_path, right_child_path, max([left_child_path, right_child_path]))
        path_dict[node] = path_count
        return path_count
