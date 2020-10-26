from typing import List, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ""

        return min(
            [
                p[::-1]
                for p in self.pathFromRoot(
                    root, "", {i: chr(ord("a") + i) for i in range(0, 26)}
                )
            ],
            default="",
        )

    def pathFromRoot(
        self, node: TreeNode, parents: str, m: Dict[int, str]
    ) -> List[str]:
        p = parents + m[node.val] if parents else m[node.val]
        if not node.left and not node.right:
            return [p]

        return (self.pathFromRoot(node.left, p, m) if node.left else []) + (
            self.pathFromRoot(node.right, p, m) if node.right else []
        )
