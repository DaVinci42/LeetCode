# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast:
            if fast.next == None:
                return slow
            if fast.next.next == None:
                return slow.next
            slow = slow.next
            fast = fast.next.next
