"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        slow, fast = head, head
        has_cycle = False
        while fast is not None and fast.next is not None:
            if fast.next == slow:
                has_cycle = True
                break
            slow = slow.next
            if fast.next.next is None:
                return None
            else:
                fast = fast.next.next

        if not has_cycle:
            return None

        fast = slow.next.next
        slow = slow.next
        length = 1
        while fast != slow:
            fast = fast.next.next
            slow = slow.next
            length += 1

        slow, fast, step = head, head, 1
        while step < length:
            fast = fast.next
            step += 1

        while fast.next != slow:
            slow = slow.next
            fast = fast.next
        return slow
