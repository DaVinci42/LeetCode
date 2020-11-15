class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s

        return " ".join(list(filter(lambda c: c, s.split(" ")))[::-1])

s = Solution()
print(s.reverseWords("the sky is blue"))