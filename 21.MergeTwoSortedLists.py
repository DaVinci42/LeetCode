# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        head, preNode = None, None
        while l1 or l2:
            if not l1:
                preNode.next = l2
                return head
            if not l2:
                preNode.next = l1
                return head

            n: ListNode
            if l1.val <= l2.val:
                n = l1
                l1 = l1.next
            else:
                n = l2
                l2 = l2.next

            if not head:
                head = n
            if preNode:
                preNode.next = n
            preNode = n
        return head

