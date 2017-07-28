"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        slow, fast = head, head
        while fast is not None and fast.next is not None:
            if fast.next == slow:
                return True
            slow = slow.next
            if fast.next.next is None:
                return False
            else:
                fast = fast.next.next

        return False
