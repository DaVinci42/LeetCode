"""
151. Reverse Words in a String

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
"""


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ""
        a = s.split(" ")
        return " ".join(a[::-1])