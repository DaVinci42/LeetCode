from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = []
        for i in range(0, len(strs[0])):
            c = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return ''.join(result)
            result.append(c)
        return ''.join(result)
