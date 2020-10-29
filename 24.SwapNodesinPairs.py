# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        h: ListNode = None
        tail: ListNode = None
        node = head
        while node and node.next:
            nextN = node.next.next

            if not tail:
                h = node.next
                tail = node

            tail.next = node.next
            node.next.next = node
            node.next = None
            tail = node
            node = nextN

        if node:
            tail.next = node
        return h
