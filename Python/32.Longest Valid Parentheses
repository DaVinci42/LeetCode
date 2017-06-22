"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""


class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) <= 1:
            return 0
        dict = {}
        length = len(s)
        for i, c in enumerate(s):
            if c == '(' and i + 1 <= length - 1 and s[i + 1] == ')':
                dict[i] = i + 1

        new_dic = self.join_dict(dict, s)
        while not self.is_dict_equal(dict, new_dic):
            dict = new_dic
            new_dic = self.join_dict(dict, s)

        max = 0
        for k in new_dic:
            length_p = new_dic[k] - k + 1
            max = max if max >= length_p else length_p
        return max

    def join_dict(self, dict, s):
        dict = dict.copy()
        length = len(s)
        key_set = set(dict.keys())
        for l in key_set:
            if l not in dict:
                continue
            r = dict[l]
            if r < length - 1 and r + 1 in dict:
                right = dict[r + 1]
                dict[l] = right
                del dict[r + 1]
            elif (l > 0 and s[l - 1] == '(' and
                  r + 1 <= length - 1 and s[r + 1] == ')'):
                del dict[l]
                dict[l - 1] = r + 1
        return dict

    def is_dict_equal(self, dic1, dic2):
        l1 = len(dic1.keys())
        l2 = len(dic2.keys())
        if l1 != l2:
            return False
        for k in dic1:
            v = dic1[k]
            if k not in dic2 or dic2[k] != v:
                return False
        return True
