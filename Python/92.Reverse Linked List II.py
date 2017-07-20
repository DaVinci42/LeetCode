"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n ? length of list.
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or m == n:
            return head

        pre_node = None
        node, index = head, 1
        if not m > 1:
            pre_node = None
        else:
            node, index = head, 1
            while index < m - 1:
                node = node.next
                index += 1
            pre_node = node

        while index < n:
            node = node.next
            index += 1
        after_node = node.next

        node = head if pre_node is None else pre_node.next
        reversed_node = []
        while node != after_node:
            reversed_node.append(node)
            node = node.next

        node, start = None, None
        while len(reversed_node) > 0:
            n = reversed_node.pop()
            if node is None:
                node = n
                start = n
            else:
                node.next = n
                node = n

        node.next = after_node

        if pre_node is None:
            return start
        else:
            pre_node.next = start
            return head
