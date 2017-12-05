"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""


class Solution:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 4, 5, 6]))
