from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total, buy = 0, prices[0]

        for i in range(len(prices) - 1):
            curDay, nextDay = prices[i], prices[i + 1]

            if curDay >= nextDay:
                total += curDay - buy
                buy = nextDay

        total += prices[-1] - buy

        return total
