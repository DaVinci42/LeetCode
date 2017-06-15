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
        dict = {}
        max_len, tmp_len = 0, 0
        i, j = 0, 0
        for j in range(0, len(s)):
            n = s[j]
            if n in dict:
                if max_len < tmp_len:
                    max_len = tmp_len

                pre = dict[n]
                for k in range(i, pre + 1):
                    dict.pop(s[k])

                i = pre + 1
                tmp_len = j - i + 1
            else:
                tmp_len += 1
            dict[n] = j
            j += 1

        if max_len < tmp_len:
            max_len = tmp_len

        return max_len
