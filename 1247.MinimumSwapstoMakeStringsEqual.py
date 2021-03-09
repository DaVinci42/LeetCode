from collections import Counter


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        l1, l2 = list(s1), list(s2)
        for i in range(len(s1) - 1, -1, -1):
            if l1[i] == l2[i]:
                del l1[i]
                del l2[i]

        c = Counter(l1)
        res, xSize, ySize = 0, c["x"], c["y"]
        res += xSize // 2
        xSize = xSize % 2
        res += ySize // 2
        ySize = ySize % 2

        if xSize == 0 and ySize == 0:
            return res
        elif xSize == 1 and ySize == 1:
            return res + 2
        else:
            return -1
