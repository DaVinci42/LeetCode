"""
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        elif head.next.next is None:
            n1, n2 = head, head.next
            n1.next = None
            n2.next = None
            if n1.val <= n2.val:
                n1.next = n2
                head = n1
            else:
                n2.next = n1
                head = n2
            return head

        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        left_head, right_head = head, slow.next
        slow.next = None
        left_node, right_node = self.sortList(left_head), self.sortList(right_head)

        new_head, new_tail = None, None
        while left_node is not None or right_node is not None:
            min_node = None
            if left_node is None:
                min_node = right_node
                right_node = right_node.next
            elif right_node is None:
                min_node = left_node
                left_node = left_node.next
            else:
                if left_node.val <= right_node.val:
                    min_node = left_node
                    left_node = left_node.next
                else:
                    min_node = right_node
                    right_node = right_node.next
            if new_head is None:
                new_head = min_node
                new_tail = min_node
            else:
                new_tail.next = min_node
                new_tail = min_node
        return new_head
