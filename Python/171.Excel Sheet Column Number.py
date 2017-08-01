"""
171. Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""


class Solution(object):

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        r = []
        for c in s:
            n = ord(c) - 64
            r.append(n)
        r = r[::-1]
        print(r)

        d, result = 1, 0
        for i in r:
            result += (d * i)
            d *= 26
        return result
