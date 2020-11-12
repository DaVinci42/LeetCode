class Solution:
    def toLowerCase(self, s: str) -> str:
        if not s:
            return s
        return "".join(c.lower() for c in s)
