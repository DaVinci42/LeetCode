"""
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if (nums1 is None or nums2 is None or
                len(nums1) == 0 or len(nums2) == 0):
            return list()

        dict1 = dict()
        for n in nums1:
            count = 0 if n not in dict1 else dict1[n]
            dict1[n] = count + 1

        dict2 = dict()
        for n in nums2:
            count = 0 if n not in dict2 else dict2[n]
            dict2[n] = count + 1

        intersect_set = set(nums1) & set(nums2)
        result = list()
        for n in intersect_set:
            count = min(dict1[n], dict2[n])
            result += [n] * count
        return result
