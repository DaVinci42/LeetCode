from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs, ct = Counter(s), Counter(t)
        for c in cs.keys():
            if c not in ct:
                continue
            minV = min(cs[c], ct[c])
            cs[c] = cs[c] - minV
            ct[c] = ct[c] - minV

        return sum(cs.values())