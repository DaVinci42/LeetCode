from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def options(row: int, col: int) -> Set[str]:
            return set([str(i) for i in range(1, 10)]).difference(
                set([s for s in board[row] if s != "."])
                .union(
                    set([board[r][col] for r in range(0, 9) if board[r][col] != "."])
                )
                .union(
                    set(
                        [
                            board[r][c]
                            for r in range(3 * (row // 3), 3 * (row // 3) + 3)
                            for c in range(3 * (col // 3), 3 * (col // 3) + 3)
                            if board[r][c] != "."
                        ]
                    )
                )
            )

        def solve(row: int, col: int) -> bool:
            if col >= 9 and row >= 8:
                return True

            if col >= 9 and row < 8:
                return solve(row + 1, 0)

            if board[row][col] != ".":
                return solve(row, col + 1)

            for n in options(row, col):
                board[row][col] = n
                if solve(row, col + 1):
                    return True
                else:
                    board[row][col] = "."
            return False

        solve(0, 0)
