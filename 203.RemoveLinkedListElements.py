# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        node, res = head, []
        while node:
            if node.val != val:
                res.append(node)
            node = node.next

        if not res:
            return None

        for i in range(0, len(res) - 1):
            res[i].next = res[i + 1]
        res[-1].next = None
        return res[0]
