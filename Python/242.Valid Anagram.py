"""
242. Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return s is None and t is None

        if len(s) != len(t):
            return False

        s_dict = dict()
        for c in s:
            count = 1 if c not in s_dict else s_dict[c] + 1
            s_dict[c] = count

        t_dict = dict()
        for c in t:
            count = 1 if c not in t_dict else t_dict[c] + 1
            t_dict[c] = count

        return s_dict == t_dict
