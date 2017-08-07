"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if ((nums1 is None or len(nums1) == 0) and
                (nums2 is None or len(nums2) == 0)):
            return 0

        length1, length2 = len(nums1), len(nums2)
        all = length1 + length2
        if all % 2 == 0:
            v1 = self.find_kth(nums1, nums2, 0, 0, all // 2)
            v2 = self.find_kth(nums1, nums2, 0, 0, all // 2 + 1)
            return (v1 + v2) / 2.0
        else:
            return self.find_kth(nums1, nums2, 0, 0, all // 2 + 1)

    def find_kth(self, nums1, nums2, s1, s2, k):
        if len(nums1) - s1 > len(nums2) - s2:
            return self.find_kth(nums2, nums1, s2, s1, k)
        if s1 >= len(nums1):
            return nums2[s2 + k - 1]
        if k == 1:
            return min(nums1[s1], nums2[s2])

        i1, i2 = min(s1 + k // 2 - 1, len(nums1) - 1), s2 + k // 2 - 1
        v1, v2 = nums1[i1], nums2[i2]

        if v1 <= v2:
            return self.find_kth(nums1, nums2, i1 + 1, s2,
                                 k - (i1 - s1 + 1))
        elif v1 > v2:
            return self.find_kth(nums1, nums2, s1, i2 + 1,
                                 k - (i2 - s2 + 1))
