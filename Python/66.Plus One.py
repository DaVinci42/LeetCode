"""
66. Plus One

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None or len(digits) == 0:
            return 1

        for i in range(len(digits) - 1, -1, -1):
            value = digits[i]

            if value + 1 > 9:
                digits[i] = value + 1 - 10
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] = value + 1
                break
        return digits
