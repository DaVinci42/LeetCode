from collections import Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        valList, node = [], head
        while node:
            valList.append(node.val)
            node = node.next
        counter = Counter(valList)
        res = sorted([k for k in counter if counter[k] == 1])
        head, preNode = None, None
        for v in res:
            node = ListNode(v)
            if not preNode:
                head = node
                preNode = node
            else:
                preNode.next = node
                preNode = node
        return head
