from typing import Set
from typing import Tuple


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        self.records: Set[Tuple[int, int]] = set()
        for i in range(0, len(s)):
            self.records.add((i, i))
        self.cache = set()
        while self.records:
            left, right = self.records.pop()
            n_l, n_r = self.grow(left, right, s)
            if (left, right) != (n_l, n_r):
                self.records.add((n_l, n_r))
            self.cache.add((left, right))
        result = max(self.cache, key=lambda t: t[1] - t[0])
        return s[result[0]:result[1] + 1]

    def grow(self, left, right, s) -> Tuple[int, int]:
        if left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
            return left - 1, right + 1
        elif left == right:
            while left > 0 and s[left - 1] == s[right]:
                left -= 1
            while right < len(s) - 1 and s[right + 1] == s[left]:
                right += 1
            return left, right
        else:
            return left, right
