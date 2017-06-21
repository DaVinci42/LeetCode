"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None or len(lists) == 0:
            return []

        ListNode.__lt__ = lambda a, b: a.val < b.val
        list = []
        for i in lists:
            if i is not None:
                list.append(i)
        lists = list
        lists.sort()

        head, node = None, None
        while len(lists) > 0:
            min = lists[0]
            if node is None:
                node = min
                head = min
            else:
                node.next = min
                node = min
            new_node = min.next
            if new_node is not None:
                lists[0] = new_node
                lists.sort()
            else:
                lists.remove(min)
        return head
