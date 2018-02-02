"""
415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 is None or len(num1) == 0:
            return num2
        if num2 is None or len(num2) == 0:
            return num1

        idx1, idx2 = len(num1) - 1, len(num2) - 1
        adding = False
        result = list()
        while idx1 >= 0 or idx2 >= 0 or adding:
            v1, v2 = 0, 0
            if idx1 >= 0:
                v1 = int(num1[idx1])
                idx1 -= 1
            if idx2 >= 0:
                v2 = int(num2[idx2])
                idx2 -= 1
            sum = v1 + v2 if not adding else v1 + v2 + 1
            adding = sum >= 10
            sum %= 10
            result.append(sum)
        return "".join(map(lambda x: str(x), result[::-1]))
