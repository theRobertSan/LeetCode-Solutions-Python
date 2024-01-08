from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        directEmployees = defaultdict(list)

        for subordinate, manager in enumerate(manager):
            if manager != -1:
                directEmployees[manager].append(subordinate)

        def dfs(employee: int):
            if employee not in directEmployees:
                return 0

            maxSubordinateTime = 0
            for subordinate in directEmployees[employee]:
                maxSubordinateTime = max(maxSubordinateTime, dfs(subordinate))

            return informTime[employee] + maxSubordinateTime

        return dfs(headID)
