class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = ""
        for c in s:
            ss += c
            if len(ss) != len(set(ss)):
                ss = ss[1:]
        return len(ss)
