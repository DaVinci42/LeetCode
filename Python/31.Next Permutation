"""
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
"""


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return

        length = len(nums)
        i, target = length - 1, length
        tmp_list = []
        while i >= 1:
            v = nums[i]
            tmp_list.append(v)
            if nums[i - 1] < v:
                target = i - 1
                break
            i -= 1

        if target == length:
            self.reverse_list(nums)
        else:
            v_target = nums[target]
            tmp_list.append(v_target)
            tmp_list.sort()

            next = v_target
            for i in tmp_list:
                if i > v_target:
                    next = i
                    break
            tmp_list.remove(next)
            nums[target] = next
            for i, v in enumerate(tmp_list):
                nums[target + i + 1] = v

    def reverse_list(self, nums):
        i, j = 0, len(nums) - 1
        while j > i:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
