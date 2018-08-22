"""
658. Find K Closest Elements

Given a sorted array, two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
Absolute value of elements in the array and x will not exceed 10^4
"""


class Solution:

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return list()
        if k > len(arr) or k <= 0:
            return list()

        diff_dict = dict()
        for a in arr:
            diff = abs(x - a)
            nums = () if diff not in diff_dict else diff_dict[diff]
            diff_dict[diff] = nums + (a,)

        result, keys = list(), list(diff_dict.keys())
        keys.sort()

        for i in keys:
            nums = list(diff_dict[i])
            current_length, add_length = len(result), len(nums)
            if current_length + add_length == k:
                result += nums
                result.sort()
                return result
            elif current_length + add_length > k:
                nums.sort()
                result += nums[:k - current_length]
                result.sort()
                return result
            else:
                result += nums
