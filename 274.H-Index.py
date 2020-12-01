from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        res = 0
        citations.sort(reverse=True)
        for i, n in enumerate(citations):
            if n < i + 1:
                break
            res += 1
        return res
