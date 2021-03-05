class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        def canBreak(l1: List[str], l2: List[str]) -> bool:
            for i in range(0, len(s1)):
                if l1[i] < l2[i]:
                    return False
            return True

        l1, l2 = sorted(s1), sorted(s2)
        return canBreak(l1, l2) or canBreak(l2, l1)
