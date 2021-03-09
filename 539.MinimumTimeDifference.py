from typing import List
import sys
from itertools import chain


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(s: str) -> List[int]:
            h, m = int(s[:2]), int(s[-2:])
            return [h * 60 + m, (h + 24) * 60 + m]

        timeList = sorted(chain(*map(convert, timePoints)))

        res = sys.maxsize
        for i in range(0, len(timeList) - 1):
            res = min(timeList[i + 1] - timeList[i], res)
            if res == 0:
                return 0
        return res
