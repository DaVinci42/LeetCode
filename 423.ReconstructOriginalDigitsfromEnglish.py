from collections import Counter
import itertools


class Solution:
    def originalDigits(self, s: str) -> str:
        if not s:
            return ""

        c, res = Counter(s), [0] * 10
        res[0] = c["z"]
        res[2] = c["w"]
        res[4] = c["u"]
        res[6] = c["x"]
        res[8] = c["g"]
        res[1] = c["o"] - res[0] - res[2] - res[4]
        res[7] = c["s"] - res[6]
        res[5] = c["v"] - res[7]
        res[3] = c["h"] - res[8]
        res[9] = int((c["n"] - res[1] - res[7]) / 2)

        return "".join(
            itertools.chain.from_iterable(
                [itertools.repeat(str(i), res[i]) for i in range(10)]
            )
        )
