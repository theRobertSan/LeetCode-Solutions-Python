from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        timeSpent = 0
        prev, cur = 0, 1

        while cur < len(colors):
            if colors[prev] == colors[cur]:
                prevTime, curTime = neededTime[prev], neededTime[cur]
                if curTime < prevTime:
                    timeSpent += curTime
                else:
                    timeSpent += prevTime
                    prev = cur
                cur += 1
            else:
                prev = cur
                cur += 1

        return timeSpent
