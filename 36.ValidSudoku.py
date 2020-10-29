from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(nums: List[chr]) -> bool:
            ns = [n for n in nums if n != "."]
            return len(ns) == len(set(ns))

        for r in range(0, 9):
            if not valid(board[r]):
                return False
        for c in range(0, 9):
            if not valid([board[i][c] for i in range(0, 9)]):
                return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not valid(
                    [board[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
                ):
                    return False
        return True
