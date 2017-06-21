"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head, node = None, None
        while l1 is not None and l2 is not None:
            min = None
            if l1.val <= l2.val:
                min = l1
                l1 = l1.next
            else:
                min = l2
                l2 = l2.next

            if node is None:
                node = min
                head = node
            else:
                node.next = min
                node = node.next

        if l1 is None:
            node.next = l2
        if l2 is None:
            node.next = l1
        return head
