"""
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""


class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        index, length = len(s) - 1, -1
        while index >= 0:
            c = s[index]
            if c == ' ':
                if length == -1:
                    index -= 1
                    continue
                else:
                    break
            else:
                if length == -1:
                    length = 1
                else:
                    length += 1
                index -= 1

        return length if length != -1 else 0


s = Solution()
print(s.lengthOfLastWord("Hello nerd  "))
