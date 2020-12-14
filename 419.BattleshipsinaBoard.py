from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        return sum(
            (
                1
                if board[m][n] == "X"
                and (m == 0 or board[m - 1][n] != "X")
                and (n == 0 or board[m][n - 1] != "X")
                else 0
                for m in range(len(board))
                for n in range(len(board[0]))
            )
        )