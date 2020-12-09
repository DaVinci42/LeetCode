class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pList, sList = list(pattern), s.split(" ")
        if len(pList) != len(sList):
            return False

        pDict, sDict = {}, {}
        for i, p in enumerate(pList):
            c = sList[i]

            if p in pDict and pDict[p] != c or c in sDict and sDict[c] != p:
                return False

            if p not in pDict:
                pDict[p] = c
            if c not in sDict:
                sDict[c] = p
        return True