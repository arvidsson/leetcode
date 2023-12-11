# Given an array of prices of a stock, what is the max profit you can get when doing a single buy one day and then a single sell on a following day.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for price in prices:
            if price < buy_price:
                buy_price = price
            if price - buy_price > max_profit:
                max_profit = price - buy_price
        return max_profit


input = [7, 2, 1000, 1, 6, 4]
print(Solution().maxProfit(input))
