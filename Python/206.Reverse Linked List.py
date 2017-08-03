"""
206. Reverse Linked List

Reverse a singly linked list.
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        pre, node = head, head.next
        pre.next = None
        while node is not None:
            next = node.next
            node.next = pre
            pre, node = node, next

        return pre
