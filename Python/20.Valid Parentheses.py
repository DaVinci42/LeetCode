"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Subscribe to see which companies asked this question.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = set(['(', '[', '{'])
        right = set([')', ']', '}'])
        cache = []
        for c in s:
            if c in left:
                cache.append(c)
            elif c in right:
                if len(cache) == 0:
                    return False
                l = cache.pop()
                if not self.isPair(l, c):
                    return False

        return len(cache) == 0

    def isPair(self, l, r):
        return (l == '(' and r == ')') or (l == '[' and r == ']') or (l == '{' and r == '}')
