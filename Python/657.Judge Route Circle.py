"""
657. Judge Route Circle

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true


Example 2:
Input: "LL"
Output: false
"""


class Solution:

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if not moves:
            return False

        current = (0, 0)

        for m in moves:
            x, y = current
            if m == 'U':
                current = (x, y - 1)
            elif m == 'R':
                current = (x + 1, y)
            elif m == 'D':
                current = (x, y + 1)
            elif m == 'L':
                current = (x - 1, y)

        return current == (0, 0)
