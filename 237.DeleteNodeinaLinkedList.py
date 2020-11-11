# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        if not node or not node.next:
            return

        while node.next:
            nextNode = node.next
            node.val, nextNode.val = nextNode.val, node.val

            if not nextNode.next:
                node.next = None
            else:
                node = nextNode
