"""
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        if head is None:
            return head

        new_head, last_node = None, None
        tmp_node = head
        while tmp_node is not None:
            if (tmp_node.next is None or tmp_node.next.val != tmp_node.val):

                if last_node is None:
                    last_node = tmp_node
                    new_head = last_node
                else:
                    last_node.next = tmp_node
                    last_node = last_node.next
                tmp_node = tmp_node.next
                last_node.next = None

            else:
                current_val = tmp_node.val
                while tmp_node is not None and tmp_node.val == current_val:
                    tmp_node = tmp_node.next

        return new_head
