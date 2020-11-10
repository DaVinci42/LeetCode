# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.head = None

        def reverse(node: ListNode) -> ListNode:
            if not node or not node.next:
                self.head = node
                return node

            tail = reverse(node.next)
            tail.next = node
            node.next = None
            return node

        reverse(head)
        return self.head
