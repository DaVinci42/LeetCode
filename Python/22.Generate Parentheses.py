"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate('', result, n, n)
        return result

    def generate(self, pre, result, left, right):
        if right == 0:
            result.append(pre)
            return
        if left == right:
            self.generate(pre + '(', result, left - 1, right)
        elif left == 0:
            self.generate(pre + ')', result, left, right - 1)
        else:
            self.generate(pre + '(', result, left - 1, right)
            self.generate(pre + ')', result, left, right - 1)
