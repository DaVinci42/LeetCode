from typing import List
from collections import Counter
import itertools


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        counter, res = Counter(nums), []
        for k, ns in itertools.groupby(counter.most_common()[::-1], key=lambda t: t[1]):
            for n in sorted(ns, reverse=True):
                for _ in range(k):
                    res.append(n[0])
        return res
