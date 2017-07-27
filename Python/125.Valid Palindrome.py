"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""


class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True

        s_list = list(filter(lambda c: 65 <= ord(c.upper()) <= 90 or
                             48 <= ord(c.upper()) <= 57, s))
        length = len(s_list)
        if length == 0:
            return True

        left, right = 0, length - 1
        while right > left:
            c_left = s_list[left].upper()
            c_right = s_list[right].upper()

            if c_left == c_right:
                left += 1
                right -= 1
            else:
                return False
        return True
