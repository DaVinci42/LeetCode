from typing import List
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        q = PriorityQueue()
        for i, n in enumerate(lists):
            if not n:
                continue
            q.put((n.val, i, n))

        head: ListNode = None
        preNode: ListNode = None
        while not q.empty():
            _, idx, n = q.get()
            if n.next:
                q.put((n.next.val, idx, n.next))
            if not head:
                head = n
            if preNode:
                preNode.next = n
            preNode = n
        return head
