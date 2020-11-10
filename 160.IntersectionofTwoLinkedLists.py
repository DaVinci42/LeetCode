from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        def nodeToStack(node: ListNode) -> List[ListNode]:
            res, n = [], node
            while n:
                res.append(n)
                n = n.next
            return res

        sA, sB = nodeToStack(headA), nodeToStack(headB)
        if sA[-1] != sB[-1]:
            return None

        n = sA[-1]
        while sA and sB and sA[-1] == sB[-1]:
            n = sA[-1]
            sA.pop()
            sB.pop()
        return n

