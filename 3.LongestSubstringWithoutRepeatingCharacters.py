class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        cache = {}

        def grow(start: int, cur: int) -> int:
            for i in range(cur, len(s)):
                c = s[i]
                if c not in cache or cache[c] < start:
                    cache[c] = i
                else:
                    curLen = i - start
                    preC = cache[c]
                    cache[c] = i
                    return max(curLen, grow(preC + 1, i + 1))
            return len(s) - start

        return grow(0, 0)
