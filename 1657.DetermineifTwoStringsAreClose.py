from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        if set(c1.keys()) != set(c2.keys()):
            return False

        if sorted(c1.values()) != sorted(c2.values()):
            return False

        return True