"""
97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""


class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 is None or len(s1) == 0:
            return s2 == s3
        if s2 is None or len(s2) == 0:
            return s1 == s3
        if s3 is None:
            return False
        if len(s1) + len(s2) != len(s3):
            return False

        record = [(0, 0)]
        length1, length2 = len(s1), len(s2)
        recorded = set()

        while len(record) > 0:
            current = record.pop()
            index1, index2 = current[0], current[1]
            index = index1 + index2
            if index1 == length1 and index2 == length2:
                return True
            if index2 <= length2 - 1 and s3[index] == s2[index2]:
                next = (index1, index2 + 1)
                if next not in recorded:
                    record.append(next)
                    recorded.add(next)
            if index1 <= length1 - 1 and s3[index] == s1[index1]:
                next = (index1 + 1, index2)
                if next not in recorded:
                    record.append(next)
                    recorded.add(next)
        return False
