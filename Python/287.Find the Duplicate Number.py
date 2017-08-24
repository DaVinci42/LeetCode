"""
287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        slow, fast = 0, nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        value, count = slow, 1
        slow = nums[slow]
        while slow != value:
            slow = nums[slow]
            count += 1

        slow, fast = 0, 0
        for i in range(0, count):
            fast = nums[fast]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
