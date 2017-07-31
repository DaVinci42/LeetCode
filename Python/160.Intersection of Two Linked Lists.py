"""
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        stack_a = []
        while headA is not None:
            stack_a.append(headA)
            headA = headA.next

        stack_b = []
        while headB is not None:
            stack_b.append(headB)
            headB = headB.next

        node_a, node_b = stack_a.pop(), stack_b.pop()
        pre_node = None if node_a != node_b else node_a
        while node_a == node_b:
            pre_node = node_a
            if len(stack_a) == 0 or len(stack_b) == 0:
                break
            node_a = stack_a.pop()
            node_b = stack_b.pop()
        return pre_node
