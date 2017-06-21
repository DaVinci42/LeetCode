"""
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None

        head, end, start = self.reverse_at_k(head, k)
        while start is not None:
            end.next, end, start = self.reverse_at_k(start, k)
        return head

    def reverse_at_k(self, head, k):
        node, list = head, []
        for i in range(0, k):
            if node is None:
                return head, None, None
            list.append(node)
            node = node.next

        for i in range(1, k):
            list[i].next = list[i - 1]
        list[0].next = None
        return list[k - 1], list[0], node
