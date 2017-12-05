"""
36. Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""


class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) < 9 or len(board[0]) < 9:
            return False

        s = set()
        for row in board:
            s.clear()
            for n in row:
                if n != '.' and n in s:
                    return False
                else:
                    s.add(n)

        for i in range(0, 9):
            s.clear()
            for row in board:
                n = row[i]
                if n != '.' and n in s:
                    return False
                else:
                    s.add(n)

        for r in range(0, 3):
            for j in range(0, 3):
                if not self.is_area_valid(board, 3 * r, 3 * j):
                    return False
        return True

    def is_area_valid(self, list, r, c):
        s = set()
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                n = list[i][j]
                if n != '.' and n in s:
                    return False
                else:
                    s.add(n)
        return True
