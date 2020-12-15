from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def isLeaf(left: int, top: int, size: int) -> bool:
            return all(
                map(
                    lambda p: p == grid[top][left],
                    (
                        grid[m][n]
                        for m in range(top, top + size)
                        for n in range(left, left + size)
                    ),
                )
            )

        def construct(left: int, top: int, size: int) -> Node:
            if isLeaf(left, top, size):
                return Node(
                    isLeaf=True,
                    val=grid[top][left],
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None,
                )
            childSize = size // 2
            return Node(
                isLeaf=False,
                val=1,
                topLeft=construct(left, top, childSize),
                topRight=construct(left + childSize, top, childSize),
                bottomLeft=construct(left, top + childSize, childSize),
                bottomRight=construct(left + childSize, top + childSize, childSize),
            )

        return construct(0, 0, len(grid))
