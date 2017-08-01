"""
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers is None or len(numbers) < 2:
            return []
        if numbers[0] + numbers[1] > target:
            return []
        if numbers[-1] + numbers[-2] < target:
            return []

        for i in range(0, len(numbers) - 1):
            j = self.find_index(
                numbers, i + 1, len(numbers) - 1, target - numbers[i])
            if j == -1:
                continue
            else:
                return [i + 1, j + 1]

    def find_index(self, nums, left, right, target):
        while right - left > 1:
            mid = (left + right) // 2
            mid_v = nums[mid]
            if mid_v > target:
                right = mid
            elif mid_v < target:
                left = mid
            else:
                return mid

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
