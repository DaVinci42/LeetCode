# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n < 1:
            return None

        right = head
        for _ in range(0, n - 1):
            if right.next:
                right = right.next
            else:
                return None

        left: ListNode = None
        while right.next:
            right = right.next
            if left == None:
                left = head
            else:
                left = left.next

        if not left:
            return head.next
        else:
            left.next = left.next.next
            return head
