# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head

        count, node = 0, head
        while node:
            count += 1
            node = node.next

        k %= count
        if not k:
            return head

        slow, fast = head, head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        newHead = slow.next
        slow.next = None
        fast.next = head
        return newHead

