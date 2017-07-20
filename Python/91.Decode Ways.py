"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        record = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                record[i] = 0
                continue

            count = 0
            if i == len(s) - 1:
                count = 1
            else:
                count = record[i + 1]
                num = int(s[i]) * 10 + int(s[i + 1])
                if 10 <= num <= 26:
                    if i + 2 in record:
                        count += record[i + 2]
                    else:
                        count += 1
            record[i] = count
        return record[0]
