"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.

class RandomListNode(object):

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        node_map = {}
        node = head
        while node is not None:
            n = RandomListNode(node.label)
            node_map[node] = n
            node = node.next

        for node in node_map:
            copy = node_map[node]
            if node.next is not None:
                copy.next = node_map[node.next]
            if node.random is not None:
                copy.random = node_map[node.random]

        return node_map[head]
