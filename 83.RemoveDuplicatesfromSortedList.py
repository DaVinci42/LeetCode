# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        slow, fast = head, head
        while slow:
            while fast and fast.val == slow.val:
                fast = fast.next
            if not fast:
                slow.next = None
                return head
            else:
                slow.next = fast
                slow = fast
        return head
