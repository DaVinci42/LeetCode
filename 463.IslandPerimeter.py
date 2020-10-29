from typing import List, Set, Tuple


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        cellSet: Set[Tuple[int, int]] = set()
        for r in range(0, len(grid)):
            row = grid[r]
            for c in range(0, len(grid[0])):
                if row[c] == 1:
                    cellSet.add((r, c))

        borderMap = {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}

        def cellBorder(row: int, col: int) -> int:
            count = len(
                cellSet.intersection(
                    set(
                        [(row, col - 1), (row - 1, col), (row, col + 1), (row + 1, col)]
                    )
                )
            )
            return borderMap[count]

        return sum(cellBorder(r, c) for r, c in cellSet)
