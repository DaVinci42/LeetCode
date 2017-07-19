"""
86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        node = head
        less_list, great_list = [], []
        while node is not None:
            if node.val < x:
                less_list.append(node)
            else:
                great_list.append(node)
            node = node.next

        if len(less_list) == 0:
            return great_list[0]
        if len(great_list) == 0:
            return less_list[0]

        head, last_node = less_list[0], less_list[0]
        for i in range(1, len(less_list)):
            node = less_list[i]
            last_node.next = node
            last_node = node

        for i in range(0, len(great_list)):
            node = great_list[i]
            last_node.next = node
            last_node = node

        last_node.next = None
        return head
