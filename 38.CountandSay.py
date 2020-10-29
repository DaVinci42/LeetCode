from typing import Dict
from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 1:
            return ""
        elif n == 1:
            return "1"

        s = "1"
        for _ in range(0, n - 1):
            s = "".join([str(len(list(g))) + str(d) for d, g in groupby(s)])
        return s
