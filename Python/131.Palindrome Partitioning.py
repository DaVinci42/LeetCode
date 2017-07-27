"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

"""


class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if s is None or len(s) == 0:
            return result
        self.partition_string([], s, result)
        return result

    def partition_string(self, pre_list, s, result):
        if len(s) == 1:
            pre_list.append(s)
            result.append(pre_list)
            return

        for i in range(1, len(s) + 1):
            sub = s[:i]
            if self.is_pylindrome(sub):
                p_list = pre_list[:]
                p_list.append(sub)

                if i == len(s):
                    result.append(p_list)
                else:
                    self.partition_string(p_list, s[i:], result)

    def is_pylindrome(self, s):
        left, right = 0, len(s) - 1
        while right > left:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
