"""
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        num_set = set()
        for i in range(1, n + 1):
            num_set.add(i)
        return self.generate_tree(num_set)

    def generate_tree(self, num_set):
        all_combine = []
        if num_set is None or len(num_set) == 0:
            all_combine.append(None)
        elif len(num_set) == 1:
            val = num_set.pop()
            all_combine.append(TreeNode(val))
        else:
            for i in num_set:
                clone_set = num_set.copy()
                clone_set.remove(i)
                left_num, right_num = set(), set()
                result = []
                for num in clone_set:
                    if num < i:
                        left_num.add(num)
                    else:
                        right_num.add(num)
                left_combine = self.generate_tree(left_num)
                right_combine = self.generate_tree(right_num)
                for ln in left_combine:
                    for rn in right_combine:
                        top = TreeNode(i)
                        top.left = ln
                        top.right = rn
                        result.append(top)
                all_combine += result
        return all_combine
