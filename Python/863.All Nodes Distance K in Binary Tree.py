"""
863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class UpWardTreeNode:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.target_node = None

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if not root:
            return list()
        if K == 0:
            return list(target.val)

        self.target_node = None
        self.convert_tree(None, root, target)
        if not self.target_node:
            return list()
        tasks, records, result = {(self.target_node, K)}, set(), set()
        while tasks:
            node, step = tasks.pop()
            records.add(node)
            parent, left, right = node.parent, node.left, node.right
            for n in [parent, left, right]:
                if n is not None and n not in records:
                    tasks.add((n, step - 1))
                    if step == 1:
                        result.add(n.val)
        return list(result)

    def convert_tree(self, parent, node, target):
        if not node:
            return None
        n = UpWardTreeNode(node.val, parent)
        n.parent = parent
        n.left = self.convert_tree(n, node.left, target)
        n.right = self.convert_tree(n, node.right, target)

        if node is target:
            self.target_node = n
        return n
