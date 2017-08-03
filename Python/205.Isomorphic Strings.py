"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return s is None and t is None
        if len(s) == 0 or len(t) == 0:
            return len(s) == 0 and len(t) == 0

        s_to_t_dict = {}
        t_to_s_dict = {}

        for i in range(0, len(s)):
            c_s = s[i]
            c_t = t[i]
            if c_s not in s_to_t_dict and c_t not in t_to_s_dict:
                s_to_t_dict[c_s] = c_t
                t_to_s_dict[c_t] = c_s
            elif c_s in s_to_t_dict and s_to_t_dict[c_s] != c_t:
                return False
            elif c_t in t_to_s_dict and t_to_s_dict[c_t] != c_s:
                return False
        return True
