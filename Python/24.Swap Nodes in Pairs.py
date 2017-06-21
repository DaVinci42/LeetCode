"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
"""
# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        head, node = self.swap_node(head)
        n2 = head.next
        while node is not None:
            n1, node = self.swap_node(node)
            n2.next = n1
            n2 = n1.next
        return head

    def swap_node(self, node1):
        if node1.next is None:
            return node1, None

        node2 = node1.next
        node3 = node2.next
        node2.next = node1
        node1.next = node3
        return node2, node3
