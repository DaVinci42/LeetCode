"""
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        elif head.next is None:
            return TreeNode(head.val)

        pre, slow, fast = None, head, head
        while fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
            else:
                break

        top = TreeNode(slow.val)
        if pre is not None:
            pre.next = None

        top.left = self.sortedListToBST(head)
        top.right = self.sortedListToBST(slow.next)
        return top
