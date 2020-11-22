from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return not s and not t
        if len(s) != len(t):
            return False

        cs = Counter(s)
        ct = Counter(t)
        for k in cs:
            if k not in ct or cs[k] != ct[k]:
                return False
        return True
