"""
122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0

        sum_profit, pre_price = 0, prices[0]
        for i in range(1, len(prices)):
            p = prices[i]
            if p > pre_price:
                sum_profit += (p - pre_price)
                pre_price = p
            elif p < pre_price:
                pre_price = p
        return sum_profit
