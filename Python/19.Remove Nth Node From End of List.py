"""
19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or (head.next is None and n > 0):
            return None
        fast, slow, pre = head, head, head
        step = 0
        while fast.next is not None:
            if step >= n - 1:
                pre = slow
                slow = slow.next
            fast = fast.next
            step += 1
        if slow == head:
            return head.next
        else:
            pre.next = slow.next
            return head
