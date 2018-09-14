"""
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(s) < len(p):
            return list()

        target_dict = dict()
        for l in p:
            count = 0 if l not in target_dict else target_dict[l]
            target_dict[l] = count + 1

        start, current_dict, result = 0, dict(), list()
        for i in range(start, len(p)):
            l = s[i]
            count = 0 if l not in current_dict else current_dict[l]
            current_dict[l] = count + 1
        while start < len(s) - len(p):
            if self.same_dict(current_dict, target_dict):
                result.append(start)

            removed, added = s[start], s[start + len(p)]
            if current_dict[removed] == 1:
                del current_dict[removed]
            else:
                current_dict[removed] = current_dict[removed] - 1
            if added in current_dict:
                current_dict[added] = current_dict[added] + 1
            else:
                current_dict[added] = 1
            start += 1
        if self.same_dict(current_dict, target_dict):
            result.append(start)

        return result

    def same_dict(self, d1, d2):
        if len(d1.keys()) != len(d2.keys()):
            return False
        for k in d1:
            if k not in d2 or d1[k] != d2[k]:
                return False
        return True
