"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        min_length = len(strs[0])
        for str in strs:
            length = len(str)
            if length < min_length:
                min_length = length

        for i in range(0, min_length):
            char = strs[0][i]
            for j in range(1, len(strs)):
                c = strs[j][i]
                if char != c:
                    return strs[0][:i]
        return strs[0][:min_length]
