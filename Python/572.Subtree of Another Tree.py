"""
572. Subtree of Another Tree

Given two non-empty binary trees s and t,
check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None or t is None:
            return s is None and t is None
        s = list([s])
        while len(s) > 0:
            tmp_list = list()
            for n in s:
                if self.is_sub_tree(n, t):
                    return True

                if n.left is not None:
                    tmp_list.append(n.left)
                if n.right is not None:
                    tmp_list.append(n.right)
            s = tmp_list
        return False

    def is_sub_tree(self, s, t):
        if s is None or t is None:
            return s is None and t is None
        if s.val != t .val:
            return False
        return self.is_sub_tree(s.left, t.left) and self.is_sub_tree(s.right, t.right)
