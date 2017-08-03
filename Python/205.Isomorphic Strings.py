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

        s_dict = {}
        for i in range(0, len(s)):
            c = s[i]
            if c not in s_dict:
                c_tuple = ()
                c_tuple += (i,)
                s_dict[c] = c_tuple
            else:
                s_dict[c] += (i,)

        t_dict = {}
        for i in range(0, len(t)):
            c = t[i]
            if c not in t_dict:
                c_tuple = ()
                c_tuple += (i,)
                t_dict[c] = c_tuple
            else:
                t_dict[c] += (i,)

        s_set, t_set = set(), set()
        for c in s_dict:
            s_set.add(s_dict[c])

        for c in t_dict:
            t_set.add(t_dict[c])
        return s_set == t_set
