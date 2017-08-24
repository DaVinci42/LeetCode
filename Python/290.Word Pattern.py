"""
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters,
and str contains lowercase letters separated by a single space.
"""


class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern is None or len(pattern) == 0 or str is None or len(str) == 0:
            return (pattern is None or len(pattern) == 0) and (str is None or len(str) == 0)
        words = str.split(" ")

        if len(pattern) != len(words):
            return False

        c_to_word_dic = dict()
        word_to_c_dic = dict()

        for i, c in enumerate(pattern):
            word = words[i]
            if c not in c_to_word_dic and word not in word_to_c_dic:
                c_to_word_dic[c] = word
                word_to_c_dic[word] = c
            elif c in c_to_word_dic and word in word_to_c_dic:
                if c_to_word_dic[c] == word and word_to_c_dic[word] == c:
                    continue
                else:
                    return False
            else:
                return False

        return True
