"""
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution(object):

    money = {}

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        self.money = {}
        return self.max_money(nums, len(nums) - 1)

    def max_money(self, nums, index):
        if index in self.money:
            return self.money[index]

        money = 0
        if index == 0:
            money = nums[0]
        elif index == 1:
            money = max(nums[0], nums[1])
        else:
            money = max(self.max_money(nums, index - 1),
                        self.max_money(nums, index - 2) + nums[index])
        self.money[index] = money
        return money
