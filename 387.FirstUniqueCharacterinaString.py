from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        c = Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1