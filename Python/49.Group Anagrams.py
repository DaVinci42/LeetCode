"""
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return list()

        result_dict = dict()
        for s in strs:
            key = list(s)
            key.sort()
            key = tuple(key)
            if key in result_dict:
                value = result_dict[key]
                value += (s,)
            else:
                value = (s,)
            result_dict[key] = value

        result = map(lambda x: list(x), result_dict.values())
        return list(result)


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
