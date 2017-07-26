"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        dic, max_length, tmp_length = {}, 0, 0
        sub_start = 0
        for i in range(0, len(s)):
            letter = s[i]
            if letter not in dic:
                tmp_length += 1
                dic[letter] = i
            else:
                for j in range(sub_start, dic[letter]):
                    del dic[s[j]]
                sub_start = dic[letter] + 1
                dic[letter] = i
                tmp_length = i - sub_start + 1

            if tmp_length > max_length:
                max_length = tmp_length
        return max_length
