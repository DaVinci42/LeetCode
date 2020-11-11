# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        def insert(node: TreeNode) -> None:
            if node.val > val:
                if node.left:
                    insert(node.left)
                else:
                    node.left = TreeNode(val)
            elif node.val < val:
                if node.right:
                    insert(node.right)
                else:
                    node.right = TreeNode(val)

        insert(root)
        return root
