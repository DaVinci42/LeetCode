class Solution:
    def validPalindrome(self, input: str) -> bool:
        s = list(input)
        reversedS = s[::-1]
        if s == reversedS:
            return True

        for i in range(0, len(s)):
            if s[i] == reversedS[i]:
                continue
            del s[i]
            del reversedS[i]
            if s == s[::-1]:
                return True
            elif reversedS == reversedS[::-1]:
                return True
            else:
                return False
