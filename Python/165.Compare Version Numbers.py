"""
165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""


class Solution(object):

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 is None:
            return -1
        elif version2 is None:
            return 1

        if version1.startswith('.'):
            version1 = "0" + version1
        if version2.startswith('.'):
            version2 = "0" + version2

        a1, a2 = version1.split("."), version2.split(".")
        a1, a2 = a1[::-1], a2[::-1]
        a1, a2 = map(lambda x: int(x), a1), map(lambda x: int(x), a2)

        while len(a1) > 0 and len(a2) > 0:
            v1, v2 = a1.pop(), a2.pop()
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        if len(a1) == 0 and len(a2) == 0:
            return 0
        elif len(a1) == 0:
            for i in a2:
                if i != 0:
                    return -1
            return 0
        else:
            for i in a1:
                if i != 0:
                    return 1
            return 0
