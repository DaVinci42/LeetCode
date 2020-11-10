from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not k:
            return []
        if not root:
            return [None] * k

        num, node = 0, root
        while node:
            num += 1
            node = node.next

        largeNum, smallLen = num % k, num // k
        res = [None] * k
        node = root
        for i in range(0, largeNum * (smallLen + 1)):
            if i % (smallLen + 1) == 0:
                res[i // (smallLen + 1)] = node
            newNode = node.next
            if i % (smallLen + 1) == smallLen:
                node.next = None
            node = newNode

        for i in range(largeNum * (smallLen + 1), num):
            if (i - largeNum * (smallLen + 1)) % smallLen == 0:
                res[largeNum + (i - largeNum * (smallLen + 1)) // smallLen] = node
            newNode = node.next
            if (i - largeNum * (smallLen + 1)) % smallLen == smallLen - 1:
                node.next = None
            node = newNode
        return res
