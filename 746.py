from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr, next = cost[-2], cost[-1]

        for i in range(len(cost) - 3, -1, -1):
            curr, next = cost[i] + min(curr, next), curr

        return min(curr, next)
