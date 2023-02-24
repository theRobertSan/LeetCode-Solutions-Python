from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[sell] <= prices[buy]:
                buy = sell
            else:
                max_profit = max(max_profit, prices[sell] - prices[buy])

            sell += 1

        return max_profit
