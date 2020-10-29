from typing import List, Set, Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        cellSet: Set[Tuple[int, int]] = set()
        for r in range(0, len(grid)):
            row = grid[r]
            for c in range(0, len(row)):
                if row[c] == 1:
                    cellSet.add((r, c))

        maxArea = 0
        while cellSet:
            s = [cellSet.pop()]
            area = 1
            while s:
                r, c = s.pop()
                for m, n in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if (m, n) in cellSet:
                        area += 1
                        s.append((m, n))
                        cellSet.remove((m, n))
            maxArea = max(maxArea, area)

        return maxArea
