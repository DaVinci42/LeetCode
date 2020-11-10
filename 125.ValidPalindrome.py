class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        cs = [c.lower() for c in s if c.isalnum()]
        return cs == cs[::-1]
