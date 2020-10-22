from typing import List, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        return self.build(
            inorder,
            0,
            len(inorder) - 1,
            postorder,
            0,
            len(postorder) - 1,
            {k: i for i, k in enumerate(inorder)},
        )

    def build(
        self,
        inorder: List[int],
        inLeft: int,
        inRight: int,
        postorder: List[int],
        postLeft: int,
        postRight: int,
        indexCache: Dict[int, int],
    ) -> TreeNode:
        if postLeft > postRight:
            return None
        elif postLeft == postRight:
            return TreeNode(postorder[postRight])

        root = postorder[postRight]
        index = indexCache[root]
        return TreeNode(
            root,
            self.build(
                inorder,
                inLeft,
                max(0, index - 1),
                postorder,
                postLeft,
                postLeft + index - inLeft - 1,
                indexCache,
            ),
            self.build(
                inorder,
                index + 1,
                inRight,
                postorder,
                postLeft + index - inLeft,
                postRight - 1,
                indexCache,
            ),
        )
