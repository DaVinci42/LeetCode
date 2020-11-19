class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t:
            return not s and not t
        if len(s) != len(t):
            return False

        sDict = {}
        for i, c in enumerate(s):
            if c not in sDict:
                sDict[c] = t[i]
            elif sDict[c] != t[i]:
                return False

        tDict = {}
        for i, c in enumerate(t):
            if c not in tDict:
                tDict[c] = s[i]
            elif tDict[c] != s[i]:
                return False

        return True
