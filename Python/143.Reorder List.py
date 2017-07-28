"""
143. Reorder List

Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""


# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        node, index, dic = head, 1, {}
        while node is not None:
            dic[index] = node
            index += 1
            node = node.next

        first, last = 1, index - 1

        node = None
        while last >= first:
            if first == last:
                n = dic[first]
                n.next = None
                if node is None:
                    node = n
                else:
                    node.next = n
            else:
                n1, n2 = dic[first], dic[last]
                n1.next = n2
                n2.next = None
                if node is None:
                    node = n1
                else:
                    node.next = n1
                node = n2
            first += 1
            last -= 1
