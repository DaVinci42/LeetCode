"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        over_10 = False
        head = l2
        pre_node = None
        while l1 or l2 or over_10:
            if l1 and l2:
                sum = l1.val + l2.val
                if over_10:
                    sum += 1
                if sum >= 10:
                    over_10 = True
                    l2.val = sum - 10
                else:
                    over_10 = False
                    l2.val = sum
                pre_node = l2
                l1 = l1.next
                l2 = l2.next
            elif l1 or l2:
                sum = 0
                if l1 is not None:
                    sum += l1.val
                    l1 = l1.next
                if l2 is not None:
                    sum += l2.val
                    l2 = l2.next
                if over_10:
                    sum += 1
                if sum >= 10:
                    sum -= 10
                    over_10 = True
                else:
                    over_10 = False
                node = ListNode(sum)
                pre_node.next = node
                pre_node = node
            else:
                node = ListNode(1)
                pre_node.next = node
                return head
        return head
