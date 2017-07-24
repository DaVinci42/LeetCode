"""
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
"""


# Definition for a binary tree node.

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None:
            return None
        length = len(nums)
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(nums[0])

        i_top = len(nums) // 2
        top = TreeNode(nums[i_top])
        top.left = self.sortedArrayToBST(nums[:i_top])
        top.right = self.sortedArrayToBST(nums[i_top + 1:])
        return top
