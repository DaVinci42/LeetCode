"""
671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node.
If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree,
you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
# Definition for a binary tree node.


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        value_set = set([root.val])
        row_nodes = [root]
        while len(row_nodes) > 0:
            tmp_list = list()
            for n in row_nodes:
                if n.left is not None:
                    tmp_list.append(n.left)
                    value_set.add(n.left.val)
                if n.right is not None:
                    tmp_list.append(n.right)
                    value_set.add(n.right.val)

            row_nodes = tmp_list

        if len(value_set) <= 1:
            return -1
        else:
            s = list(value_set)
            s.sort()
            return s[1]
