class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1 + ord(s) - ord("A")
        else:
            return self.titleToNumber(s[:-1]) * 26 + self.titleToNumber(s[-1:])