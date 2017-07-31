"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if tokens is None or len(tokens) == 0:
            return 0

        operator_set, s = set(['+', '-', '*', '/']), []
        for c in tokens:
            if c in operator_set:
                n2 = int(s.pop())
                n1 = int(s.pop())
                result = 0
                if c == '+':
                    result = n1 + n2
                elif c == '-':
                    result = n1 - n2
                elif c == '*':
                    result = n1 * n2
                else:
                    result = int(float(n1) / n2)
                s.append(result)
            else:
                s.append(c)
        return int(s.pop())
