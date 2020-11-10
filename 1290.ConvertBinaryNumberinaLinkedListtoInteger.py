# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0

        res = []
        while head:
            res.append(str(head.val))
            head = head.next

        return int("".join(res), 2)
