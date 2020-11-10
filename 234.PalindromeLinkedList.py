# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        slow, fast, oddNodes = head, head, False
        while fast:
            if not fast.next:
                oddNodes = True
                break
            elif not fast.next.next:
                oddNodes = False
                break
            slow = slow.next
            fast = fast.next.next

        def reverse(node: ListNode, tail: ListNode) -> ListNode:
            if node == tail:
                node.next = None
                return node
            rightTail = reverse(node.next, tail)
            rightTail.next = node
            node.next = None
            return node

        rightHead = slow.next
        reverse(head, slow)

        def compare(n0: ListNode, n1: ListNode) -> bool:
            while n0 or n1:
                if not n0 or not n1 or n0.val != n1.val:
                    return False
                n0 = n0.next
                n1 = n1.next
            return True

        isSame = (
            compare(slow, rightHead) if not oddNodes else compare(slow.next, rightHead)
        )

        reverse(slow, head)
        slow.next = rightHead
        return isSame
