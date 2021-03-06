from typing import List, Iterator
import itertools


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def generateHour(n: int) -> Iterator[int]:
            return filter(
                lambda s: s <= 11,
                map(lambda t: sum(t), itertools.combinations([8, 4, 2, 1], n)),
            )

        def generateMinute(n: int) -> Iterator[int]:
            return filter(
                lambda s: s <= 59,
                map(
                    lambda t: sum(t),
                    itertools.combinations([32, 16, 8, 4, 2, 1], n),
                ),
            )

        res = []
        for h in range(min(4, num) + 1):
            hs = generateHour(h)
            ms = generateMinute(num - h)
            for p in itertools.product(hs, ms):
                res.append(f"{p[0]}:{'{:0>2d}'.format(p[1])}")
        return res