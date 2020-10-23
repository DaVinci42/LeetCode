# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        if root.left:
            self.connectNode(root.left, root.right, None)
        return root

    def connectNode(self, left: Node, right: Node, tail: Node) -> Node:
        left.next = right
        right.next = tail
        if left.left:
            self.connectNode(left.left, left.right, right.left)
            self.connectNode(right.left, right.right, None if not tail else tail.left)
