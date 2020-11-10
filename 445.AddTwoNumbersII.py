# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        def nodeToInt(node: ListNode) -> int:
            s, n = 0, node
            while n:
                s = s * 10 + n.val
                n = n.next
            return s

        total = nodeToInt(l1) + nodeToInt(l2)
        head, preN = None, None
        for c in str(total):
            n = ListNode(int(c))
            if not head:
                head = n
                preN = n
            else:
                preN.next = n
                preN = n
        return head
