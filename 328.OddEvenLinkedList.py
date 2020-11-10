# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head

        tail = head
        while tail.next:
            tail = tail.next

        node, firstEven = head, None
        while node and node != firstEven and node.next != firstEven:
            evenNode = node.next
            node.next = evenNode.next
            node = node.next

            tail.next = evenNode
            tail = evenNode
            tail.next = None
            if not firstEven:
                firstEven = evenNode

        return head
