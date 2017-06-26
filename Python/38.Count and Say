"""
38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 1:
            return '1'
        i, result = 0, '1'
        while i < n - 1:
            result = self.convert_seq(result)
            i += 1
        return result

    def convert_seq(self, seq):
        result = ''
        pre, count = seq[0], 0
        for i in range(0, len(seq)):
            c = seq[i]
            if c == pre:
                count += 1
            else:
                result += (str(count) + str(pre))
                count = 1
                pre = c
        return result + (str(count) + str(pre))
