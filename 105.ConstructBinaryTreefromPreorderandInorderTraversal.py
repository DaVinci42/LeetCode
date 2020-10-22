from typing import List, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        return self.build(
            preorder,
            0,
            len(preorder) - 1,
            inorder,
            0,
            len(inorder) - 1,
            {k: i for i, k in enumerate(inorder)},
        )

    def build(
        self,
        preorder: List[int],
        preLeft: int,
        preRight: int,
        inorder: List[int],
        inLeft: int,
        inRight: int,
        indexCache: Dict[int, int],
    ) -> TreeNode:
        if preLeft > preRight:
            return None
        elif preLeft == preRight:
            return TreeNode(preorder[preLeft])

        root = preorder[preLeft]
        index = indexCache[root]
        return TreeNode(
            root,
            self.build(
                preorder,
                preLeft + 1,
                preLeft + index - inLeft,
                inorder,
                inLeft,
                index - 1,
                indexCache,
            ),
            self.build(
                preorder,
                preLeft + index - inLeft + 1,
                preRight,
                inorder,
                index + 1,
                inRight,
                indexCache,
            ),
        )
