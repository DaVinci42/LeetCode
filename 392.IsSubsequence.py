class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def isSub(ss: str, sIndex: int, tt: str, tIndex: int) -> bool:
            if sIndex >= len(ss):
                return True
            for i in range(tIndex, len(tt)):
                if tt[i] == ss[sIndex]:
                    return isSub(ss, sIndex + 1, tt, i + 1)
            return False

        return isSub(s, 0, t, 0)