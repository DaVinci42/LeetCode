"""
8. String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated.
If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
"""
import math


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_int = int(math.pow(2, 31) - 1)
        min_int = int(-1 * math.pow(2, 31))
        if str is None or len(str) == 0:
            return 0
        allowed = set()
        allowed.add('-')
        allowed.add('+')
        for i in range(ord('0'), ord('0') + 10):
            allowed.add(chr(i))

        result = ""
        is_sign_showed = False
        is_non_zero_showed = False
        is_num_showed = False
        for i in range(0, len(str)):
            char = str[i]
            if char == ' ':
                if is_num_showed or is_sign_showed:
                    break
                else:
                    continue
            if char not in allowed:
                break
            is_sign = char == '-' or char == '+'
            if not is_sign:
                is_num_showed = True
            if is_sign and is_sign_showed:
                return 0

            is_sign_showed = True
            if char == '+':
                continue
            if char == '0' and not is_non_zero_showed:
                continue
            if char != '-' and char != '+' and char != '0':
                is_non_zero_showed = True

            result += char
        if not is_non_zero_showed:
            return 0
        result = int(result)
        if result > max_int:
            return max_int
        elif result < min_int:
            return min_int
        else:
            return int(result)
