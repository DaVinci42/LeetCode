"""
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.
"""

import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        length = int(math.log10(x) + 1)
        i, j = 0, length - 1
        while i < j:
            right = self.get_index_num_from_right(x, i)
            left = self.get_index_num_from_right(x, j)
            if right != left:
                return False
            i += 1
            j -= 1
        return True

    def get_index_num_from_right(self, num, index):
        result = num // math.pow(10, index) - \
            (num // math.pow(10, index + 1)) * 10
        return int(result)
