"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""


class Solution:

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0

        avail_dot = set()
        for y in range(0, len(grid)):
            row = grid[y]
            for x in range(0, len(row)):
                d = row[x]
                if (d == '1'):
                    avail_dot.add((x, y))

        r, c = len(grid), len(grid[0])
        count = 0

        while len(avail_dot) > 0:
            count += 1

            p = next(iter(avail_dot))
            to_handle_dots = list([p])
            avail_dot.remove(p)

            while len(to_handle_dots) > 0:
                x, y = to_handle_dots.pop()

                # left
                if x > 0 and grid[y][x - 1] == '1' and (x - 1, y) in avail_dot:
                    to_handle_dots.append((x - 1, y))
                    avail_dot.remove((x - 1, y))

                # top
                if y > 0 and grid[y - 1][x] == '1' and (x, y - 1) in avail_dot:
                    to_handle_dots.append((x, y - 1))
                    avail_dot.remove((x, y - 1))

                # right
                if (x < c - 1 and grid[y][x + 1] == '1' and
                        (x + 1, y) in avail_dot):
                    to_handle_dots.append((x + 1, y))
                    avail_dot.remove((x + 1, y))

                # bottom
                if (y < r - 1 and grid[y + 1][x] == '1' and
                        (x, y + 1) in avail_dot):
                    to_handle_dots.append((x, y + 1))
                    avail_dot.remove((x, y + 1))

        return count
