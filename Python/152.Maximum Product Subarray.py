"""
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution:

    def product(self, nums):
        product = 1
        for i in nums:
            product *= i
        return product

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        zero_list, minus_list = list(), list()
        for i, n in enumerate(nums):
            if n == 0:
                zero_list.append(i)
            if n < 0:
                minus_list.append(i)

        if len(zero_list) > 0:
            split_list = list()
            pre_start = 0
            for i in zero_list:
                split_list.append(nums[pre_start:i])
                pre_start = i + 1
            split_list.append(nums[zero_list[-1] + 1:])
            result_list = map(lambda n: self.maxProduct(n), split_list)
            num_result = max(result_list)
            return max([num_result, 0])

        if len(minus_list) % 2 == 0:
            return self.product(nums)
        elif len(minus_list) == 1:
            minus_index = minus_list[0]
            left_product = self.product(nums[:minus_index])
            right_product = self.product(nums[minus_index + 1:])
            return max([left_product, right_product])
        else:
            left_index, right_index = minus_list[0], minus_list[-1]
            left_product = self.product(nums[:left_index])
            middle_product = self.product(nums[left_index + 1: right_index])
            right_product = self.product(nums[right_index + 1:])
            return (-1 * middle_product *
                    max([left_product * nums[left_index] * -1, right_product * nums[right_index] * -1]))
