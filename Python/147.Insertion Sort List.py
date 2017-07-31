"""
147. Insertion Sort List

Sort a linked list using insertion sort.
"""


# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        node = head.next
        head, tail = head, head
        while node is not None:
            if node.val >= tail.val:
                tail.next = node
                tail = node
                node = node.next
            elif node.val <= head.val:
                next = node.next
                node.next = head
                head = node
                node = next
            else:
                next = node.next
                self.insert(head, node)
                node = next
            tail.next = None
        return head

    def insert(self, head, node):
        pre = head
        while head.val < node.val:
            pre = head
            head = head.next
        pre.next = node
        node.next = head
