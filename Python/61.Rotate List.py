"""
61. Rotate List

Given a list, rotate the list to the right by k places,
where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        count, node = 0, head
        while node is not None:
            count += 1
            node = node.next

        k %= count
        if k == 0:
            return head

        slow, fast = head, head
        for i in range(0, k):
            if fast is None:
                return head
            fast = fast.next

        if fast is None:
            return head

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head
