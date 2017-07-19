"""
80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        start, removed = 0, 0
        pre_num = nums[0]
        for i, n in enumerate(nums):
            if n != pre_num:
                self.forward_list(nums, start, min(i, start + 2), removed)
                count = i - start
                if count > 2:
                    removed += (count - 2)
                start, pre_num = i, n

        self.forward_list(nums, start, min(len(nums), start + 2), removed)
        count = len(nums) - start
        if count > 2:
            removed += (count - 2)
        return len(nums) - removed

    def forward_list(self, nums, start, end, step):
        for i in range(start, end):
            nums[i - step] = nums[i]
