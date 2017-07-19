"""
83. Remove Duplicates from Sorted List

Given a sorted linked list,
delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        start_node, next_node = head, head.next
        start_node.next = None
        while next_node is not None:
            if next_node.val == start_node.val:
                next_node = next_node.next
            else:
                start_node.next = next_node
                start_node = next_node
                next_node = next_node.next
                start_node.next = None
        return head
