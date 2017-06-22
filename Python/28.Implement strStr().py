"""
28. Implement strStr()

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None or len(needle) == 0:
            return 0
        if haystack is None or len(haystack) == 0:
            return -1

        for i in range(0, len(haystack) - len(needle) + 1):
            if self.is_match_at_index(haystack, needle, i):
                return i

        return -1

    def is_match_at_index(self, string, key, index):
        for i in range(0, len(key)):
            if string[i + index] != key[i]:
                return False
        return True
