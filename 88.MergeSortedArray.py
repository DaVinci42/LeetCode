from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums1 or not nums2:
            return

        n1 = nums1[:m]
        i, j = 0, 0
        while i < m or j < n:
            if i >= m:
                nums1[i + j] = nums2[j]
                j += 1
                continue
            if j >= n:
                nums1[i + j] = n1[i]
                i += 1
                continue

            if n1[i] <= nums2[j]:
                nums1[i + j] = n1[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1

