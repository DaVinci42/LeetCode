# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = False
        left, right = l1, l2
        head: ListNode = None
        preNode: ListNode = None
        while left or right or carry:
            sum = 0
            if left:
                sum += left.val
                left = left.next
            if right:
                sum += right.val
                right = right.next
            if carry:
                sum += 1
            carry = sum >= 10
            n = ListNode(sum % 10)
            if not preNode:
                preNode = n
                head = n
            else:
                preNode.next = n
                preNode = n
        return head
