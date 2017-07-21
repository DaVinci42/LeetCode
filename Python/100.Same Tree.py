"""
100. Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif not self.is_node_same(p, q):
            return False

        s1, s2 = [p], [q]
        while len(s1) > 0:
            node1 = s1.pop()
            node2 = s2.pop()
            if not self.is_node_same(node1, node2):
                return False
            if node1.left is not None:
                s1.append(node1.left)
                s2.append(node2.left)
            if node1.right is not None:
                s1.append(node1.right)
                s2.append(node2.right)
        return True

    def is_node_same(self, p, q):
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return (self.is_node_same(p.left, q.left) and
                    self.is_node_same(p.right, q.right))
