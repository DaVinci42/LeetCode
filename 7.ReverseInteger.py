import math


class Solution:
    def reverse(self, x: int) -> int:
        negative = str(x)[0] == "-"
        result = -1 * int(str(x)[1:][::-1]) if negative else int(str(x)[::-1])
        if -1 * math.pow(2, 31) <= result <= math.pow(2, 31) - 1:
            return result
        else:
            return 0
