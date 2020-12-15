from typing import List
from collections import Counter
import itertools


class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        if not A or not B or not C or not D:
            return 0

        abCounter = Counter(a + b for a in A for b in B)
        cdCounter = Counter(c + d for c in C for d in D)
        return sum(abCounter[s] * cdCounter[-s] for s in abCounter if -s in cdCounter)
