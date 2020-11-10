# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None

        lessHead, lessNode, greaterHead, greaterNode = None, None, None, None
        node = head
        while node:
            if node.val < x:
                if not lessNode:
                    lessHead = node
                    lessNode = node
                else:
                    lessNode.next = node
                    lessNode = node
            else:
                if not greaterNode:
                    greaterHead = node
                    greaterNode = node
                else:
                    greaterNode.next = node
                    greaterNode = node
            node = node.next

        if not lessHead or not greaterHead:
            return lessHead or greaterHead

        lessNode.next = greaterHead
        greaterNode.next = None

        return lessHead
