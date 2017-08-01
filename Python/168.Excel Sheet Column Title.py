"""
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""

        s = []
        while n > 25:
            mod = n % 26
            if mod == 0:
                s.append(26)
                n = n // 26 - 1
            else:
                s.append(mod)
                n = n // 26
        if n > 0:
            s.append(n)

        r, s = "", s[::-1]
        for c in s:
            r += chr(64 + c)
        return r
