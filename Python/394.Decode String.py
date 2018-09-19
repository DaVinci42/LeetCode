"""
394. Decode String

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore,
you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""


class Solution:

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        stack, nums = list(), set([str(i) for i in range(0, 10)])

        for letter in s:
            if letter != ']':
                stack.append(letter)
            else:
                right_letter, content = stack[-1], list()
                while right_letter != '[':
                    right_letter = stack.pop()
                    content.append(right_letter)
                    right_letter = stack[-1]
                stack.pop()
                content = content[::-1]

                n, count = stack[-1], list()
                while n in nums and stack:
                    n = stack.pop()
                    count.append(n)
                    if stack:
                        n = stack[-1]
                count = "".join(count[::-1])
                stack += (content * int(count))

        return "".join(stack)
