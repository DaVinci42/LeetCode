"""
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
"""


class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if nums1 is None:
            return nums2
        if nums2 is None:
            return nums1

        index_1, index_2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            max = 0
            if index_1 >= 0 and index_2 >= 0:
                v_1 = nums1[index_1]
                v_2 = nums2[index_2]
                if v_1 >= v_2:
                    max = v_1
                    index_1 -= 1
                else:
                    max = v_2
                    index_2 -= 1
            elif index_1 < 0:
                max = nums2[index_2]
                index_2 -= 1
            else:
                max = nums1[index_1]
                index_1 -= 1

            nums1[i] = max
