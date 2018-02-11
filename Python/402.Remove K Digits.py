"""
402. Remove K Digits

Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


class Solution:

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if num is None or len(num) == 0 or len(num) <= k:
            return "0"

        tasks = list()
        tasks.append((num, len(num) - k, ""))
        while len(tasks) > 0:
            input, num_count, pre_str = tasks.pop()
            if num_count == 0:
                return str(int(pre_str))
            first_choice = input[0:len(input) - num_count + 1]
            idx, smallest = 0, int(first_choice[0])
            for i, s in enumerate(first_choice):
                if int(s) < smallest:
                    idx = i
                    smallest = int(s)
            tasks.append((input[idx + 1:], num_count - 1, pre_str + input[idx]))
