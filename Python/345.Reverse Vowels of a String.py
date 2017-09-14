"""
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""


class Solution(object):

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return s

        vowel_set, c_list = set(
            ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]), list(s)
        vowel_list = list()
        for i, c in enumerate(c_list):
            if c in vowel_set:
                vowel_list.append(c)
        vowel_list = vowel_list[::-1]

        if len(vowel_list) == 0:
            return s

        for i in range(len(c_list) - 1, -1, -1):
            c = c_list[i]
            if c in vowel_set:
                c_list[i] = vowel_list[-1]
                del vowel_list[-1]
        return "".join(c_list)
