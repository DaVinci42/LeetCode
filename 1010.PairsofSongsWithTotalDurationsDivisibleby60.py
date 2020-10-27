from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return 0

        n = [0] * 60
        for t in time:
            n[t % 60] += 1

        count = 0
        for i in range(1, 30):
            if not n[i] or not n[60 - i]:
                continue
            count += n[i] * n[60 - i]

        t0 = n[0]
        if t0 > 1:
            count += int(t0 * (t0 - 1) / 2)
        t30 = n[30]
        if t30 > 1:
            count += int(t30 * (t30 - 1) / 2)
        return count
