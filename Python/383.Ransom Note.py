"""
383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote is None or len(ransomNote) == 0:
            return True
        if magazine is None or len(ransomNote) == 0:
            return False

        ransom_dict = dict()
        for c in ransomNote:
            count = ransom_dict[c] if c in ransom_dict else 0
            ransom_dict[c] = count + 1

        for c in magazine:
            if c in ransom_dict:
                c_count = ransom_dict[c]
                if c_count == 1:
                    del ransom_dict[c]
                else:
                    ransom_dict[c] = c_count - 1

        return len(ransom_dict) == 0
