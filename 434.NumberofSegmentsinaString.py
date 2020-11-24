class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        for i, c in enumerate(s):
            if c != " " and (i == 0 or s[i - 1] == " "):
                res += 1
        return res