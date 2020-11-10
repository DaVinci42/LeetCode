# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def match(treeNode: TreeNode, listNode: ListNode) -> bool:
    if not listNode:
        return True
    if not treeNode:
        return False

    if treeNode.val != listNode.val:
        return False
    return match(treeNode.left, listNode.next) or match(treeNode.right, listNode.next)


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head or not root:
            return not head and not root

        if match(root, head):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
