class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1

        def test(index: int) -> bool:
            for i, c in enumerate(needle):
                if haystack[index + i] != c:
                    return False
            return True

        for i in range(0, len(haystack) - len(needle) + 1):
            if test(i):
                return i
        return -1
