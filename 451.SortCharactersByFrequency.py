from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s

        res, counter = [], Counter(s)
        for c, count in counter.most_common():
            res += [c] * count
        return "".join(res)
