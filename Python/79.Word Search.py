"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None or len(board) == 0:
            return False
        if word is None or len(word) == 0:
            return False

        option_list = []

        target = word[0]
        for r in range(0, len(board)):
            row = board[r]
            for c in range(0, len(row)):
                letter = row[c]
                if letter == target:
                    path = set()
                    path.add(str(r) + "-" + str(c))
                    option_list.append([0, r, c, path])
        if len(word) == 1:
            return len(option_list) > 0

        while len(option_list) > 0:
            record = option_list.pop()
            index = record[0] + 1

            if index >= len(word):
                return True

            r, c, path = record[1], record[2], record[3]

            target = word[index]
            if c > 0 and board[r][c - 1] == target:
                left = str(r) + "-" + str(c - 1)
                if left not in path:
                    a_path = path.copy()
                    a_path.add(left)
                    option_list.append([index, r, c - 1, a_path])
            if r > 0 and board[r - 1][c] == target:
                top = str(r - 1) + "-" + str(c)
                if top not in path:
                    a_path = path.copy()
                    a_path.add(top)
                    option_list.append([index, r - 1, c, a_path])
            if c < len(board[r]) - 1 and board[r][c + 1] == target:
                right = str(r) + "-" + str(c + 1)
                if right not in path:
                    a_path = path.copy()
                    a_path.add(right)
                    option_list.append([index, r, c + 1, a_path])
            if r < len(board) - 1 and board[r + 1][c] == target:
                bottom = str(r + 1) + "-" + str(c)
                if bottom not in path:
                    a_path = path.copy()
                    a_path.add(bottom)
                    option_list.append([index, r + 1, c, a_path])
        return False
